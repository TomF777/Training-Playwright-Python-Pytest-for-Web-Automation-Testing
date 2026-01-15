# Playwright Auto Waiting Navigation

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto(
            "https://bootswatch.com/default",
            wait_until="load"  # wait until all web page resources are loaded
            # other options: "domcontentloaded", "networkidle", "commit"
        )

    browser.close()