import asyncio
import requests
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

URL = "https://www.barchart.com/stocks/quotes/NVDA/gamma-exposure"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1499030863180992563/BF2DedZZ31GOYtX8G83rUmFK2Vz1jjiq9zshw92nrvvr6tQGOHriG0yITWnhiVg5zsgY"
screenshot_path = "screenshot.png"



async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        )

        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="en-US"
        )

        page = await context.new_page()
        await Stealth().apply_stealth_async(page)

        await page.goto(URL, wait_until="domcontentloaded", timeout=80000)
        await page.wait_for_timeout(2000)

        try:
            await page.locator("a.cmpboxbtnyes").click(timeout=10000)
            print("Clicked Accept All")
            await page.wait_for_timeout(2000)
        except Exception as e:
            print("Cookie popup not found:", e)

        await page.screenshot(path=screenshot_path, full_page=True)

        await browser.close()

    with open(screenshot_path, "rb") as f:
        r = requests.post(
            DISCORD_WEBHOOK_URL,
            data={"content": "NVDA Gamma Exposure Screenshot"},
            files={"file": f}
        )

    print(r.status_code, r.text)


asyncio.run(main())