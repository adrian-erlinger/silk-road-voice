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
DEFAULT_OUTPUT_LANGUAGE = "English"
LANGUAGE_OPTIONS = {
    "en": "English",
    "uz": "Uzbek Latin",
    "ru": "Russian",
    "tj": "Tajik",
    "english": "English",
    "uzbek": "Uzbek Latin",
    "russian": "Russian",
    "tajik": "Tajik",
}
STAFF_REVIEW_REMINDERS = {
    "English": (
        "Staff reminder: Review and edit the suggested reply before sending. "
        "Do not treat risk-sensitive sections as final official advice."
    ),
    "Uzbek Latin": (
        "Xodimlar uchun eslatma: Tavsiya etilgan javobni yuborishdan oldin "
        "ko'rib chiqing va tahrir qiling. Xavfli mavzular bo'yicha bo'limlarni "
        "yakuniy rasmiy maslahat deb qabul qilmang."
    ),
    "Russian": (
        "Напоминание для сотрудников: проверьте и отредактируйте рекомендуемый "
        "ответ перед отправкой. Не считайте разделы о рисках окончательной "
        "официальной консультацией."
    ),
    "Tajik": (
        "Ёддошт барои кормандон: ҷавоби тавсияшударо пеш аз фиристодан "
        "санҷед ва таҳрир кунед. Қисматҳои марбут ба хавфро ҳамчун маслиҳати "
        "ниҳоии расмӣ қабул накунед."
    ),
}
LANGUAGE_CONFIRMATIONS = {
    "English": (
        "Operator output language has been set to English. "
        "You can now paste a traveler message. The suggested traveler-facing "
        "reply will remain in the traveler's detected language."
    ),
    "Uzbek Latin": (
        "Operator chiqish tili Uzbek Latin qilib o'rnatildi. "
        "Endi sayohatchi xabarini joylashingiz mumkin. Sayohatchiga tavsiya "
        "etilgan javob uning aniqlangan tilida qoladi."
    ),
    "Russian": (
        "Язык вывода для оператора установлен: русский. "
        "Теперь можно вставить сообщение путешественника. Рекомендуемый ответ "
        "для путешественника останется на определенном языке путешественника."
    ),
    "Tajik": (
        "Забони баромад барои оператор ба тоҷикӣ танзим шуд. "
        "Акнун метавонед паёми сайёҳро гузоред. Ҷавоби тавсияшуда барои сайёҳ "
        "ба забони муайяншудаи худи сайёҳ мемонад."
    ),
}


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


def get_language_instructions(output_language: str) -> str:
    """Return simple LLM instructions for the selected operator language."""
    if output_language == "Uzbek Latin":
        return (
            "Use the Uzbek Latin section headings from the prompt. Write all "
            "operator-facing analysis, labels, notes, and internal guidance in "
            "Uzbek using Latin script. Keep the actual traveler-facing draft reply "
            "in the traveler's detected original language, defaulting to English "
            "if unclear."
        )
    if output_language == "Russian":
        return (
            "Use the Russian section headings from the prompt. Write all "
            "operator-facing analysis, labels, notes, and internal guidance in "
            "Russian. Keep the actual traveler-facing draft reply in the "
            "traveler's detected original language, defaulting to English if "
            "unclear."
        )
    if output_language == "Tajik":
        return (
            "Use the Tajik section headings from the prompt. Write all "
            "operator-facing analysis, labels, notes, and internal guidance in "
            "Tajik using clear, practical operator-facing language. Keep the actual "
            "traveler-facing draft reply in the traveler's detected original "
            "language, defaulting to English if unclear."
        )
    return (
        "Use the English section headings from the prompt. Write all "
        "operator-facing analysis, labels, notes, and internal guidance in English. "
        "Keep the actual traveler-facing draft reply in the traveler's detected "
        "original language, defaulting to English if unclear."
    )


def analyze_traveler_request(
    traveler_message: str, output_language: str = DEFAULT_OUTPUT_LANGUAGE
) -> str:
    """Send a traveler message to the LLM and return an operator summary."""
    missing = get_missing_env_vars()
    if missing:
        missing_list = ", ".join(missing)
        raise RuntimeError(f"Setup error: missing required environment variable(s): {missing_list}")

    prompt_template = load_prompt_template()
    sensitive_topics = detect_sensitive_topics(traveler_message)
    topic_note = ", ".join(sensitive_topics) if sensitive_topics else "None detected by keyword check"
    language_instructions = get_language_instructions(output_language)

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
                        f"Selected output language: {output_language}\n"
                        f"Language instructions: {language_instructions}\n\n"
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
        "English:\n"
        "Internal bot for tour operator staff. It analyzes pasted traveler "
        "requests and drafts a reply for staff review. It does not send messages "
        "to travelers automatically. Choose output language with /language EN, "
        "/language UZ, /language RU, or /language TJ. Then paste a traveler message.\n\n"
        "Uzbek Latin:\n"
        "Tur operator xodimlari uchun ichki bot. U sayohatchi xabarlarini tahlil "
        "qiladi va xodimlar ko'rib chiqishi uchun javob qoralamasini tayyorlaydi. "
        "Sayohatchilarga avtomatik xabar yubormaydi. Tilni /language EN, "
        "/language UZ, /language RU yoki /language TJ bilan tanlang. Keyin "
        "sayohatchi xabarini joylang.\n\n"
        "Русский:\n"
        "Внутренний бот для сотрудников туроператора. Он анализирует сообщения "
        "путешественников и готовит черновик ответа для проверки сотрудником. "
        "Он не отправляет сообщения путешественникам автоматически. Выберите язык: "
        "/language EN, /language UZ, /language RU или /language TJ. Затем вставьте "
        "сообщение путешественника.\n\n"
        "Тоҷикӣ:\n"
        "Боти дохилӣ барои кормандони туроператор. Паёмҳои сайёҳонро таҳлил "
        "мекунад ва ҷавоби пешнависро барои санҷиши корманд омода мекунад. "
        "Ба сайёҳон худкор паём намефиристад. Забонро бо /language EN, "
        "/language UZ, /language RU ё /language TJ интихоб кунед. Сипас паёми "
        "сайёҳро гузоред."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show simple usage instructions."""
    await update.message.reply_text(
        "How to use:\n"
        "1. Paste one traveler message into this chat.\n"
        "2. Review the structured operator summary.\n"
        "3. Check any risk flags and missing information.\n"
        "4. Edit the suggested reply before sending it to the traveler.\n\n"
        "Choose output language:\n"
        "/language EN = English\n"
        "/language UZ = Uzbek Latin\n"
        "/language RU = Russian\n"
        "/language TJ = Tajik\n\n"
        "Full names also work: /language english, /language uzbek, "
        "/language russian, /language tajik.\n\n"
        "This bot does not send messages to travelers automatically. It must not "
        "be used as final advice for visa, customs, registration, safety, legal, "
        "medical, permit, drone, restricted-area, or commercial-filming questions."
    )


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Set the operator output language for this Telegram chat in memory."""
    if not context.args:
        await update.message.reply_text(
            "Choose an output language by sending one of these commands:\n"
            "/language EN\n"
            "/language UZ\n"
            "/language RU\n"
            "/language TJ\n\n"
            "Full names also work: english, uzbek, russian, tajik."
        )
        return

    requested_language = context.args[0].lower()
    selected_language = LANGUAGE_OPTIONS.get(requested_language)

    if not selected_language:
        await update.message.reply_text(
            "Unsupported language. Please use one of these commands:\n"
            "/language EN\n"
            "/language UZ\n"
            "/language RU\n"
            "/language TJ"
        )
        return

    context.chat_data["output_language"] = selected_language
    await update.message.reply_text(LANGUAGE_CONFIRMATIONS[selected_language])


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Analyze pasted traveler text and return the structured operator output."""
    traveler_message = update.message.text.strip()
    if not traveler_message:
        await update.message.reply_text("Please paste a traveler message as text.")
        return

    await update.message.chat.send_action(action=ChatAction.TYPING)

    try:
        output_language = context.chat_data.get("output_language", DEFAULT_OUTPUT_LANGUAGE)
        summary = analyze_traveler_request(traveler_message, output_language)
    except RuntimeError as exc:
        await update.message.reply_text(str(exc))
        return
    except Exception:
        await update.message.reply_text(
            "Unexpected error: the request could not be analyzed. Please try again "
            "or ask a technical operator to check the bot logs."
        )
        return

    output_language = context.chat_data.get("output_language", DEFAULT_OUTPUT_LANGUAGE)
    reminder = f"\n\n{STAFF_REVIEW_REMINDERS.get(output_language, STAFF_REVIEW_REMINDERS[DEFAULT_OUTPUT_LANGUAGE])}"
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
    application.add_handler(CommandHandler("language", language_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_error_handler(error_handler)

    print("Voice of the Silk Road bot is running. Press Ctrl+C to stop.")
    application.run_polling()


if __name__ == "__main__":
    main()
