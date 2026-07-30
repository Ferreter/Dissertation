import asyncio
import requests
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

URL = "https://www.barchart.com/stocks/quotes/NVDA/gamma-exposure"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1499030863180992563/BF2DedZZ31GOYtX8G83rUmFK2Vz1jjiq9zshw92nrvvr6tQGOHriG0yITWnhiVg5zsgY"
SCREENSHOT_PATH = "nvda_gamma_chart.png"


async def main():
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

        # Accept cookie popup if it appears
        try:
            await page.locator("a.cmpboxbtnyes").click(timeout=10000)
            await page.wait_for_timeout(2000)
        except Exception:
            print("Cookie popup not found or already accepted")

        # Wait until the Highcharts SVG chart exists
        await page.locator("svg.highcharts-root").first.wait_for(timeout=30000)

        # Optional: wait for chart rendering to settle
        await page.wait_for_timeout(2000)

        # Remove sticky ads / footer overlays
        await page.evaluate("""
        document.querySelectorAll(
                '.raptive-footer, .adthrive-ad, .adthrive-footer, iframe[title="3rd party ad content"]'
            ).forEach(el => el.remove());
        """)
        await page.wait_for_timeout(1000)
        # Screenshot only the SVG chart
        chart = page.locator("svg.highcharts-root").first
        await chart.scroll_into_view_if_needed()
        await chart.screenshot(path=SCREENSHOT_PATH)

        await browser.close()

    # Send screenshot to Discord
    with open(SCREENSHOT_PATH, "rb") as f:
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            data={"content": "NVDA Gamma Exposure Chart"},
            files={"file": f}
        )

    print(response.status_code, response.text)


if __name__ == "__main__":
    asyncio.run(main())