#!/bin/sh
# Seed A&P shops into the niche collection + the general "Shops" collection (toggle-safe add only).
cd /opt/market-research-agent
IDS=$(cat logs/shophunter/ap_seed_ids.txt)
echo "=== ADD to Animals & Pet Supplies ==="
python3 scripts/sh_collection_manage.py add "Animals & Pet Supplies" $IDS
echo "=== NICHE_DONE ==="
echo "=== ADD to Shops ==="
python3 scripts/sh_collection_manage.py add "Shops" $IDS
echo "=== ALLDONE_MARKER ==="
