# Product Discovery Scout Agent

An autonomous AI agent for identifying high-potential e-commerce products suitable for rapid MVP testing through paid traffic (Meta, TikTok).

## Purpose

Not here to find perfect businesses.
Here to find products with a high probability of successful market validation and scalable paid advertising performance.

**Daily target:** 5 qualified products/day from scanning 15–20 candidates.

## How It Works

```
Scan 15–20 candidates
        ↓
Apply Mandatory Filters (fast reject)
        ↓
Score remaining products (0–100)
        ↓
Output top 5 in Scout Mode format
        ↓
Save to Notion database
```

## Architecture

```
market-research-agent/
├── brain/               # Core identity, mindset, operating rules
│   ├── system.md        # Main system prompt (lean, ~50 lines)
│   ├── mindset.md       # Agent thinking style
│   ├── autonomy-rules.md
│   └── token-efficiency.md
├── criteria/            # Product evaluation logic
│   ├── mandatory-filters.md   # Hard reject rules (apply before scoring)
│   ├── scoring-system.md      # 100-point weighted scoring
│   ├── rejection-rules.md
│   └── product-requirements.md
├── skills/              # Modular intelligence blocks
│   ├── product-discovery.md
│   ├── paid-traffic-analysis.md
│   ├── wow-factor-analysis.md
│   ├── trend-analysis.md
│   ├── ugc-analysis.md
│   ├── sourcing-analysis.md
│   └── shophunter-analysis.md
├── workflows/           # Operational procedures
│   ├── daily-scout.md         # Main daily loop
│   ├── product-validation.md  # Deep validation for 85+ products
│   ├── notion-update.md       # How to save findings to Notion
│   └── telegram-report.md     # Daily summary format
├── prompts/             # Reusable task prompts
│   ├── find-products.md
│   ├── analyze-tiktok-ads.md
│   ├── validate-product.md
│   └── daily-report.md
├── memory/              # Learning layer
│   ├── accepted-products.md
│   ├── rejected-products.md
│   ├── successful-patterns.md
│   └── failed-patterns.md
├── config/              # Settings and integrations
│   ├── sources.md             # Research sources list
│   ├── notion-config.md       # Notion database schema
│   └── agent-rules.md         # Core operating rules
└── outputs/             # Generated reports
    ├── daily-reports/
    ├── high-potential-products/
    └── telegram-summaries/
```

## Scoring System

| Category | Points |
|----------|--------|
| Problem-Solving Strength | 20 |
| Wow-Effect / Scroll-Stopping | 20 |
| Paid Ads Viability | 15 |
| Emotional Trigger Strength | 10 |
| Market Size / Scalability | 10 |
| Margin Potential | 10 |
| Logistics Simplicity | 5 |
| UGC Potential | 5 |
| Evergreen Potential | 5 |
| **Total** | **100** |

**Thresholds:**
- 85–100 → High Priority Winning Product
- 70–84 → Worth Testing
- 55–69 → Medium Potential
- Below 55 → Reject

## Product Requirements

- Price range: **$39–$79** (hard filter — under $38 fails paid traffic economics)
- Competitor ad activity on Meta or TikTok (proof of market)
- Minimum **3 creative angles** (single-angle products die under ad fatigue)
- Sourceable from China (Alibaba/AliExpress, 5+ suppliers)
- Lightweight shipping (under 1kg preferred)
- Low return risk

## Notion Integration

All accepted products (score 65+) are saved to the **Product Tracker** database in Notion with fields:
Score, Category, Recommendation, Problem Solved, Emotional Trigger, Why It May Work, Price Range, Competitor Ads, Ad Platform, Creative Angles, Saturation, Supplier, Source.

## Operating Modes

- **Scout Mode** (default): concise outputs, fast filtering, 5 products/session
- **Deep Validation Mode**: triggered only for 85+ products or explicit request

## Tech Stack

- AI: Claude (Anthropic) via Claude Code
- Output storage: Notion database
- Version control: GitHub
- Sources: TikTok Ads Library, Meta Ads Library, Amazon Movers & Shakers, AliExpress, Alibaba
