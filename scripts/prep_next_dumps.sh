#!/bin/sh
# Pre-load next-session category dumps (scroll-to-exhaustion). SEQUENTIAL — sh_cat_dump uses the
# persistent ShopHunter profile (lock), so never run these in parallel.
cd /opt/market-research-agent
echo "=== [1/4] Health & Beauty ==="
python3 scripts/sh_cat_dump.py "Health & Beauty"  health_beauty_shops.json  8000 hb_dump.sentinel
echo "=== [2/4] Luggage & Bags ==="
python3 scripts/sh_cat_dump.py "Luggage & Bags"   luggage_bags_shops.json   8000 lb_dump.sentinel
echo "=== [3/4] Sporting Goods ==="
python3 scripts/sh_cat_dump.py "Sporting Goods"   sporting_goods_shops.json 8000 sg_dump.sentinel
echo "=== [4/4] Software ==="
python3 scripts/sh_cat_dump.py "Software"         software_shops.json       8000 sw_dump.sentinel
echo "=== ALL_DUMPS_DONE ==="
