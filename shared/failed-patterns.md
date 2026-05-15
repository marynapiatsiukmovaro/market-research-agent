# FAILED PATTERNS

**Purpose: Negative calibration.** Patterns that predict product failure or founder rejection.
These inform filter logic and scoring calibration — not founder approval status.
Update as new failure patterns emerge.

## Marina's Hard Rejections (confirmed from real feedback)

Key patterns with one illustrative example each. Full product log: `departments/facebook-ads-library/operational-memory/founder-feedback.md`.

### "Везде" Pattern — Auto-Reject
- Example: LED Light Therapy Wand (78) → "не вызывает вау, везде"
- **Rule:** If product is visible on Facebook/Instagram feeds regularly → do not propose

### "Пустышки" Pattern — Auto-Reject
- Example: Red Light Laser Hair Cap (80) → "недоказуемый результат, не хочу продавать пустышки"
- **Rule:** Hair regrowth, circulation improvement, immune boost, vague wellness = reject

### Late Market Entry — Auto-Reject
- Example: Lymphatic Drainage Massager (75) → "рынок уже создан, нужно заходить на старте"
- **Rule:** If 100+ active ads and product visible everywhere → too late to enter

### Long Explanation Required — Auto-Reject
- Example: Wireless TENS Patch (71) → "слишком долго объяснять"
- **Rule:** If customer needs to understand HOW it works before wanting it → reject for cold traffic

### Old Category — Auto-Reject
- Example: Ultrasonic Skin Scrubber (71) → "старый товар, нет вау-эффекта"
- **Rule:** If product concept is 3+ years old and has no new differentiator → reject

---

## Recurring Scoring Failures

### 71-Score With Saturation Warning = Reject In Practice
Products scoring 71 with HIGH saturation notes consistently rejected by Marina.
Practical rule: raise acceptance bar to 75+ for "Worth Testing" recommendation.

### WebSearch-Only Discovery = Low Quality Signal
All 3 sessions used WebSearch. Result: Marina approved only 3/14 products (21%).
WebSearch finds what's already trending = already saturated.
Fix: Minea data will find products at ad launch stage, not peak stage.

### Multi-Audience Scoring ≠ Market Size Reality
Air Compression Leg Massager scored 75 with 4 audiences, rejected as "narrow market."
Scoring system overestimated audience breadth. Marina's real-world market sense is more accurate.

---

## Problematic Categories (avoid unless very strong signal)

- Generic phone accessories — extreme saturation
- Basic fitness resistance bands — commodity
- Supplements without clear visual result — low UGC, high refund risk, ad policy risk
- EMS/electrical muscle stimulation — Meta ad policy risk, frequent bans
- Any product visible widely in Marina's own social media feed

## Weak Hook Patterns

- Feature-first ads (no emotional hook)
- Products that look identical to 50 Amazon listings
- "Improves your health" claims without specific visible mechanism
- Products requiring >10 seconds of explanation to create desire
