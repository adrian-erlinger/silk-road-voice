# Traveler Request Intake Template

This file defines the intake structure for traveler requests sent to Uzbek tour operators through Telegram or similar messaging channels.

The purpose is to convert a messy traveler message into clear operational information that local staff can review, translate, clarify, and act on.

## Intake Goal

For every traveler request, the system should identify:

* What the traveler wants
* What information is already known
* What information is missing
* Which cultural expectations need interpretation
* Which risks or compliance issues require human review
* What the operator should ask next
* What internal preparation may be needed

## Source Message

The system should accept traveler messages in text form first.

Later versions may support:

* Telegram voice notes
* Uploaded screenshots
* Itinerary documents
* Emails pasted into Telegram
* Mixed-language messages

## Traveler-Side Languages

The intake workflow is designed for messages in:

* English
* French
* German
* Italian
* Japanese
* Korean
* Chinese

Additional languages may be added later.

## Operator-Side Output Languages

The operator summary should eventually support:

* Uzbek, Latin script
* Russian
* Tajik

English may also be used as an internal bridge language when needed.

## Intake Fields

### 1. Traveler Profile

Extract or mark as missing:

```text
Traveler name:
Country or region:
Primary language:
Number of travelers:
Age range or traveler type:
Family, couple, friends, solo traveler, group, business traveler, student, other:
```

### 2. Trip Timing

Extract or mark as missing:

```text
Arrival date:
Departure date:
Trip length:
Season or month:
Flexibility:
Urgency of response:
```

### 3. Route and Cities

Extract or mark as missing:

```text
Arrival city:
Departure city:
Cities requested:
Regions requested:
Transport preferences:
Domestic flight, train, car, walking, other:
```

Common Uzbekistan destinations may include:

* Tashkent
* Samarkand
* Bukhara
* Khiva
* Fergana Valley
* Nukus
* Aral Sea region
* Termez
* Chimgan / Charvak
* Desert camps
* Rural villages
* Border or restricted areas requiring review

### 4. Experience Interests

Extract stated interests and infer likely categories.

Possible categories:

```text
Architecture:
History:
Food:
Crafts:
Markets:
Religious heritage:
Soviet architecture:
Silk Road heritage:
Jewish heritage:
Islamic heritage:
Nature:
Desert:
Mountains:
Photography:
Shopping:
Family travel:
Luxury:
Adventure:
Community-based tourism:
Women-led experiences:
Homestay:
Train travel:
Nightlife:
Wellness:
Other:
```

### 5. Cultural Intent Phrases

Identify culturally loaded terms that require interpretation.

Examples:

```text
Authentic:
Local:
Not touristy:
Hidden gem:
Ethical:
Responsible:
Immersive:
Off the beaten path:
Safe for solo women:
Women-led:
Premium:
Private access:
Photography-friendly:
Spiritual:
Nomadic:
```

For each phrase, the system should explain what the traveler likely means and what the operator should clarify.

### 6. Practical Constraints

Extract or mark as missing:

```text
Budget range:
Hotel level:
Comfort expectations:
Private or group tour:
Guide language:
Dietary restrictions:
Mobility limitations:
Health considerations:
Children or older travelers:
Accessibility needs:
Religious or cultural needs:
Photography or filming needs:
```

### 7. Dietary and Food Requirements

Extract or mark as missing:

```text
Vegetarian:
Vegan:
Halal:
No pork:
No alcohol:
No spicy food:
Allergies:
Gluten-free:
Dairy-free:
Fish or seafood restrictions:
Meat broth or animal fat restrictions:
Cross-contamination concern:
```

The system should flag dietary requirements for human confirmation before restaurants, hosts, or cooking activities are booked.

### 8. Safety, Rules, and Compliance Review

Flag requests that may require human review and official-source checking.

Potential flags:

```text
Visa questions:
Customs questions:
Registration questions:
Border areas:
Restricted zones:
Photography of official buildings:
Photography of police or military:
Photography of infrastructure:
Religious site behavior:
Drone use:
Commercial filming:
Medical questions:
Political questions:
Safety guarantees:
Travel with children:
Solo women traveler safety:
Animal activities:
High-risk outdoor activity:
```

The system should not provide final legal, visa, customs, safety, medical, or official regulatory advice. It should flag the issue and recommend checking official sources.

### 9. Missing Information

The system should create a short list of missing information needed before the operator can prepare a proposal.

Common missing items:

```text
Exact dates:
Number of travelers:
Arrival and departure cities:
Budget range:
Hotel category:
Preferred guide language:
Dietary restrictions:
Mobility needs:
Private or group preference:
Comfort level:
Must-see places:
Activities to avoid:
```

### 10. Suggested Follow-Up Questions

The system should produce 3 to 7 practical questions for the operator to ask the traveler.

Questions should be polite, short, and suitable for Telegram.

Example:

```text
Could you please send your exact travel dates?
How many travelers will be in your group?
What hotel level do you prefer?
Do you prefer a private tour or a small group?
Do you have any dietary restrictions we should know about?
Would you like the guide to speak English, Russian, or another language?
```

### 11. Internal Preparation Notes

The system should provide private notes for the operator.

These notes should help staff prepare before responding or confirming.

Examples:

```text
Check vegetarian-friendly restaurants before proposing food activities.
Confirm whether a women guide is available for the requested dates.
Do not promise a homestay until host availability and comfort level are checked.
If the traveler asks about photography near official sites, flag for official-source review.
Prepare a short route option with Tashkent, Samarkand, and Bukhara if the traveler has limited time.
```

## Intake Output Standard

The intake should be converted into the standard operator output format:

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

## Intake Principles

The system should:

* Preserve meaning rather than translate literally
* Mark missing information clearly
* Separate facts from assumptions
* Interpret cultural intent cautiously
* Avoid overpromising
* Keep human staff in control
* Format replies for Telegram use
* Support fast review by operators under time pressure

## Source Need

This section identifies whether the traveler request needs source-backed information.

The bot should classify the request into one or more source-need categories.

## Source Need Categories

```text
No source needed
Official source needed
Place recommendation source needed
Community insight useful
Operator validation needed
```

## When No Source Is Needed

Use this when the traveler request can be handled through normal intake and clarification.

Examples:

```text
We want a five-day cultural trip.
We are interested in food and architecture.
We prefer a private guide.
We are vegetarian.
```

## When an Official Source Is Needed

Use this when the traveler asks about rules, permissions, safety, legal issues, medical issues, or government requirements.

Examples:

```text
Can I take photos in the Tashkent metro?
Do I need a filming permit?
Can I fly a drone?
Do I need a visa?
Do I need registration?
Can I bring medicine through customs?
Can I visit a border area?
```

The bot should not provide final guidance from memory.

The bot should flag official-source review and human operator review.

## When a Place Recommendation Source Is Needed

Use this when the traveler asks for a specific place, local recommendation, food stop, shop, market, café, restaurant, museum, workshop, or attraction.

Examples:

```text
Where can I find Bukhara-style somsa in Tashkent?
Can you recommend a vegetarian restaurant in Samarkand?
Where can I buy Rishtan ceramics?
Is there a good tea house near Registan?
Where can I find a local bakery in Bukhara?
```

The bot should use a source-backed lookup when available.

Future versions should call a Maps or Places API and return candidate links for operator review.

## When Community Insight Is Useful

Use this when the traveler expresses anxiety, uncertainty, or expectation gaps that are common in travel forums or public discussions.

Examples:

```text
Is Uzbekistan safe for a first-time traveler?
Will I be able to get around with only English?
How do I avoid scams?
Is this itinerary too rushed?
Can I meet locals without being intrusive?
```

Community insight should inform cultural interpretation and response framing.

Community insight should not replace official sources or human review.

## When Operator Validation Is Needed

Use this when the traveler asks for something that depends on local availability, partner quality, pricing, routing, staffing, or real-time feasibility.

Examples:

```text
Can you arrange women-led experiences?
Can you find a real homestay?
Can we meet local artisans?
Can we get private access?
Can you arrange meals for a severe allergy?
Can you confirm a guide who speaks Korean?
```

The bot should tell the operator what must be checked before promising anything to the traveler.

## Source Need Output

The bot should include source need analysis in the operator-facing output.

Recommended structure:

```text
Source need:
- Place recommendation source needed
- Operator validation needed

Why:
The traveler asks for a specific local food experience in a specific city. Candidate places should come from a source-backed lookup and then be reviewed by local staff.

Suggested lookup:
Bukhara somsa Tashkent

Operator validation:
Check current opening hours, recent reviews, location suitability, and whether the place actually serves the requested dish.
```

## Product Principle

Source need classification should make the bot more useful and less generic.

The bot should not merely repeat the traveler’s words.

It should identify what the operator needs to verify, where the information should come from, and what can safely be drafted for the traveler.

