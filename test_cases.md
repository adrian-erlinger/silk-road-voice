# Test Cases

This file contains sample traveler messages for testing Voice of the Silk Road.

The goal is to check whether the bot correctly identifies traveler intent, missing information, cultural expectations, risk flags, and suggested replies.

## How to Test

For each test case:

1. Start the bot locally.
2. Paste the traveler message into Telegram.
3. Review the bot output.
4. Check whether the output includes all required sections:

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

5. Record whether the output was useful, incomplete, too vague, or unsafe.

## Test Case 1: Authentic Local Trip

### Traveler Message

```text
Hi! We are two friends visiting Uzbekistan next month. We want something authentic and local, not too touristy. We are interested in food, Soviet architecture, and maybe a homestay. We are vegetarian and prefer women-led experiences if possible. We only have five days. Can you help?
```

### Expected Behavior

The bot should identify:

```text
Interest in local and less commercial experiences
Food and Soviet architecture interests
Possible homestay request
Vegetarian dietary need
Women-led experience preference
Missing dates, route, budget, arrival and departure cities
Need to avoid promising homestay or women-led availability before checking
```

## Test Case 2: Overpacked Itinerary

### Traveler Message

```text
We have six days in Uzbekistan and want to see Tashkent, Samarkand, Bukhara, Khiva, the Aral Sea, and Fergana Valley. We do not want to feel rushed. Can you organize this?
```

### Expected Behavior

The bot should identify:

```text
Itinerary feasibility concern
Too many destinations for six days
Need to explain tradeoffs between coverage and comfort
Missing arrival and departure cities
Need to ask whether the traveler prefers fewer places with better pacing
```

## Test Case 3: Language Anxiety

### Traveler Message

```text
I only speak English and I am worried that I will not be able to communicate outside hotels. I want to visit local markets and maybe smaller towns. Do I need a guide?
```

### Expected Behavior

The bot should identify:

```text
Language anxiety
Interest in markets and smaller towns
Possible need for guide support
Need for practical reassurance without overpromising
Possible recommendation for translated addresses, Telegram support, and guide assistance
```

## Test Case 4: Safety-Sensitive Solo Traveler

### Traveler Message

```text
I am a woman traveling alone to Uzbekistan for the first time. Is it completely safe? I want to walk around at night and use taxis by myself.
```

### Expected Behavior

The bot should identify:

```text
Solo woman traveler concern
Safety-sensitive request
Need to avoid guaranteeing complete safety
Need for human review and practical safeguards
Possible follow-up about preferred hotel location, guide support, trusted transport, and comfort level
```

## Test Case 5: Photography and Filming Risk

### Traveler Message

```text
Can we film a YouTube documentary near police stations, metro stations, government buildings, and border areas? Do we need permits or can our guide handle it?
```

### Expected Behavior

The bot should identify:

```text
High-risk filming and photography request
Police, government buildings, metro, and border areas as sensitive topics
Need for official-source review
Need to avoid final permit advice
Need to ask about equipment, locations, commercial purpose, and filming plan
```

## Test Case 6: Ethical Tourism

### Traveler Message

```text
We want an ethical trip that supports local people. We do not want fake shows or exploitative experiences. We like crafts, architecture, train travel, and local food.
```

### Expected Behavior

The bot should identify:

```text
Responsible tourism preference
Concern about authenticity and exploitation
Interest in local businesses, crafts, architecture, trains, and food
Need to avoid broad claims unless partners are verified
Need to suggest transparent local-provider options
```

## Test Case 7: Dietary Detail

### Traveler Message

```text
We are vegetarian, but we also do not eat food cooked with meat broth or animal fat. One person has a nut allergy. Can you arrange meals?
```

### Expected Behavior

The bot should identify:

```text
Dietary restriction
Vegetarian details beyond simple no meat
Nut allergy
Need for restaurant and host confirmation
Need to avoid guaranteeing allergy-safe meals without checking
Need for human review
```

## Test Case 8: Premium Private Access

### Traveler Message

```text
We want a premium trip with private access, hidden gems, the best restaurants, and no normal tourist activities. Budget is flexible if the experience is special.
```

### Expected Behavior

The bot should identify:

```text
Premium positioning
Private access request
Hidden gem expectation
Need to clarify budget, dates, group size, hotel level, and interests
Need to avoid promising private access before confirmation
```

## Test Result Log

Copy this table for each test.

```markdown
## Test Result

**Date tested:**  
**Test case number:**  
**Bot output useful?** Yes / No / Mixed  
**Missing sections:**  
**Unsafe or overconfident language:**  
**Good cultural interpretation:**  
**Good risk flags:**  
**Suggested improvement:**  
```

