"""Capture the legacy NVDA gamma chart and send it to Discord.

This experiment is retained for provenance but is separate from the final
dissertation pipeline. The webhook is read from the local environment file.
"""

import asyncio
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

URL = "https://www.barchart.com/stocks/quotes/NVDA/gamma-exposure"


def find_project_root() -> Path:
    """Find the repository from either the root or the scripts folder."""
    for candidate in (Path.cwd().resolve(), *Path.cwd().resolve().parents):
        if (candidate / "config.yaml").is_file():
            return candidate
    raise FileNotFoundError("Could not find config.yaml and the project root.")


PROJECT_ROOT = find_project_root()
load_dotenv(PROJECT_ROOT / "main.env")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
SCREENSHOT_PATH = PROJECT_ROOT / "outputs" / "legacy_browser" / "nvda_gamma_chart.png"


async def main():
    if not DISCORD_WEBHOOK_URL:
        raise RuntimeError("Set DISCORD_WEBHOOK_URL in main.env before running this script.")
    SCREENSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="en-US"
        )

        page = await context.new_page()
        await Stealth().apply_stealth_async(page)

        await page.goto(URL, wait_until="domcontentloaded", timeout=90000)
        await page.wait_for_timeout(3000)

        # I treat the cookie prompt as optional because it is not shown on every run.
        try:
            await page.locator("a.cmpboxbtnyes").click(timeout=10000)
            await page.wait_for_timeout(2000)
        except Exception:
            print("Cookie popup not found or already accepted")

        # I wait for the SVG itself rather than relying on a fixed page delay.
        await page.locator("svg.highcharts-root").first.wait_for(timeout=30000)

        # I allow the final animation to settle before taking the image.
        await page.wait_for_timeout(2000)

        # I remove overlays that can hide the chart without changing its data.
        await page.evaluate("""
        document.querySelectorAll(
                '.raptive-footer, .adthrive-ad, .adthrive-footer, iframe[title="3rd party ad content"]'
            ).forEach(el => el.remove());
        """)
        await page.wait_for_timeout(1000)
        # I capture only the chart so the resulting artefact is reproducible.
        chart = page.locator("svg.highcharts-root").first
        await chart.scroll_into_view_if_needed()
        await chart.screenshot(path=str(SCREENSHOT_PATH))

        await browser.close()

    # I send the saved file only after the browser has closed cleanly.
    with SCREENSHOT_PATH.open("rb") as image_file:
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            data={"content": "NVDA Gamma Exposure Chart"},
            files={"file": image_file},
            timeout=60,
        )
        response.raise_for_status()

    print(response.status_code, response.text)


if __name__ == "__main__":
    asyncio.run(main())
