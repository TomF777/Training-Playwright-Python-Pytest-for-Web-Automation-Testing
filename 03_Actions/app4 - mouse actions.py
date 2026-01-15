# mouse actions

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    # click on a button
    button = page.get_by_role("button", name="Block button").first
    button.click()
    time.sleep(2)

    # double click on a button with 500ms delay between clicks
    button.dblclick(delay=500)

    # click button with special keys
    button.click(modifiers=["Shift", "Alt", "Control"])

    # hover over a button
    outline_button = page.locator("button.btn-outline-primary")
    outline_button.hover()