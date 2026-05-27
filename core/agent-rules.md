# AGENT CORE RULES

## Product State Architecture

Products exist in distinct states. States are NOT mutually exclusive — a product may hold multiple states simultaneously.

| State | Definition | Tracked In |
|-------|-----------|-----------|
| **Reported** | Scored 65+ and surfaced by agent. NOT founder-approved by default. | shared/reported-products.md |
| **Founder Approved** | Explicitly validated by Marina (Approved / Consider). Human-only. Agent never sets this. (**Watchlist** = study/radar/may-return, NOT validation & NOT closed; **Rejected** = closed.) | departments/{dept}/operational-memory/founder-feedback.md + Notion Founder Review |
| **Rejected** | Failed filters, scored below 65, or rejected by founder after review. Still useful as negative calibration. | shared/rejected-products.md + Notion |
| **Needs Verification** | Interesting opportunity with insufficient validation (missing links, unclear saturation, etc.). AI/system state — NOT a founder decision. | Notion Recommendation field |
| **Calibration Example** | Used to improve future reasoning, scoring, and pattern recognition. May or may not be founder-approved. | shared/founder-taste.md + shared/successful-patterns.md |

### State separation rules
- **Recommendation** (Worth Testing / Needs Verification / Rejected) = agent evaluation. Agent sets this.
- **Founder Review** (Approved / Consider / Watchlist / Rejected — 4 tiers, see `shared/notion-schema.md`) = human decision. Marina sets this. Agent never sets this. **Watchlist = on-radar / study / may-return — NOT approval and NOT closed; never stop monitoring a Watchlist category.**
- A product scoring 65+ is Reported. It is NOT automatically Founder Approved.
- A product can be Reported + Rejected (reported this session, rejected by Marina afterward).
- A product can be Rejected + Calibration Example (useful as negative pattern, not for selling).
- Needs Verification lives in Recommendation logic only, not in Founder Review.

---

## Thinking Rules
- Think probabilistically, never assume certainty
- "This may work" not "this will work"
- Every evaluation is a probability, not a guarantee
- Avoid hype and emotional reasoning

## Operational Rules
- Always apply mandatory filters BEFORE scoring
- Never score a product that failed mandatory filters
- Default to Scout Mode — deep analysis only on 85+ products
- Target 2–5 products per session — quality over quota, never force weak products to fill 5
- Scan 15–20 candidates per session
- If fewer than 2 score 65+, output only what genuinely qualifies — do NOT lower the bar

## Quality Rules
- Reject fast on weak products — don't waste reasoning tokens
- A product with one creative angle is not a product, it's a liability
- No competitor ads = no proof anyone will pay for traffic = higher risk
- Preferred price $45–$79. Extended range $39–$100 acceptable with justification. Under $39: reject unless margins confirmed. $100–$170: score normally, Margin Potential cap 5/10, strong social proof preferred but NOT mandatory. Above $170: reject.

## URL Rules (critical — read carefully)
- NEVER invent, guess, or construct a URL
- If a link cannot be found after a real search → write "Not found"
- A plausible-looking fake URL is worse than no URL — it wastes the user's time
- Only attach URLs you have actually seen and verified exist
- When in doubt: "Not found" is always the correct answer

## Output Rules
- Scout Mode: concise, structured, scannable
- No unnecessary explanations
- Always include Score and Recommendation
- Always include Source (where found)
- Save to Notion after every session
- Update memory files at end of every session (non-negotiable)
