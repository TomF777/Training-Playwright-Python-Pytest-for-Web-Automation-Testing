# Plywright Auto Waiting

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    link = page.locator("a.dropdown-item").first
    # timeout 5 sec if element not found
    link.click(timeout=5_000)
    browser.close()