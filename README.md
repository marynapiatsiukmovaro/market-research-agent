# Product Discovery Scout Agent

An autonomous AI agent for identifying high-potential e-commerce products suitable for rapid MVP testing through paid traffic (Meta, TikTok).

## Purpose

Not here to find perfect businesses.
Here to find products with a high probability of successful market validation and scalable paid advertising performance.

**Daily target:** Minimum 2 strong candidates — no upper limit. Report all products scoring 65+ as long as signal quality holds. Quality over quota — never force weak products.

## How It Works

```
Scan 15–20 candidates per keyword round
        ↓
Apply Mandatory Filters (fast reject)
        ↓
Score remaining products (0–100)
        ↓
Output all qualifying products (65+)
        ↓
Save to Notion database
```

## Architecture

```
market-research-agent/
├── core/                        # Universal rules shared by all departments
│   ├── identity.md              # Role, objective, output format
│   ├── mindset.md               # How to think and prioritize
│   ├── mandatory-filters.md     # Hard reject rules (apply before scoring)
│   ├── scoring-system.md        # 100-point weighted scoring (source of truth)
│   ├── product-requirements.md  # Product criteria and price logic
│   ├── founder.md               # Who Marina is, winner product definition
│   ├── research-framework.md    # 4-layer architecture: Core/Departments/Hypotheses/Learnings
│   ├── operating-rules.md       # Verification hierarchy, pivot triggers, anti-hallucination
│   └── session-health-rules.md  # Context monitoring and self-reporting
│
├── departments/                 # Per-channel sourcing operations (isolated)
│   ├── facebook-ads-library/    # FB Ads Library via VPS scraper (keyword-first discovery)
│   │   ├── workflow.md          # Session entry point — daily scout workflow
│   │   ├── pre-flight.md        # VPS connection and scraper runnable checklist
│   │   ├── methods/             # facebook_scraper.py, fast_filter.py, keyword-scan
│   │   ├── hypotheses/          # _active.md → current direction (single source) + archived
│   │   └── operational-memory/  # op-rules, learnings, keyword-map, founder-feedback, seen-advertisers
│   │
│   └── shophunter/              # ShopHunter store-first discovery (revenue / longevity / multi-store)
│       ├── workflow.md          # Session entry point → methods/discovery-funnel.md
│       ├── capabilities.md      # What ShopHunter exposes + inherited capabilities
│       ├── methods/             # discovery-funnel.md, interface-guide.md, subagent-spec.md
│       ├── hypotheses/          # research directions (storeleads-breadth, collection-monitor)
│       └── operational-memory/  # learnings, founder-feedback  (op-rules: not yet created)
│
├── shared/                      # Channel-agnostic resources
│   ├── founder-taste.md         # Marina's company-wide quality bar (read before scoring)
│   ├── reported-products.md     # Anti-duplicate check (read every session)
│   ├── rejected-products.md     # Failure patterns (read every session)
│   ├── successful-patterns.md   # Recurring winner traits
│   ├── failed-patterns.md       # Recurring weak patterns
│   ├── sources-overview.md      # How to read each signal type
│   ├── notion-schema.md         # Live Notion DB schema (verified source of truth)
│   ├── notion-workflow.md       # How to save findings to Notion
│   ├── product-validation.md    # Deep-validation checklist (85+ products)
│   └── skills/                  # product-discovery, paid-traffic-analysis, trend,
│                                #   wow-factor, ugc, sourcing, shophunter (store-signal)
│
├── review/                      # Promotion queue (learnings → core)
│   └── promotion-queue.md
│
├── prompts/                     # Ready-made session startup prompts
│
├── outputs/                     # Generated reports
│   └── daily-reports/           # YYYY-MM-DD.md per session
│
└── archive/                     # Historical reference material
```

**Department isolation rule:** Logic from one department must never bleed into another. Core files are shared; department files are not.
See `core/research-framework.md` for the full 4-layer architecture explanation.

## Scoring System

| Category | Points |
|----------|--------|
| Problem-Solving Strength | 20 |
| Wow-Effect / Scroll-Stopping | 20 |
| Entry Window (market timing) | 10 |
| Paid Ads Viability | 12 |
| Emotional Trigger Strength | 10 |
| Margin Potential | 10 |
| Market Size / Scalability | 6 |
| Logistics Simplicity | 5 |
| UGC Potential | 5 |
| Evergreen Potential | 2 |
| **Total** | **100** |

**Thresholds:**
- 85–100 → Worth Testing (exceptional)
- 70–84 → Worth Testing
- 55–69 → Worth Testing with caution / Rejected if saturation concerns
- Below 55 → Rejected

Full calibration guidance: `core/scoring-system.md`

## Product Requirements

- Preferred price: **$45–$79** | Extended range: **$39–$100** with justification
- Price $100–$170: score normally, Margin Potential capped at 5/10
- Price above $170: reject
- Competitor ad activity on Meta or TikTok required (proof of market)
- Minimum **3 creative angles** (single-angle products die under ad fatigue)
- Sourceable from China (Alibaba/AliExpress, 5+ suppliers)
- Lightweight shipping (under 1kg preferred)
- Low return risk
- No fake URLs — if a link cannot be found after real search, write "Not found"

## Notion Integration

All reported products (score 65+) are saved to the **Product Tracker** database in Notion with fields:
Score, Category, Recommendation, Founder Review (blank — Marina sets), Competitor Signal, Price Range, Emotional Trigger, Saturation, Ad Platform, Creative Angles, Source, Discovery Keyword, Notes, Ad Link, Store Link.

See `shared/notion-workflow.md` for the full save protocol.

## Operating Modes

- **Scout Mode** (default): concise outputs, fast filtering, all 65+ products reported
- **Deep Validation Mode**: triggered only for 85+ products or explicit request

## Tech Stack

- AI: Claude (Anthropic) via Claude Code
- Output storage: Notion database
- Version control: GitHub
- Primary source: Facebook Ads Library via VPS scraper (5.78.217.133)
- Secondary sources: Amazon, TikTok organic, AliExpress (verification only)
