# Operator Output Format

This file defines the standard output that Voice of the Silk Road should generate from a traveler request.

The goal is to help Uzbek tour operator staff quickly understand what the traveler wants, what information is missing, what cultural expectations may need interpretation, and what response should be sent back through Telegram.

## Standard Output

Each traveler request should be converted into the following structure:

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

## Field Definitions

### Traveler intent

A short explanation of what the traveler appears to want.

This should capture the real request behind the message, not only the literal words.

Example:

```text
The traveler wants a short, curated cultural trip that feels local and less commercial than a standard sightseeing package.
```

### Trip summary

A concise operational summary for the tour company.

Example:

```text
Two travelers want a five-day Uzbekistan itinerary next month focused on food, Soviet architecture, local experiences, and possibly a homestay.
```

### Key details

Important facts already provided by the traveler.

Examples:

```text
- Number of travelers: 2
- Travel dates: next month, exact dates not provided
- Trip length: 5 days
- Interests: food, Soviet architecture, homestay, local experiences
- Dietary needs: vegetarian
- Preference: women-led experiences if available
```

### Missing information

Questions the operator should ask before confirming the trip.

Examples:

```text
- Exact travel dates
- Arrival and departure cities
- Budget range
- Preferred comfort level
- Dietary restrictions beyond vegetarian
- Mobility or health limitations
- Whether the travelers want private or group arrangements
```

### Cultural interpretation

Explanation of traveler expectations that may not translate directly.

This section should help local staff understand phrases such as “authentic,” “local,” “not touristy,” “hidden gem,” “ethical,” “immersive,” “safe,” or “off the beaten path.”

Example:

```text
“Authentic and local” likely means the traveler wants smaller-scale experiences, direct interaction with local people, and fewer large-group tourist stops. It does not mean the operator should avoid major sites, but the itinerary should include personal, community-based, or locally guided elements.
```

### Risk or compliance flags

Issues that require human review before responding or confirming.

This section should be cautious. It should not make legal, visa, safety, customs, or medical determinations automatically.

Examples:

```text
- Homestay availability should be checked carefully.
- Vegetarian meals should be confirmed with hosts and restaurants in advance.
- Any request involving restricted areas, border zones, photography rules, protected sites, or official permits should be reviewed against official Uzbekistan rules.
- Safety, visa, customs, registration, or medical questions should be handled by a human and checked against official sources.
```

### Suggested operator reply

A Telegram-ready message the operator can send to the traveler.

The reply should be clear, polite, and practical. It should confirm understanding, ask for missing information, and avoid overpromising.

Example:

```text
Thank you for your message. We can help design a five-day Uzbekistan trip with food, architecture, and local cultural experiences. To prepare the best proposal, could you please send your exact travel dates, arrival and departure cities, budget range, and whether you prefer private guiding or a small group? We will also check vegetarian meal options and whether women-led experiences are available for your dates.
```

### Internal preparation notes

Private notes for the tour company.

These should not be sent directly to the traveler.

Example:

```text
Check availability of women guides or women-led workshops. Confirm vegetarian-friendly restaurants in each city. Consider Tashkent for Soviet architecture, Samarkand or Bukhara for cultural sites, and one carefully vetted local meal or craft experience. Avoid promising a homestay until host availability and standards are confirmed.
```

## Output Principles

The system should:

* Preserve traveler meaning, not only translate words
* Separate confirmed details from assumptions
* Identify missing information before suggesting a booking
* Explain culturally loaded traveler expectations
* Keep human staff in control of final responses
* Flag sensitive or regulated issues for review
* Produce Telegram-ready replies that are polite and practical
* Support Uzbek Latin, Russian, and Tajik operator workflows

## Human Review Rule

The system should never automatically approve travel arrangements, legal guidance, safety claims, visa advice, customs guidance, medical advice, or regulated activities.

When uncertain, the system should flag the issue for human review and recommend checking official sources.
