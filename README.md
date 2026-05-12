# Market Research Agent

An AI-powered market research system that autonomously gathers, analyzes, and synthesizes competitive intelligence, market trends, and industry insights.

## Overview

Market Research Agent is a modular AI system built on top of Claude that performs deep market research on demand. It breaks complex research tasks into structured workflows, applies evaluation criteria, and produces actionable reports.

## Architecture

```
market-research-agent/
├── brain/          # Core reasoning and orchestration logic
├── criteria/       # Evaluation frameworks and scoring rubrics
├── prompts/        # System and task-specific prompt templates
├── skills/         # Modular capability units (search, scrape, summarize)
├── workflows/      # Multi-step research pipeline definitions
├── memory/         # Persistent context, findings, and knowledge base
└── research/       # Output reports and research artifacts
```

## Modules

### /brain
The central orchestrator. Manages task decomposition, agent routing, and synthesis of results from multiple sources into coherent insights.

### /criteria
Evaluation frameworks used to score and filter information — relevance rubrics, source credibility checks, market signal scoring, and competitive threat matrices.

### /prompts
Prompt templates for each research phase: query generation, source evaluation, competitive analysis, trend detection, and final report synthesis.

### /skills
Atomic capability modules:
- **search** — web and academic search
- **scrape** — structured data extraction from websites
- **summarize** — compress and distill long-form content
- **compare** — side-by-side competitor analysis
- **trend** — time-series signal detection

### /workflows
Orchestrated research pipelines:
- `competitor-analysis.yaml` — full competitive landscape scan
- `market-sizing.yaml` — TAM/SAM/SOM estimation workflow
- `trend-report.yaml` — emerging trend identification
- `customer-persona.yaml` — ICP and buyer persona research

### /memory
Persistent storage for research findings, entity knowledge graphs, and source credibility scores. Enables the agent to build cumulative knowledge over time.

### /research
Final output artifacts: reports, summaries, raw data exports, and visualizations produced by completed research runs.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run a research workflow
python run.py --workflow competitor-analysis --topic "AI coding assistants"

# Output will be saved to /research/
```

## Configuration

Copy `.env.example` to `.env` and set your API keys:

```env
ANTHROPIC_API_KEY=your_key_here
SERP_API_KEY=your_key_here
```

## Tech Stack

- **AI Model** — Claude (Anthropic)
- **Orchestration** — Custom multi-agent framework
- **Storage** — Local filesystem + optional vector DB
- **Search** — SerpAPI / Tavily

## License

MIT
