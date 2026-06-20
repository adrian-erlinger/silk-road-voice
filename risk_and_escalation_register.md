# Risk and Escalation Register

This file defines the risk and escalation logic for Voice of the Silk Road.

The goal is to help Uzbek tour operators identify traveler requests that require human review, official-source checking, or careful wording before a response is sent through Telegram.

The system should support staff judgment. It should not make final decisions on legal, visa, customs, safety, medical, political, or regulated travel matters.

## Core Rule

When a traveler request touches official rules, safety, permissions, health, legality, restricted locations, or sensitive cultural issues, the system should flag the issue for human review.

The system should not provide final authoritative guidance unless a human operator has checked the relevant official source.

## Risk Levels

### Low Risk

The request can usually be handled by standard operator review.

Examples:

```text
General sightseeing questions
Basic itinerary preferences
Hotel comfort level
Food interests without allergies
General cultural interests
Normal route planning
```

### Medium Risk

The request needs careful clarification before confirming.

Examples:

```text
Dietary restrictions
Mobility limitations
Older travelers
Solo women travelers
Homestays
Rural visits
Desert camps
Night travel
Photography in public places
Unclear budget or comfort expectations
```

### High Risk

The request requires human review before the operator replies with any firm commitment.

Examples:

```text
Visa questions
Customs questions
Registration questions
Drone use
Commercial filming
Photography of official sites
Photography of police, military, border, or infrastructure areas
Travel near border zones or restricted areas
Medical questions
Safety guarantees
Political questions
Religious sensitivity
Requests involving permits or official approval
```

### Stop / Escalate

The system should recommend immediate human escalation.

Examples:

```text
Traveler reports illness, injury, arrest, harassment, theft, lost passport, missing person, or emergency
Traveler asks how to avoid official rules
Traveler requests illegal, unsafe, exploitative, or deceptive arrangements
Traveler asks for guaranteed access to restricted areas
Traveler requests advice that could affect legal status or personal safety
```

## Risk Register

| Risk area                  | Trigger examples                                                                  |     Risk level | System action                                                                     | Human review needed? |
| -------------------------- | --------------------------------------------------------------------------------- | -------------: | --------------------------------------------------------------------------------- | -------------------- |
| Visa                       | “Do I need a visa?”, “Can I enter with my passport?”, “Can I extend my stay?”     |           High | Flag for official-source review                                                   | Yes                  |
| Customs                    | “Can I bring medicine?”, “Can I bring drone equipment?”, “Can I export antiques?” |           High | Flag for official-source review                                                   | Yes                  |
| Registration               | “Do hotels register me?”, “Do I need to register after arrival?”                  |           High | Flag for official-source review                                                   | Yes                  |
| Border or restricted areas | “Can we visit border areas?”, “Can we film near the border?”                      |           High | Flag for official-source review                                                   | Yes                  |
| Photography and filming    | “Can we photograph police, metro, religious sites, markets, border areas?”        | Medium to High | Ask for details and flag sensitive locations                                      | Yes                  |
| Drone use                  | “Can I fly a drone?”                                                              |           High | Flag for official-source review                                                   | Yes                  |
| Religious sites            | “Can I film inside mosques?”, “Can we visit during prayer?”                       | Medium to High | Recommend etiquette review and site-specific confirmation                         | Yes                  |
| Medical needs              | “Can you advise on medication?”, “What should I do if I get sick?”                |           High | Do not give medical advice; refer to human support and official/emergency sources | Yes                  |
| Safety guarantees          | “Is it completely safe?”, “Can you guarantee no harassment?”                      |           High | Avoid guarantees; provide practical precautions                                   | Yes                  |
| Solo women travelers       | “Is this safe for solo women?”, “Can I travel alone at night?”                    | Medium to High | Provide practical safeguards and offer human follow-up                            | Yes                  |
| Older travelers            | “My father cannot walk much,” “We need easy walking”                              |         Medium | Flag accessibility needs and confirm route suitability                            | Yes                  |
| Dietary restrictions       | “Vegetarian,” “vegan,” “allergy,” “halal,” “gluten-free”                          |         Medium | Clarify restrictions and brief restaurants or hosts                               | Yes                  |
| Homestays                  | “Can we stay with a family?”                                                      |         Medium | Confirm comfort, registration, privacy, and host readiness                        | Yes                  |
| Animal activities          | “Can we ride animals?”, “Can we visit animal shows?”                              |         Medium | Clarify welfare expectations and available options                                | Yes                  |
| Political history          | “Can we discuss Soviet politics?”, “Can we visit political sites?”                |         Medium | Recommend careful guide matching and context-aware interpretation                 | Yes                  |
| Nightlife                  | “Can you arrange nightlife?”                                                      |         Medium | Clarify expectations and safety considerations                                    | Yes                  |
| LGBTQ traveler concerns    | “Is it safe for LGBTQ travelers?”                                                 |           High | Avoid guarantees; provide cautious, human-reviewed guidance                       | Yes                  |
| Commercial media           | “We are filming a documentary,” “We have a YouTube channel”                       |           High | Flag permits, site rules, and commercial filming review                           | Yes                  |
| Private access             | “Can we get private access to sites?”                                             | Medium to High | Do not promise access before confirmation                                         | Yes                  |

## Official-Source Review Principle

The system should not invent or summarize official rules from memory.

For official matters, the operator should check current sources from the relevant Uzbekistan authority before responding. Potential source categories include:

```text
Ministry of Foreign Affairs
Official e-visa portal
Customs authorities
Tourism authorities
Internal affairs / registration authorities
Transport authorities
Protected site or museum authorities
Local site management
Embassy or consular guidance when relevant
```

The tool should eventually include a maintained source list, but the first version should only flag the issue and remind the operator to verify.

## Standard Risk Flag Language

When the system detects a sensitive issue, it should use plain language.

Example:

```text
Risk flag: This request may involve official rules or site-specific restrictions. A human operator should check current official sources before giving final advice.
```

Example:

```text
Risk flag: The traveler is asking about safety. The operator should avoid guarantees and provide practical precautions only after human review.
```

Example:

```text
Risk flag: The traveler mentioned photography or filming near sensitive locations. Confirm the exact sites, equipment, and purpose before responding.
```

## Escalation Output

When a request requires escalation, the system should include:

```text
Risk level:
Why this is flagged:
What official or human source should be checked:
What the operator can safely say now:
What should not be promised:
Suggested follow-up question:
```

## Safe Response Principles

The operator reply should:

* Avoid legal, visa, customs, medical, or safety guarantees
* Ask for missing information before giving advice
* Refer sensitive matters to human review
* Say when something must be checked
* Avoid promising private access, permits, site entry, or safety outcomes
* Keep the tone calm, professional, and practical

## Example: Photography Request

Traveler message:

```text
Can we take photos everywhere in Uzbekistan? We want to photograph markets, metro stations, religious places, police, and border areas. We are making a YouTube travel documentary.
```

System risk output:

```text
Risk level: High

Why this is flagged:
The traveler is asking about photography and filming in potentially sensitive locations, including police, border areas, religious sites, and infrastructure. The request may involve site-specific rules, official restrictions, or permit requirements.

What should be checked:
Current official rules, site-specific policies, and whether commercial filming or special equipment requires permission.

What the operator can safely say now:
We can help plan photography-friendly locations, but some places may have restrictions. Please send the exact sites, equipment, and filming purpose so we can review what may be possible.

What should not be promised:
Do not say that photography is allowed everywhere. Do not confirm filming near police, border areas, official buildings, infrastructure, or religious sites without review.

Suggested follow-up question:
Could you please share the exact cities and sites you want to film, whether this is for personal or commercial use, and what equipment you plan to bring?
```

## Example: Vegetarian Food Request

Traveler message:

```text
We are vegetarian and want local food experiences.
```

System risk output:

```text
Risk level: Medium

Why this is flagged:
Vegetarian expectations vary. Some dishes may use meat broth, animal fat, or shared preparation surfaces even when they do not contain visible meat.

What should be checked:
Whether the traveler eats eggs, dairy, fish, meat broth, or food cooked with animal fat.

What the operator can safely say now:
We can plan vegetarian-friendly meals, but we should confirm your exact dietary requirements first.

What should not be promised:
Do not promise that all traditional meals can be made vegetarian without checking with restaurants or hosts.

Suggested follow-up question:
Do you avoid meat broth, animal fat, fish, eggs, dairy, or cross-contamination?
```

## Example: Solo Woman Traveler Safety

Traveler message:

```text
I am a solo woman traveler. Is it safe for me to travel alone in Uzbekistan?
```

System risk output:

```text
Risk level: High

Why this is flagged:
The traveler is asking for a safety assessment. The operator should avoid guarantees and provide practical support options.

What should be checked:
Route, dates, accommodation location, transport plan, guide arrangements, night travel, and emergency contact process.

What the operator can safely say now:
We can help plan a route with reliable transport, central hotels, trusted guides, and clear support contacts.

What should not be promised:
Do not guarantee complete safety or say there is no risk.

Suggested follow-up question:
Would you prefer private transport, central hotels, and a woman guide where available?
```

## Human Review Rule

The system can assist with understanding, structuring, translating, and drafting.

A human operator must make final decisions on:

```text
Legal or official guidance
Safety-sensitive travel
Permits or restricted access
Medical issues
Emergency issues
High-value bookings
Unusual or sensitive traveler requests
```
