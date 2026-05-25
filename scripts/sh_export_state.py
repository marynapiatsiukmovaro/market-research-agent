# Export ShopHunter login from the persistent profile into a portable storage_state.json
# so N stateless parallel workers can share one login (no profile-lock fight).
from playwright.sync_api import sync_playwright
PROFILE = "/opt/market-research-agent/cookies/shophunter_profile"
STATE = "/opt/market-research-agent/cookies/sh_state.json"
with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE, headless=True,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        viewport={"width": 1500, "height": 1700})
    pg = ctx.new_page()
    pg.goto("https://app.shophunter.io/explore/shops", wait_until="domcontentloaded", timeout=45000)
    pg.wait_for_timeout(3500)
    title = pg.title()
    ctx.storage_state(path=STATE)
    ctx.close()
import os
print("STATE saved:", STATE, "bytes:", os.path.getsize(STATE), "| page title:", title[:60])
