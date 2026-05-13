#!/bin/bash
PROJECT_DIR="/opt/market-research-agent"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/scout_$(date +%Y-%m-%d_%H-%M-%S).log"
MINEA_RESULTS="$LOG_DIR/minea_results.json"
PROMPT_FILE="$LOG_DIR/claude_prompt_$$.txt"

mkdir -p "$LOG_DIR"
echo "=== Scout session started: $(date) ===" | tee -a "$LOG_FILE"

cd "$PROJECT_DIR"

# ── Sync latest files from GitHub ────────────────────────────────────────────
echo "[0/3] Syncing from GitHub..." | tee -a "$LOG_FILE"
git stash 2>/dev/null || true
git pull origin main 2>&1 | tee -a "$LOG_FILE"

source venv/bin/activate
export $(grep -v '^#' .env | xargs)

# ── Step 1: Scrape Minea ──────────────────────────────────────────────────────
echo "[1/3] Running Minea scraper..." | tee -a "$LOG_FILE"
python3 skills/minea_scraper.py 2>&1 | tee -a "$LOG_FILE"

# ── Step 2: Build Claude prompt ───────────────────────────────────────────────
MINEA_COUNT=0
if [ -f "$MINEA_RESULTS" ]; then
    MINEA_COUNT=$(python3 -c "import json; data=json.load(open('$MINEA_RESULTS')); print(len(data))" 2>/dev/null || echo 0)
fi

echo "[2/3] Minea scraped $MINEA_COUNT products. Building prompt..." | tee -a "$LOG_FILE"

if [ -f "$MINEA_RESULTS" ] && [ "$MINEA_COUNT" -gt 0 ]; then
    MINEA_DATA="$(cat $MINEA_RESULTS)"
    cat > "$PROMPT_FILE" << ENDPROMPT
You are a Product Discovery Scout Agent for MOVARO brand.

STEP 0 — Load ALL context files before doing anything:
- brain/system.md
- brain/mindset.md
- criteria/mandatory-filters.md
- criteria/scoring-system.md
- memory/accepted-products.md   (anti-duplicate — do NOT report anything already listed)
- memory/rejected-products.md   (failure patterns — skip similar products faster)
- memory/founder-taste.md       (Marina's quality bar — read before scoring)
- memory/founder-feedback.md    (real YES/NO feedback — calibration source)
- memory/founder-goals.md       (who Marina is, winner product definition)
- config/sources.md
- config/session-health-rules.md  (monitor your own quality, self-report if degrading)

STEP 1 — Product candidates:
Minea scraped $MINEA_COUNT products from paid ads. Raw data:
$MINEA_DATA

STEP 2 — Apply mandatory filters (criteria/mandatory-filters.md):
Reject immediately if any filter fails. Do NOT score failing products.
Key new filters: unverifiable results = reject. Product seen everywhere = reject.

STEP 3 — Score remaining products (criteria/scoring-system.md):
Apply all 9 categories. Check against founder-taste.md before finalizing score.

STEP 4 — Select top products:
Report only 65+. Target 2-5. Quality over quota.
A product Marina would reject based on founder-feedback.md patterns = do not include.

STEP 5 — Assign Confidence Level and Discovery Type to each product:
Confidence: High (multiple validated signals) / Medium (good signals, incomplete) / Low (hypothesis)
Discovery Type: Minea ad data / Amazon signal / TikTok signal / Trend-based / etc.

STEP 6 — Find real links (Ad Link + Store Link). Never invent URLs. Not found = write 'Not found'.

STEP 7 — Output Scout Mode report. Save to outputs/daily-reports/$(date +%Y-%m-%d).md

STEP 8 — Save each accepted product (65+) to Notion database ID: 35b53ba8-196e-80bf-9be2-e6a4eb49059e
Follow workflows/notion-update.md. Fill: Founder Review = 'Needs Verification' (Marina will review).

STEP 9 — End-of-session updates (MANDATORY):
1. memory/accepted-products.md — add one row per accepted product
2. memory/rejected-products.md — add notable rejections with lessons
3. memory/successful-patterns.md — update Discovery Type win-rate table
4. memory/failed-patterns.md — add new failure patterns if discovered

STEP 10 — Session Status Output:
Report: Session Quality / Context Health / Confidence / products found / next recommended action.
ENDPROMPT

else
    cat > "$PROMPT_FILE" << ENDPROMPT
You are a Product Discovery Scout Agent for MOVARO brand.

STEP 0 — Load ALL context files before doing anything:
- brain/system.md + brain/mindset.md
- criteria/mandatory-filters.md + criteria/scoring-system.md
- memory/accepted-products.md + memory/rejected-products.md
- memory/founder-taste.md + memory/founder-feedback.md + memory/founder-goals.md
- config/sources.md + config/session-health-rules.md

Minea data unavailable this session. Use WebSearch as fallback.
When using WebSearch: attribute source as 'WebSearch' — NOT as 'TikTok Ads Library' or 'Meta Ads Library'.

Follow workflows/daily-scout.md exactly (all steps including STEP 8 memory update + STEP 10 session status).
Notion database ID: 35b53ba8-196e-80bf-9be2-e6a4eb49059e
ENDPROMPT

fi

# ── Step 3: Run Claude analysis ───────────────────────────────────────────────
echo "[3/3] Running Claude analysis..." | tee -a "$LOG_FILE"

# claude --dangerously-skip-permissions cannot run as root — use scout user
if [ "$(whoami)" = "root" ]; then
    chown scout:scout "$PROMPT_FILE" 2>/dev/null || true
    PFILE="$PROMPT_FILE"
    su - scout -c "cd /opt/market-research-agent && source venv/bin/activate && export \$(grep -v '^#' .env | xargs) && claude --dangerously-skip-permissions -p \"\$(cat '$PFILE')\"" 2>&1 | tee -a "$LOG_FILE"
else
    claude --dangerously-skip-permissions -p "$(cat "$PROMPT_FILE")" 2>&1 | tee -a "$LOG_FILE"
fi

rm -f "$PROMPT_FILE"

echo "=== Scout session ended: $(date) ===" | tee -a "$LOG_FILE"
