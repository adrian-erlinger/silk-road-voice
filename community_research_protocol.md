# Community Research Protocol

This file defines how Voice of the Silk Road should use public community sources such as r/Uzbekistan, travel forums, and public trip reports.

The goal is to learn from real traveler questions and local commentary without treating informal community discussion as official guidance.

## Purpose

Community sources can help the project understand:

```text
Traveler anxieties
Common misunderstandings
Language barriers
Cultural expectation gaps
Recurring itinerary questions
Concerns about safety, scams, payment, transport, food, and local etiquette
Local perspectives on what travelers often misunderstand
```

This information can improve:

```text
Cultural intent glossary
Sample scenarios
Traveler request intake fields
Risk and escalation categories
Telegram response templates
Pilot success metrics
```

## What Counts as a Community Source

Examples:

```text
r/Uzbekistan public threads
Public travel forums
Public traveler Q&A threads
Public trip reports
Public blog comments
Public social media discussions where review is allowed
```

Do not use:

```text
Private messages
Closed groups
Paid databases
Personal contact information
Screenshots of private conversations
Sensitive personal stories without strong anonymization
```

## Research Method

Use a human-reviewed process.

### Step 1: Identify a thread or public discussion

Look for public discussions related to Uzbekistan travel, such as:

```text
First-time travel questions
Solo traveler questions
Women traveler safety questions
Language barrier questions
Scam or overcharging concerns
Itinerary feasibility questions
Food and dietary questions
Photography or filming questions
Visa, customs, registration, or official-rule questions
Cultural etiquette questions
Local recommendations
Tour agency trust questions
```

### Step 2: Read for patterns

Do not copy comments into the product.

Instead, identify recurring themes.

Examples:

```text
Travelers often ask whether English is enough outside major cities.
Travelers worry about being overcharged by taxis or agencies.
Travelers ask whether a seven-day itinerary is too rushed.
Travelers use words like “authentic” without knowing what kind of experience they actually want.
Local commenters often distinguish between major tourist cities and rural areas.
```

### Step 3: Summarize in original words

Write a short, human-authored summary.

Do not copy long comments.

Do not include usernames.

Do not present one comment as a general fact.

### Step 4: Assign the insight to a product file

Each insight should be connected to at least one file.

Examples:

```text
cultural_intent_glossary.md
sample_scenarios.md
traveler_request_intake_template.md
risk_and_escalation_register.md
telegram_response_templates.md
pilot_success_metrics.md
```

### Step 5: Set confidence level

Use one of three confidence levels:

```text
Low: One comment or one thread only.
Medium: Repeated in more than one discussion or supported by local/operator experience.
High: Recurring pattern across several discussions and consistent with operator experience.
```

Community sources should normally remain Low or Medium unless supported by additional evidence.

## What to Record

Use `community_insight_log.md` to record:

```text
Source URL:
Date reviewed:
Thread topic:
Traveler concern:
Local or operator insight:
Product implication:
Related file to update:
Confidence level:
Notes:
```

## What Not to Record

Do not record:

```text
Usernames
Personal contact information
Full comment text
Private messages
Sensitive personal details
Political accusations
Unverified claims as facts
Long copied passages
```

## Use of Reddit

Reddit can be used as a qualitative research source, especially r/Uzbekistan public travel discussions.

Allowed uses:

```text
Manual review of public threads
Theme extraction
Anonymized summaries
Recurring traveler concern mapping
Fictionalized scenario design
Response-template improvement
Glossary expansion
```

Not allowed in version 1:

```text
Automatic Reddit scraping
Bulk comment storage
Username storage
Long quote storage
Bot answers based directly on Reddit comments
Treating Reddit as an official source
Using Reddit to answer legal, visa, customs, medical, safety, or permit questions
```

## Official-Source Boundary

Community sources may reveal that travelers ask about official issues.

Examples:

```text
Visa rules
Customs rules
Registration
Photography restrictions
Drone use
Border areas
Restricted zones
Commercial filming
Medical issues
Safety guarantees
```

When these topics appear, the product should flag the issue for official-source review.

Community comments should not be used to answer official-rule questions.

## Scenario Design Rules

When community research inspires a sample scenario:

```text
Make the scenario fictional.
Do not copy a real comment.
Do not include usernames.
Do not include personal details from a real person.
Combine patterns from multiple sources where possible.
Focus on the operator problem.
```

Example transformation:

Community pattern:

```text
Travelers ask whether English is enough and whether they can travel independently outside major cities.
```

Fictionalized scenario:

```text
A traveler asks whether they can visit Tashkent, Samarkand, Bukhara, and Fergana without Russian or Uzbek, and whether they need a guide for rural areas.
```

## Template Design Rules

When community research informs Telegram templates:

```text
Address the traveler concern directly.
Use practical language.
Avoid over-reassurance.
Avoid guarantees.
Ask clarifying questions.
Offer human follow-up where needed.
```

Example concern:

```text
Is Uzbekistan safe for a solo woman traveler?
```

Better operator response pattern:

```text
We can help plan the trip with reliable transport, central hotels, trusted guides, and clear support contacts. We cannot guarantee that any trip is completely risk-free, but we can design the route around practical safeguards. Would you prefer a woman guide where available?
```

## Quality Checks

Before adding an insight from a community source, check:

```text
Is this a recurring pattern or only one opinion?
Could this be harmful if treated as fact?
Does this belong in cultural interpretation, risk flagging, or official-source review?
Is the wording anonymized?
Is the product implication clear?
Is this useful for a tour operator?
```

## Product Principle

Community research should make the product more human, more realistic, and more useful for operators.

It should not replace official sources, professional judgment, or human review.
