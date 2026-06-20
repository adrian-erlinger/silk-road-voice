# Voice of the Silk Road

**Telegram-first AI intake toolkit for Uzbek tour operators handling multilingual traveler requests.**

Voice of the Silk Road is a pilot-stage concept for Uzbek tour operators serving a growing influx of international travelers. The toolkit helps local tour staff understand foreign traveler requests, interpret cultural expectations, identify missing logistics, flag issues that require human review, and prepare clear responses in Uzbek Latin, Russian, or Tajik.

The project is designed around a real operating constraint: many tour operators already run their business through Telegram. The goal is not to replace that workflow. The goal is to make Telegram-based communication easier, faster, and more reliable for multilingual tourism teams.

## Problem

Tourism in Uzbekistan is growing quickly, and local tour companies increasingly serve travelers from Europe, East Asia, Central Asia, and other regions. Many travelers communicate in English or other foreign languages, often with accents, idioms, or expectations that are difficult for local staff to interpret.

Tour operators may have strong English speakers on the team, but language skills are uneven across staff. Older guides, drivers, coordinators, and operations staff may rely on Uzbek, Russian, or Tajik. This creates bottlenecks, slows response time, and increases the risk that traveler expectations are misunderstood.

The harder problem is not only translation. Travelers often ask for experiences using culturally loaded terms such as “authentic,” “local,” “hidden gem,” “ethical,” “immersive,” “safe,” or “off the beaten path.” Local operators need to understand what the traveler likely means, what can realistically be delivered, and where a careful human response is needed.

## Version 1 Scope

Version 1 focuses on one workflow:

**Traveler Request Intake**

A tour operator receives a traveler message through Telegram. The message may be written in English, French, German, Italian, Japanese, Korean, Chinese, or another language. The toolkit converts the request into an operator-ready summary that can be reviewed by local staff.

## Intended Users

Primary users:

* Tour operator staff in Uzbekistan
* Operations managers
* Local guides
* Drivers and field staff
* Younger English-speaking coordinators supporting older or non-English-speaking staff

Traveler-facing use is a later phase. Version 1 is designed for internal tour operator operations.

## Operator Languages

The toolkit is designed to support outputs for local staff in:

* Uzbek, Latin script
* Russian
* Tajik

## Traveler Languages

The toolkit is designed to support intake from travelers using:

* English
* French
* German
* Italian
* Japanese
* Korean
* Chinese

Additional languages can be added later.

## Target Output

For each traveler request, the toolkit should produce a structured operator summary:

```text
Traveler intent:
Trip summary:
Key details:
Missing information:
Cultural interpretation:
Risk or compliance flags:
Suggested operator reply:
Internal preparation notes:
```

## Example Use Case

A traveler sends a Telegram message:

> We are two friends visiting Uzbekistan next month. We want something authentic and local, not too touristy. We are interested in food, Soviet architecture, and maybe a homestay. We are vegetarian and prefer women-led experiences if possible. We only have five days.

The toolkit should help the operator understand:

* The traveler wants a curated experience, not only standard sightseeing.
* “Authentic and local” may mean small-group, community-based, or less commercial experiences.
* Vegetarian food must be checked carefully in advance.
* Women-led experiences may require specific guide or host matching.
* Five days may be too short for an overly broad itinerary.
* The operator should ask follow-up questions before confirming availability.

## What This Project Is

This project is:

* A Telegram-first workflow concept
* A traveler request intake framework
* A multilingual operations support toolkit
* A cultural interpretation aid for tour operators
* A pilot-readiness project for future AI voice and translation features

## What This Project Is Not

This project is not:

* A full booking platform
* A replacement for human guides
* A production tourism management system
* A legal, visa, customs, or safety authority
* A fully automated response system
* A tool for making final decisions without human review

## Safety and Human Review

Tourism involves real people, money, travel logistics, cultural expectations, and safety considerations. The toolkit should flag issues that require human review rather than making final decisions automatically.

Risk and compliance flags should eventually be grounded in official Uzbekistan government sources, such as visa, customs, registration, safety, and tourism regulations. Version 1 will begin with a basic risk register and escalation framework.

## Success Metrics

The pilot will focus on three practical outcomes:

1. Faster response time to traveler inquiries
2. Fewer misunderstood traveler requests
3. More bookings converted through clearer communication and better expectation alignment

## Planned Repository Contents

```text
README.md
traveler_request_intake_template.md
sample_scenarios.md
cultural_intent_glossary.md
operator_output_format.md
risk_and_escalation_register.md
telegram_response_templates.md
pilot_success_metrics.md
```

## Future Roadmap

Possible future features:

* Telegram bot for text-based traveler request intake
* Voice-note transcription
* Multilingual summary generation
* Suggested Telegram replies in Uzbek, Russian, Tajik, and English
* Cultural intent glossary expansion
* Official-rules risk reference layer
* ElevenLabs voice output for operator briefings or traveler-facing audio
* Pre-tour multilingual audio briefings
* Guide support during live tours
* Post-tour feedback summarization

## Project Status

Early concept and pilot-readiness design.

## Run Locally

This project includes a minimal Telegram bot scaffold for Version 1.

The bot currently runs locally from a developer machine. It is not yet deployed to a server.

### Requirements

```text
Python 3
Telegram bot token from BotFather
OpenAI API key
```

### Setup

Clone the repository:

```bash
git clone https://github.com/adrian-erlinger/silk-road-voice.git
cd silk-road-voice
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a private local environment file:

```bash
cp .env.example .env
```

Edit `.env` and add private credentials:

```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
LLM_API_KEY=your_openai_api_key_here
LLM_MODEL=gpt-4o-mini
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
```

Do not commit `.env` to GitHub.

### Run the Bot

Start the bot locally:

```bash
python3 bot.py
```

When the bot is running, Telegram messages sent to the bot will be processed by the local Python process.

To stop the bot:

```text
Control + C
```

### Current Limitations

Version 1 is a local prototype.

It does not yet include:

```text
Cloud deployment
Persistent database
User accounts
Voice-note intake
Automatic traveler messaging
Payment or booking management
Official-rule lookup
Reddit scraping or web scraping
Maps API place lookup is planned but not yet implemented
```

The bot is designed for internal operator review only. Staff must review and edit any suggested reply before sending it to a traveler.

