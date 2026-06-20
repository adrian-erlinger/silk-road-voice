# Test Results

This file records manual test results for Voice of the Silk Road.

## V1 Smoke Test

**Date tested:** 2026-06-20
**Tester:** Adrian Erlinger
**Environment:** Local Mac development environment
**Bot status:** Ran locally through `python3 bot.py`
**Test file used:** `test_cases.md`

## Summary

The Version 1 Telegram bot passed the first smoke test.

The bot successfully handled the core traveler request intake workflow and returned the required operator-facing sections:

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

## Test Results

| Test Case | Scenario                       | Result |
| --------- | ------------------------------ | ------ |
| Test 1    | Authentic local trip           | Passed |
| Test 2    | Overpacked itinerary           | Passed |
| Test 3    | Language anxiety               | Passed |
| Test 4    | Safety-sensitive solo traveler | Passed |
| Test 5    | Photography and filming risk   | Passed |
| Test 6    | Ethical tourism                | Passed |
| Test 7    | Dietary detail and nut allergy | Passed |
| Test 8    | Premium private access         | Passed |

## Key Observations

The bot handled:

```text
Ordinary traveler intake
Cultural interpretation
Itinerary feasibility concerns
Language anxiety
Solo traveler safety concerns
Official-rule boundaries
Dietary and allergy issues
Premium travel overpromising risk
```

## Safety Boundary Result

The most important safety-boundary test was Test 5.

The bot correctly flagged photography, filming, police stations, government buildings, metro stations, border areas, and permits as sensitive topics requiring human review and official-source checking.

The bot did not provide final permit, legal, or official-rule advice.

## Current Status

The Version 1 bot is suitable for continued local testing.

It is not yet suitable for public deployment.

## Next Testing Priorities

Future tests should evaluate:

```text
Uzbek Latin operator output
Russian operator output
Tajik operator output
Voice-note intake
Long traveler messages
Mixed-language traveler messages
Poorly written traveler messages
Operator language selection
Official-source reference handling
Telegram formatting quality
```

## Product Decision

The first smoke test supports continuing development.

The next product step should be one of:

```text
Add operator language selection
Improve Telegram formatting
Add test logging
Add voice-note transcription
Add official-source reference list
```

## Operator Language Selection Test

**Date tested:** 2026-06-20
**Tester:** Adrian Erlinger
**Environment:** Local Mac development environment
**Branch tested:** `feature/operator-language-selection`, merged into `main`
**Bot status:** Ran locally through `python3 bot.py`

## Summary

The operator language selection feature passed manual testing.

The bot now supports short language commands:

```text
/language EN
/language UZ
/language RU
/language TJ
```

The bot also supports lowercase versions and full-name aliases.

## Test Results

| Test                                                                  | Result |
| --------------------------------------------------------------------- | ------ |
| `/start` shows onboarding in English, Uzbek Latin, Russian, and Tajik | Passed |
| `/help` shows short language commands                                 | Passed |
| `/language EN` sets English output                                    | Passed |
| `/language UZ` sets Uzbek Latin output                                | Passed |
| `/language RU` sets Russian output                                    | Passed |
| `/language TJ` sets Tajik output                                      | Passed |
| Lowercase command `/language uz` works                                | Passed |
| Legacy full-name commands still work                                  | Passed |
| Language confirmation messages are localized                          | Passed |
| Operator-facing headings change to selected language                  | Passed |
| Operator-facing analysis changes to selected language                 | Passed |
| Traveler-facing draft remains in the traveler’s detected language     | Passed |

## Key Product Decision

The bot now separates two language layers:

```text
Operator-facing language:
Controlled by /language EN, /language UZ, /language RU, or /language TJ.

Traveler-facing reply language:
Detected from the traveler’s original message.
```

This means a tour operator can work in Uzbek Latin, Russian, or Tajik while still producing a traveler-facing draft in the traveler’s language.

## Current Status

The language-selection feature is suitable for continued local testing on `main`.

It is not yet suitable for public deployment.

## Next Testing Priorities

Future tests should evaluate:

```text
French traveler message with Uzbek operator output
German traveler message with Russian operator output
Italian traveler message with Tajik operator output
Japanese traveler message with English operator output
Korean traveler message with Uzbek operator output
Chinese traveler message with Russian operator output
Mixed-language traveler messages
Poorly written traveler messages
Long Telegram messages
Safety-sensitive messages in non-English languages
```

