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

## Source Rules

Voice of the Silk Road uses different source types for different purposes.

### Official Sources

Official sources should be used for rules, regulations, legal requirements, permits, visa issues, customs issues, registration rules, safety requirements, and government guidance.

The bot should not invent or guess official guidance.

When a traveler request involves official rules, the bot should flag the issue for human review and recommend checking the relevant official source before responding.

Examples of official-source topics:

```text
Visa requirements
Customs requirements
Registration requirements
Border zones
Restricted areas
Drone use
Commercial filming
Photography of official buildings, police, military, infrastructure, or religious sites
Medical issues
Legal issues
Safety guarantees
Permits
Emergency situations
```

### Community Sources

Community sources such as r/Uzbekistan, public travel forums, and public trip reports may inform traveler concerns, cultural interpretation, sample scenarios, and response templates.

Community sources should be treated as qualitative research, not as official authority.

The bot should not scrape Reddit, store usernames, copy long comments, or present community comments as verified facts.

Allowed community-source uses:

```text
Identify recurring traveler concerns
Identify cultural expectation gaps
Improve fictionalized sample scenarios
Improve the Cultural Intent Glossary
Improve Telegram response templates
Improve risk flag examples
Improve pilot learning questions
```

Not allowed in version 1:

```text
Automatic Reddit scraping
Bulk comment storage
Username storage
Long quote storage
Bot answers based directly on Reddit comments
Using Reddit as an official source
Using Reddit to answer legal, visa, customs, medical, safety, or permit questions
```

### Human Review

The bot should keep tour operator staff in control.

The bot may summarize traveler messages, identify missing information, interpret cultural expectations, draft replies, and flag risks.

The bot should not send final replies automatically, confirm bookings, promise availability, set prices, guarantee safety, or provide legal, visa, customs, medical, or official guidance.

### Related Files

Codex and future contributors should follow:

```text
source_policy.md
community_research_protocol.md
community_insight_log.md
risk_and_escalation_register.md
```


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

## Future Capability: Source-Aware Operator Copilot

Version 1 began as a traveler request intake assistant.

The next product direction is to make the bot a source-aware operator copilot. The bot should not only summarize traveler requests. It should identify what information the operator needs, what source type is appropriate, and when source-backed lookup is required.

## Why This Matters

Generic outputs are not enough for tour operators.

If a traveler asks:

```text
Can I take photos in the Tashkent metro?
```

the bot should not simply say:

```text
Check the latest regulations.
```

It should identify that this is an official-rule question and tell the operator what kind of source must be checked before responding.

If a traveler asks:

```text
Where can I find Bukhara-style somsa in Tashkent?
```

the bot should not invent a restaurant or bakery.

It should identify that this is a place recommendation request and, when Maps API lookup is available, return source-backed candidate places with clickable links.

## Source-Aware Request Types

The bot should classify traveler requests into one or more of these categories:

```text
No source needed
Official source needed
Place recommendation source needed
Community insight useful
Operator validation needed
```

## Official-Source Requests

Official-source requests include:

```text
Visa rules
Customs rules
Registration rules
Photography rules
Drone use
Commercial filming
Border areas
Restricted zones
Permits
Safety guarantees
Legal issues
Medical issues
```

For these requests, the bot should:

```text
Flag official-source review
Avoid final guidance from memory
Recommend checking the relevant official source or site-specific authority
Ask practical follow-up questions
Keep the human operator in control
```

## Place Recommendation Requests

Place recommendation requests include:

```text
Restaurants
Cafés
Bakeries
Markets
Museums
Craft workshops
Ceramics shops
Silk or textile workshops
Photo spots
Neighborhoods
Attractions
Landmarks
Specific dishes in specific cities
```

For these requests, the future Maps API feature should:

```text
Call a place-search API
Return source-backed candidate places
Include clickable map links
Include address, rating, review count, and opening status when available
Explain why each candidate may match
Include operator validation reminders
Avoid invented places
```

## Planned Maps API Feature

The first implementation should use Google Places API.

The future code should add:

```text
GOOGLE_MAPS_API_KEY
```

as a private environment variable in `.env`.

The key must not be committed to GitHub.

The repo may include a placeholder in `.env.example` when implementation begins.

## Future Output Section

Future bot output should include:

```text
Verified sources and candidate links:
```

This section should appear before:

```text
Risk or compliance flags:
```

For place recommendation requests, it should include API-returned candidate places.

For official-rule requests, it should state that official-source review is needed.

For requests that do not need source-backed lookup, it can state:

```text
No place lookup needed.
```

## Human Review Rule

The bot should return source-backed candidates to the operator.

The bot should not automatically send place recommendations to travelers.

The operator must review candidate places before sending them to a traveler.

The operator should verify:

```text
Current opening hours
Recent reviews
Location suitability
Food quality
Whether the place actually matches the traveler’s requested experience
Dietary fit
Accessibility
Group-size suitability
Traveler comfort level
Local guide confidence
```

## No Hallucinated Places Rule

The bot must not invent restaurant names, shop names, museum names, workshop names, or local recommendations.

If no API result is available, the bot should say so.

If the Maps API fails, the bot should still provide normal intake analysis and a suggested operator search query.

## Implementation Sequence

Recommended implementation order:

```text
1. Add Maps API feature spec
2. Update source policy and output format
3. Add source-need classification
4. Add Maps/source-aware test cases
5. Add GOOGLE_MAPS_API_KEY placeholder to .env.example
6. Add a place-search helper module
7. Add request classification for place recommendation needs
8. Call Google Places API for local recommendation requests
9. Return 3 candidate places with Google Maps links
10. Test against Maps and source-aware test cases
```

## Product Principle

The bot should become more useful by becoming more source-aware, not by becoming more confident.

The operator should receive better evidence, better links, better questions, and better validation prompts.

