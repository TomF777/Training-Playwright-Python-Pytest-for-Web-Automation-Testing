# Playwright custom waiting

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    link = page.get_by_role("link", name="2015")
    link.click()

    # wait for a specific selector to appear
    page.wait_for_selector(selector="td.film-title")

    browser.close()