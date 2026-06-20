# Source Policy

This file defines how Voice of the Silk Road should use different sources of information.

The project is designed to help Uzbek tour operators understand multilingual traveler requests, interpret cultural expectations, flag sensitive issues, and prepare Telegram-ready responses.

Because tourism involves real people, travel logistics, money, safety, culture, and official rules, the system must treat different sources differently.

## Source Hierarchy

### 1. Official Sources

Official sources should be used for rules, regulations, legal requirements, permits, safety requirements, visa issues, customs issues, registration rules, and government guidance.

Examples of official source categories:

```text
Ministry of Foreign Affairs
Official e-visa portal
Customs authorities
Tourism authorities
Internal affairs or registration authorities
Transport authorities
Protected site or museum authorities
Local site management
Embassy or consular guidance when relevant
```

Official sources should be treated as the highest authority for official rules.

The system should not invent or guess official guidance.

If current official guidance is needed, the system should flag the issue for human review and tell the operator to check the relevant official source before responding.

### 2. Tour Operator Human Review

Tour operator staff should make final decisions on operational feasibility.

Examples:

```text
Availability of guides
Availability of women-led experiences
Homestay suitability
Restaurant readiness
Vegetarian or allergy handling
Hotel comfort level
Transport feasibility
Route timing
Pricing
Partner quality
Traveler fit
```

The system can assist with summaries, drafts, risk flags, and preparation notes.

The system should not make final commitments to travelers.

### 3. Community Sources

Community sources can be used to understand traveler concerns, local perspectives, recurring questions, expectation gaps, and cultural interpretation issues.

Examples:

```text
r/Uzbekistan travel discussions
Public travel forums
Public traveler trip reports
Public Q&A threads
Local commentary on tourism issues
```

Community sources may inform:

```text
Sample scenarios
Cultural intent glossary entries
Traveler concern categories
Response templates
Risk flag examples
Pilot learning questions
```

Community sources should not be treated as official guidance.

Community sources should not be used to make claims about legal rules, visa rules, customs rules, safety guarantees, permits, restricted areas, medical issues, or official procedures.

### 4. Model Inference

The AI model can help interpret traveler intent, organize information, draft replies, and identify possible risks.

Model output should be treated as a draft.

The model should not be treated as an authority on official rules, safety, legal issues, medical issues, or final operational decisions.

## Use of Reddit and Public Forums

Public Reddit threads and similar forums can provide useful qualitative insight into:

```text
What travelers worry about before visiting Uzbekistan
What local residents say about common traveler misunderstandings
What questions foreign visitors repeat
Where travelers report confusion, anxiety, or unmet expectations
What language and cultural gaps appear in real travel planning
```

The project may use Reddit and other public forums as a research input, but only through human-reviewed summaries.

The project should not:

```text
Scrape Reddit automatically in version 1
Store usernames
Store large amounts of comment text
Copy full comments into the repository
Treat anonymous comments as verified facts
Use Reddit as an official source
Generate safety, legal, visa, customs, or permit guidance from Reddit comments
```

The project may:

```text
Review public threads manually
Summarize recurring themes in original language
Record source URLs for research traceability
Convert themes into glossary entries, scenarios, or response templates
Flag common traveler concerns for human review
```

## Privacy and Attribution Rules

When using community sources:

```text
Do not include usernames
Do not include private messages
Do not include personal contact information
Do not quote long comments
Do not copy sensitive personal stories into the product
Do not present one comment as a general fact
```

When a thread informs product design, record only:

```text
Source URL
Date reviewed
Thread topic
Traveler concern
Local or operator insight
Product implication
Confidence level
Related file to update
```

## Official-Rule Boundary

The system must flag, not answer, requests involving:

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

For these issues, the system should recommend human review and official-source checking.

## Human-in-the-Loop Rule

The system should keep human operators in control.

The system can:

```text
Summarize traveler messages
Identify missing information
Interpret cultural expectations
Draft Telegram replies
Flag risks
Suggest follow-up questions
Prepare internal notes
```

The system should not:

```text
Send final replies automatically
Promise availability
Confirm bookings
Set prices
Guarantee safety
Provide legal advice
Provide visa advice
Provide customs advice
Provide medical advice
Approve restricted activities
```

## Source Use by File

### README.md

May describe the source policy at a high level.

### cultural_intent_glossary.md

May use community sources to identify recurring traveler phrases and expectation gaps.

### sample_scenarios.md

May include fictionalized scenarios inspired by recurring public travel questions.

### traveler_request_intake_template.md

May include fields that capture common community-reported concerns, such as safety anxiety, scam concerns, language anxiety, and itinerary feasibility.

### risk_and_escalation_register.md

Should distinguish between official-rule risks, community-reported concerns, service-quality concerns, and cultural-expectation gaps.

### telegram_response_templates.md

May include response templates for recurring traveler questions found in public forums.

### pilot_success_metrics.md

May track whether the pilot improves handling of common traveler concerns.

### community_insight_log.md

Should record human-reviewed themes from community sources without storing usernames or long comments.

## Product Principle

The project should use community knowledge to understand people better, not to replace official sources or human judgment.


## Place Discovery Sources

Place discovery sources are used for local recommendation requests.

Examples include:

```text id="df660v"
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
Local experience locations
Hotels or lodging areas
Attractions
Landmarks
Specific dishes in specific cities
```

Place discovery sources may include:

```text id="o3zfyw"
Google Places API
Google Maps links
Yandex Maps or business search in a future version
Operator-vetted local lists
Local guide validation
```

Place discovery sources can help the operator identify candidate places, but they should not replace human review.

## Place Recommendation Rule

The bot should not invent place recommendations from model memory.

If the traveler asks for a place recommendation, the bot should use a source-backed lookup when available.

A source-backed place candidate should include:

```text id="4mcfi0"
Place name
Address
Clickable map link
Rating if available
Review count if available
Opening status if available
Website or phone if available
Reason it may match the traveler request
Operator validation reminder
```

The bot may explain why a place may match the traveler’s request, but the bot should not claim the place is verified unless it was returned by a source and reviewed by a human operator.

## Operator Validation for Place Recommendations

Before sending a place recommendation to a traveler, the operator should verify:

```text id="91zuvu"
Current opening hours
Recent reviews
Location suitability
Food quality
Whether the place actually offers the requested dish or experience
Dietary fit
Accessibility
Group-size suitability
Traveler comfort level
Local guide confidence
```

The bot should return candidate places for operator review.

The bot should not automatically send place recommendations to travelers.

## Maps API Boundary

Maps or Places APIs should be used for place discovery.

They should not be used as the authority for official rules.

Examples of questions that require official-source review instead of Maps authority:

```text id="8ci9gx"
Can I take photos in the Tashkent metro?
Do I need a permit to film?
Can I fly a drone?
Can I enter a restricted area?
What are the visa rules?
What are the customs rules?
Do I need registration?
```

For mixed requests, the bot should separate the place-discovery component from the official-rule component.

Example:

```text id="ee0e1j"
Can I film Soviet architecture and metro stations in Tashkent?
```

The bot may identify relevant places, but filming and photography rules must still be flagged for human review and official-source checking.

## No Hallucinated Places Rule

If no place lookup is available, or if the Maps API returns no usable result, the bot should say so.

The bot may provide search queries for operator follow-up.

The bot should not invent restaurant names, shop names, attraction names, or local recommendations.

