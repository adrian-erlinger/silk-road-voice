# Pilot Success Metrics

This file defines the first success metrics for Voice of the Silk Road.

The pilot is designed for Uzbek tour operators who need to respond faster, understand traveler expectations more clearly, and convert more inquiries into confirmed bookings.

## Pilot Goal

The goal of the pilot is to test whether AI-supported traveler request intake can improve Telegram-based communication between local tour operators and multilingual travelers.

The pilot should not be judged by technical complexity. It should be judged by whether it improves daily tour operations.

## Primary Success Metrics

### 1. Faster Response Time

**Question:**
Does the toolkit help staff respond to traveler inquiries more quickly?

**Why it matters:**
Travelers often contact multiple agencies at the same time. A faster, clearer reply can improve booking conversion.

**How to measure:**

```text
Average time from traveler inquiry to first useful operator reply
```

**Possible baseline:**

```text
Manual response time before pilot: 2 to 12 hours
```

**Pilot target:**

```text
First useful reply prepared within 15 minutes for standard inquiries
```

### 2. Fewer Misunderstood Requests

**Question:**
Does the toolkit reduce misunderstanding of traveler expectations?

**Why it matters:**
The core issue is not only translation. Travelers often use culturally loaded phrases such as “authentic,” “ethical,” “hidden gem,” “safe,” “premium,” or “not touristy.” Operators need to understand what the traveler likely means before designing the trip.

**How to measure:**

```text
Number of requests where staff had to rework the proposal because the traveler’s expectation was misunderstood
```

**Possible baseline:**

```text
Manual process often requires repeated clarification by senior English-speaking staff
```

**Pilot target:**

```text
Staff identify major missing information and cultural expectations before sending the first proposal
```

### 3. More Bookings Converted

**Question:**
Does the toolkit help operators convert more inquiries into confirmed bookings?

**Why it matters:**
Improved communication should support business growth, not only internal convenience.

**How to measure:**

```text
Inquiry-to-proposal rate
Proposal-to-booking rate
Number of inquiries lost because of slow or unclear response
```

**Pilot target:**

```text
Higher percentage of qualified traveler inquiries receive a clear proposal or next-step reply
```

## Secondary Metrics

### Staff Escalation Rate

**Question:**
Does the toolkit reduce bottlenecks on the strongest English-speaking staff?

**How to measure:**

```text
Number of traveler messages escalated to senior English-speaking staff
```

**Desired direction:**

```text
Fewer routine inquiries require escalation, while sensitive or complex inquiries are escalated more consistently.
```

### Missing Information Capture

**Question:**
Does the toolkit help staff ask better follow-up questions?

**How to measure:**

```text
Percentage of replies that ask for exact dates, number of travelers, arrival and departure cities, budget, hotel level, guide language, dietary needs, and mobility needs when missing.
```

**Desired direction:**

```text
More first replies include the right clarification questions.
```

### Risk Flag Accuracy

**Question:**
Does the toolkit correctly flag requests involving safety, official rules, permits, photography, filming, border areas, dietary restrictions, accessibility, or other sensitive issues?

**How to measure:**

```text
Number of high-risk requests flagged for human review
Number of sensitive requests missed
Number of false alarms that slowed normal operations
```

**Desired direction:**

```text
Sensitive issues are flagged early without overwhelming staff.
```

### Operator Satisfaction

**Question:**
Do local staff find the workflow useful?

**How to measure:**

```text
Short staff survey after each week of pilot use
```

Example questions:

```text
Did the toolkit help you understand traveler requests?
Did the suggested reply save time?
Did the cultural interpretation section help?
Were risk flags useful?
What should be changed?
```

### Traveler Satisfaction

**Question:**
Do travelers receive clearer and more relevant responses?

**How to measure:**

```text
Traveler feedback after proposal or booking
```

Example questions:

```text
Did the operator understand your request?
Was the response clear?
Did the proposed itinerary match your expectations?
Did you feel your needs were understood?
```

## Minimum Viable Pilot

A useful first pilot can be small.

Suggested pilot size:

```text
10 to 25 traveler inquiries
2 to 4 operator staff
1 tour company
2 to 4 weeks
```

## Pilot Data to Track

For each inquiry, track:

```text
Inquiry ID:
Date received:
Traveler language:
Operator output language:
Response time:
Traveler intent identified:
Missing information identified:
Cultural terms identified:
Risk flags identified:
Suggested reply used? yes / no / edited:
Escalated to senior staff? yes / no:
Proposal sent? yes / no:
Booking confirmed? yes / no:
Operator notes:
```

## Success Threshold

The pilot should be considered promising if:

```text
Staff can prepare useful replies faster.
Cultural misunderstandings are identified earlier.
Routine inquiries require less senior staff intervention.
Sensitive requests are flagged for human review.
More qualified inquiries move to proposal or booking.
```

## What Not to Measure Yet

Version 1 should not over-focus on:

```text
Perfect translation quality
Full automation
Voice cloning quality
Advanced analytics
End-to-end booking management
Production-scale reliability
```

Those can come later. Version 1 should prove that the workflow is useful for real tour operator staff.

## Pilot Review Questions

At the end of the pilot, review:

```text
Which traveler requests were easiest to process?
Which requests still required senior staff?
Which cultural phrases caused the most confusion?
Which risk flags were most useful?
Which suggested replies were actually sent?
Which parts of the output were ignored?
What should be added before building the Telegram bot further?
```

## Product Learning Goal

The main learning goal is to understand whether tour operators need:

```text
A Telegram bot
A web dashboard
A voice-note intake tool
A response template library
A cultural interpretation assistant
A multilingual operator briefing tool
A booking support workflow
```

The pilot should guide product direction rather than assume the final answer in advance.
