# Build Plan

This file defines the first build plan for Voice of the Silk Road.

The goal is to build a narrow Telegram bot MVP that supports one workflow: traveler request intake for Uzbek tour operators.

## Product Goal

Voice of the Silk Road should help local tour operator staff understand multilingual traveler requests, identify missing information, interpret cultural expectations, flag sensitive issues, and prepare Telegram-ready replies.

The product should fit the way Uzbek tour operators already work: Telegram-first, fast, practical, and easy for mixed-language teams to use.

## Version 1 Workflow

### Traveler Request Intake

A tour operator sends or forwards a traveler message to the bot.

The bot returns a structured operator summary:

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

## Version 1 Users

Primary users:

```text
Tour operator staff in Uzbekistan
Operations managers
Local guides
Drivers and field staff
Younger English-speaking coordinators supporting older or non-English-speaking staff
```

The tool is for internal operator use. It should not automatically communicate with travelers in version 1.

## Version 1 Input

The first version should accept:

```text
Text pasted into Telegram
Forwarded traveler messages
Mixed-language traveler messages
```

The first version does not need to support:

```text
Voice notes
Images
PDFs
Payments
Booking management
Itinerary generation
```

These can be future features.

## Version 1 Output

The first version should return:

```text
Structured operator summary
Missing information checklist
Cultural interpretation notes
Risk flags
Suggested Telegram reply
Internal preparation notes
```

The output should be practical for staff to copy, edit, and send.

## Languages

### Traveler-side intake languages

The workflow should be designed for:

```text
English
French
German
Italian
Japanese
Korean
Chinese
```

### Operator-side output languages

The first implementation can use English as a bridge output.

Future versions should support:

```text
Uzbek, Latin script
Russian
Tajik
```

## Risk and Safety Rules

The bot should not give final advice on:

```text
Visa rules
Customs rules
Registration rules
Photography restrictions
Drone use
Border areas
Restricted zones
Medical issues
Safety guarantees
Legal issues
Permits
Commercial filming
```

When these topics appear, the bot should flag them for human review.

The bot should say that current official sources must be checked before giving final advice.

## Minimum Technical Scope

The first technical build should be simple.

Recommended stack:

```text
Python
python-telegram-bot
OpenAI API or another LLM API
python-dotenv
```

The first version should include:

```text
bot.py
requirements.txt
.env.example
README setup instructions
Prompt template for traveler request intake
Basic error handling
No database
No user accounts
No deployment automation
```

## Suggested Project Structure

```text
silk-road-voice/
  README.md
  build_plan.md
  operator_output_format.md
  traveler_request_intake_template.md
  cultural_intent_glossary.md
  risk_and_escalation_register.md
  telegram_response_templates.md
  pilot_success_metrics.md
  sample_scenarios.md

  bot.py
  requirements.txt
  .env.example
  prompts/
    traveler_intake_prompt.md
```

## Bot Behavior

When a user sends a traveler request, the bot should:

1. Accept the message.
2. Pass it to the LLM with the traveler intake prompt.
3. Return the structured operator summary.
4. Include risk flags when relevant.
5. Avoid making final legal, safety, visa, customs, or medical claims.
6. Remind the operator that all replies should be reviewed before sending.

## Prompt Requirements

The LLM prompt should instruct the model to:

```text
Act as an operations assistant for an Uzbek tour operator.
Preserve traveler meaning rather than translating literally.
Identify cultural expectations and explain them in practical terms.
Separate facts from assumptions.
List missing information.
Flag safety, official-rules, dietary, accessibility, filming, or sensitive requests.
Draft a Telegram-ready reply.
Keep the human operator in control.
Avoid overpromising.
```

## Version 1 Example

Input:

```text
Hi! We are two friends visiting Uzbekistan next month. We want something authentic and local, not too touristy. We are interested in food, Soviet architecture, and maybe a homestay. We are vegetarian and prefer women-led experiences if possible. We only have five days. Can you help?
```

Expected output:

```text
Traveler intent:
The travelers want a short, curated Uzbekistan trip that feels local and less commercial than a standard sightseeing package.

Trip summary:
Two travelers want a five-day trip next month focused on food, Soviet architecture, local experiences, and possibly a homestay.

Key details:
- Number of travelers: 2
- Timing: next month, exact dates missing
- Trip length: 5 days
- Interests: food, Soviet architecture, homestay, local experiences
- Dietary need: vegetarian
- Preference: women-led experiences if available

Missing information:
- Exact dates
- Arrival and departure cities
- Budget range
- Hotel comfort level
- Private or group preference
- Vegetarian details, including meat broth, animal fat, eggs, dairy, or cross-contamination

Cultural interpretation:
“Authentic and local” likely means smaller-scale experiences, interaction with local people, and fewer formulaic tourist stops. The operator should balance major sites with personal or community-based experiences.

Risk or compliance flags:
- Vegetarian meals require confirmation with restaurants and hosts.
- Women-led experiences should not be promised before availability is checked.
- Homestay availability, comfort, and registration requirements should be reviewed.

Suggested operator reply:
Thank you for your message. We can help design a five-day Uzbekistan trip with food, architecture, and local cultural experiences. To prepare the best proposal, could you please send your exact travel dates, arrival and departure cities, budget range, and whether you prefer private guiding or a small group? We will also check vegetarian meal options and whether women-led experiences are available for your dates.

Internal preparation notes:
Check women guide or women-led workshop availability. Confirm vegetarian-friendly restaurants. Consider Tashkent for Soviet architecture and Samarkand or Bukhara for cultural sites. Do not promise a homestay until availability and standards are confirmed.
```

## What Not to Build Yet

Do not build these in version 1:

```text
Full travel booking platform
Payment processing
Customer database
Production CRM
Live itinerary builder
Hotel inventory
Train ticket integration
Voice cloning
Real-time translation during tours
Automatic traveler messaging
Official-rules search engine
```

## Future Roadmap

After the text bot works, possible next steps:

```text
Add operator language selection: Uzbek Latin, Russian, Tajik
Add voice note transcription
Add ElevenLabs text-to-speech for operator briefings
Add maintained official-source reference list
Add scenario testing
Add simple logging for pilot metrics
Add Telegram inline buttons for output language and risk level
Add traveler-facing pre-tour audio briefing generator
```

## Success Standard for the First Build

The first build is successful if:

```text
A tour operator can paste a traveler message into Telegram.
The bot returns a useful structured summary.
The response identifies missing information.
The response explains cultural intent.
The response flags sensitive issues.
The response drafts a usable Telegram reply.
The system avoids final legal, safety, visa, customs, and medical advice.
```
