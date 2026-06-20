"""Minimal Telegram bot for Voice of the Silk Road Version 1.

The bot supports one workflow: internal traveler request intake for Uzbek tour
operators. It does not store traveler messages or send replies to travelers.
"""

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


PROMPT_PATH = Path("prompts/traveler_intake_prompt.md")
MAX_TELEGRAM_MESSAGE_LENGTH = 4000
REQUIRED_ENV_VARS = ("TELEGRAM_BOT_TOKEN", "LLM_API_KEY", "LLM_MODEL")


# These terms do not answer official questions. They only help the prompt flag
# requests that need human review and official-source checking.
SENSITIVE_TOPIC_KEYWORDS = {
    "visa": "visa",
    "customs": "customs",
    "registration": "registration",
    "register": "registration",
    "permit": "permit",
    "drone": "drone use",
    "restricted": "restricted area",
    "border": "border or restricted area",
    "film": "commercial filming or site rules",
    "filming": "commercial filming or site rules",
    "documentary": "commercial filming or site rules",
    "youtube": "commercial filming or site rules",
    "photograph": "photography rules",
    "photo": "photography rules",
    "police": "sensitive photography or safety issue",
    "military": "sensitive photography or safety issue",
    "medicine": "medical or customs issue",
    "medical": "medical issue",
    "doctor": "medical issue",
    "hospital": "medical issue",
    "safe": "safety-sensitive request",
    "safety": "safety-sensitive request",
    "legal": "legal issue",
    "law": "legal issue",
}


# Load environment variables from .env before reading configuration.
load_dotenv()


def get_missing_env_vars() -> list[str]:
    """Return required environment variables that are missing or blank."""
    return [name for name in REQUIRED_ENV_VARS if not os.getenv(name)]


def load_prompt_template() -> str:
    """Read the traveler intake prompt from disk."""
    try:
        return PROMPT_PATH.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(f"Prompt file not found: {PROMPT_PATH}") from exc


def detect_sensitive_topics(message: str) -> list[str]:
    """Detect possible risk topics for the LLM to flag, without giving advice."""
    lowered = message.lower()
    topics = sorted(
        {topic for keyword, topic in SENSITIVE_TOPIC_KEYWORDS.items() if keyword in lowered}
    )
    return topics


def analyze_traveler_request(traveler_message: str) -> str:
    """Send a traveler message to the LLM and return an operator summary."""
    missing = get_missing_env_vars()
    if missing:
        missing_list = ", ".join(missing)
        raise RuntimeError(f"Setup error: missing required environment variable(s): {missing_list}")

    prompt_template = load_prompt_template()
    sensitive_topics = detect_sensitive_topics(traveler_message)
    topic_note = ", ".join(sensitive_topics) if sensitive_topics else "None detected by keyword check"

    client = OpenAI(api_key=os.environ["LLM_API_KEY"])

    try:
        response = client.chat.completions.create(
            model=os.environ["LLM_MODEL"],
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": prompt_template,
                },
                {
                    "role": "user",
                    "content": (
                        "Analyze this pasted traveler message for internal operator review.\n\n"
                        f"Sensitive topics detected by keyword check: {topic_note}\n\n"
                        f"Traveler message:\n{traveler_message}"
                    ),
                },
            ],
        )
    except OpenAIError as exc:
        raise RuntimeError(f"LLM request failed: {exc}") from exc

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("LLM returned an empty response.")

    return content.strip()


def split_for_telegram(text: str) -> list[str]:
    """Split long LLM output into Telegram-sized messages."""
    if len(text) <= MAX_TELEGRAM_MESSAGE_LENGTH:
        return [text]

    chunks = []
    remaining = text
    while remaining:
        chunks.append(remaining[:MAX_TELEGRAM_MESSAGE_LENGTH])
        remaining = remaining[MAX_TELEGRAM_MESSAGE_LENGTH:]
    return chunks


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Explain what the bot does when staff send /start."""
    await update.message.reply_text(
        "Voice of the Silk Road helps tour operator staff review pasted traveler "
        "requests. Send a traveler message here and I will return an internal "
        "operator summary, missing information, risk flags, and a suggested reply "
        "for staff to review before sending."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show simple usage instructions."""
    await update.message.reply_text(
        "How to use:\n"
        "1. Paste one traveler message into this chat.\n"
        "2. Review the structured operator summary.\n"
        "3. Check any risk flags and missing information.\n"
        "4. Edit the suggested reply before sending it to the traveler.\n\n"
        "This bot does not send messages to travelers automatically. It must not "
        "be used as final advice for visa, customs, registration, safety, legal, "
        "medical, permit, drone, restricted-area, or commercial-filming questions."
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Analyze pasted traveler text and return the structured operator output."""
    traveler_message = update.message.text.strip()
    if not traveler_message:
        await update.message.reply_text("Please paste a traveler message as text.")
        return

    await update.message.chat.send_action(action=ChatAction.TYPING)

    try:
        summary = analyze_traveler_request(traveler_message)
    except RuntimeError as exc:
        await update.message.reply_text(str(exc))
        return
    except Exception:
        await update.message.reply_text(
            "Unexpected error: the request could not be analyzed. Please try again "
            "or ask a technical operator to check the bot logs."
        )
        return

    reminder = (
        "\n\nStaff reminder: Review and edit the suggested reply before sending. "
        "Do not treat risk-sensitive sections as final official advice."
    )
    for chunk in split_for_telegram(summary + reminder):
        await update.message.reply_text(chunk)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle uncaught Telegram errors without exposing private message content."""
    if isinstance(update, Update) and update.message:
        await update.message.reply_text(
            "Something went wrong while handling this Telegram update. Please try again."
        )


def main() -> None:
    """Start the Telegram bot."""
    missing = get_missing_env_vars()
    if missing:
        missing_list = ", ".join(missing)
        raise RuntimeError(f"Setup error: missing required environment variable(s): {missing_list}")

    application = Application.builder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_error_handler(error_handler)

    print("Voice of the Silk Road bot is running. Press Ctrl+C to stop.")
    application.run_polling()


if __name__ == "__main__":
    main()
