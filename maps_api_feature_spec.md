# Maps API Feature Spec

This file defines the planned Maps API feature for Voice of the Silk Road.

The goal is to make the bot more useful for tour operators by returning source-backed local place candidates with clickable links, rather than giving generic advice or telling staff to search manually.

## Product Goal

The bot should support local recommendation requests by calling a Maps or Places API and returning specific candidate places for human operator review.

The bot should not invent restaurant, café, bakery, market, hotel, museum, workshop, or attraction recommendations from model memory.

## Core Use Case

A traveler asks a place-based local recommendation question.

Example:

```text
Where can I find Bukhara-style somsa in Tashkent?
```

The bot should identify this as a place recommendation request and retrieve candidate places.

The output should give the operator concrete options to review:

```text
Place candidates:
1. Name
   Address
   Google Maps link
   Rating
   Review count
   Opening status if available
   Website or phone if available
   Why it may match
   Operator validation needed

2. Name
   Address
   Google Maps link
   Rating
   Review count
   Opening status if available
   Website or phone if available
   Why it may match
   Operator validation needed
```

## Human-in-the-Loop Rule

The bot should not send place recommendations automatically to travelers.

The bot should return candidate places to the tour operator.

The operator must review the results before sending a recommendation.

The operator should verify:

```text
Current opening hours
Recent reviews
Location suitability
Traveler comfort level
Food quality
Dietary fit
Language support
Accessibility
Whether the place truly matches the requested cultural or regional experience
```

## Source-Backed Recommendation Rule

The bot must distinguish between:

```text
Source-backed candidate:
A place returned by a Maps or Places API with a name, address, and link.

Model interpretation:
A reason the candidate may match the traveler request, based on returned data and the traveler’s stated intent.

Operator validation:
A human check before the place is recommended to the traveler.
```

The bot should not present a place as verified unless it was returned by the API.

The bot should not claim that a place is “the best” unless the operator has validated that claim.

The bot should not claim that a place serves a specific dish unless the API result or operator validation supports it.

## Initial API Choice

Use Google Places API first.

Reason:

```text
Google Places supports text-based place search.
Google Place Details can return richer place information.
Google Maps links can be included for operator review.
```

Yandex Maps may be added later as a second source for Uzbekistan-specific coverage comparison.

## Google Places API Behavior

### Text Search

Use Text Search for open-ended queries such as:

```text
Bukhara-style somsa in Tashkent
ceramics workshop in Rishtan
traditional plov restaurant in Tashkent
craft market in Bukhara
tea house near Registan
vegetarian restaurant in Samarkand
```

Text Search should return a small number of candidate places.

Recommended first limit:

```text
3 candidate places
```

### Place Details

If Text Search returns place IDs, Place Details can be used to retrieve richer information.

Useful fields may include:

```text
Place ID
Display name
Formatted address
Google Maps URI
Rating
User rating count
Business status
Current opening hours
Website URI
National phone number
International phone number
Types
Location
```

Use only fields needed for the operator workflow.

Do not request unnecessary fields because Places API field masks affect cost and latency.

## Environment Variable

The future code implementation should use:

```text
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
```

This key should be stored only in `.env`.

It should never be committed to GitHub.

The repo may include this placeholder in `.env.example` when implementation begins:

```text
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
```

## Place Recommendation Trigger Conditions

The bot should consider a Maps API lookup when the traveler asks about:

```text
Restaurants
Cafés
Bakeries
Food specialties
Markets
Museums
Craft workshops
Ceramics shops
Silk or textile workshops
Photo spots
Neighborhoods
Local experience locations
Hotels or lodging areas
Train station proximity
Attractions
Landmarks
Specific dishes in specific cities
```

Example trigger phrases:

```text
Where can I find...
Can you recommend...
Best place for...
Near...
In Tashkent...
In Samarkand...
In Bukhara...
In Khiva...
Bukhara-style somsa
Plov
Tea house
Ceramics
Suzani
Silk
Market
Workshop
Restaurant
Café
Bakery
Museum
```

## Non-Maps Requests

Do not use Maps API as the authority for official rules.

Examples:

```text
Can I take photos in the Tashkent metro?
Do I need a permit to film?
Can I fly a drone?
Can I visit a restricted area?
What are the visa rules?
What are the customs rules?
Do I need registration?
```

These require official-source review, not a place recommendation API.

The bot may still use Maps to identify place candidates if the request also asks about locations, but official-rule questions must be flagged separately.

## Mixed Request Example

Traveler asks:

```text
Can I film Soviet architecture and metro stations in Tashkent?
```

The bot should separate the request:

```text
Place component:
Possible architecture or metro-related locations may require place lookup.

Official-rule component:
Filming and photography rules require human review and official-source checking.
```

The bot should not provide final filming or photography advice.

## Output Format Change

Add a new operator-facing section to future bot output:

```text
Verified sources and candidate links:
```

This section should appear before:

```text
Risk or compliance flags:
```

For place recommendation requests, it should include API-returned candidates.

For non-place requests, it can say:

```text
No place lookup needed.
```

For official-rule requests, it can say:

```text
Official-source review needed. No final rule guidance should be given until the operator checks the relevant official source.
```

## Candidate Ranking Logic

The first version should rank candidates conservatively.

Preferred candidates should have:

```text
Clear name
Clear address
Google Maps link
Relevant place type
Higher rating
Meaningful number of reviews
Open or currently operating status if available
Reasonable proximity to requested city or area
```

The bot should not over-rank candidates based only on rating.

A place with a perfect rating and very few reviews may be less reliable than a place with a slightly lower rating and many reviews.

## Search Query Generation

For a place recommendation request, the bot or helper function should generate a concise search query.

Examples:

Traveler request:

```text
Where can I find Bukhara-style somsa in Tashkent?
```

Possible API query:

```text
Bukhara somsa Tashkent
```

Additional possible local-language variants for future improvement:

```text
Buxoro somsa Toshkent
бухарская самса Ташкент
```

For version 1 of this feature, use one primary query first.

Later versions can try multiple language variants and merge results.

## Operator Validation Notes

Each candidate should include a validation reminder.

Examples:

```text
Confirm current opening hours.
Check whether the place actually serves the requested dish.
Check whether recent reviews are positive.
Check whether the location is convenient for the traveler’s itinerary.
Check whether the venue is suitable for dietary restrictions, accessibility, or group size.
```

## Traveler-Facing Draft Rule

The traveler-facing draft should not automatically include all returned candidates.

The draft should say that the operator will verify options unless the operator has validated the places.

Safer draft example:

```text
Yes, we can look for Bukhara-style somsa options in Tashkent. We will verify current opening hours and local quality before recommending specific places. Do you prefer a simple local bakery, a sit-down restaurant, or a food-market stop?
```

Once the operator validates the API candidates, a future version may generate a more specific traveler-facing draft that includes selected links.

## Error Handling

If the Maps API call fails, the bot should not fail completely.

It should return:

```text
Maps lookup unavailable.
Suggested search query:
Operator validation needed:
```

The bot should still provide the normal traveler request analysis.

## No Hallucinated Places Rule

If the Maps API returns no usable result, the bot should say so.

It should not invent places.

It may provide search queries for operator follow-up.

## Privacy and Data Handling

The bot should not store traveler messages.

The bot should not store Maps API results in a database in the first implementation.

The bot may process one request at a time and return results to the operator.

## Initial Test Cases

Add tests for:

```text
Where can I find Bukhara-style somsa in Tashkent?
Can you recommend a vegetarian restaurant in Samarkand?
Where can I buy Rishtan ceramics?
Can I take photos in the Tashkent metro?
Can I film a YouTube video near government buildings and metro stations?
```

Expected behavior:

```text
Place recommendation requests should return candidate links.
Official-rule requests should trigger official-source review.
Mixed requests should separate place lookup from official-rule review.
No invented places should appear.
```

## Future Enhancements

Future versions may add:

```text
Yandex Maps lookup
Multiple language search variants
Operator-vetted favorites list
Result caching
Clickable inline Telegram buttons
Map preview links
Distance from hotel or itinerary stop
Open-now filtering
Cuisine or category filters
Review summarization
Source comparison between Google and Yandex
```

## Product Principle

The Maps API feature should make the bot more specific and useful while keeping the human operator responsible for final recommendations.

