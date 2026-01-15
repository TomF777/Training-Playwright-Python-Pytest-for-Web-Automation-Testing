from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD


import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(
                            headless=False,
                            slow_mo=500,
                            channel='msedge',
                            args=["--disable-dev-shm-uasge", "--disable-blink-features=AutomationControlled"])

    page = browser.new_page()
    page.set_viewport_size({"width": 900, "height": 800})

    page.goto("https://accounts.google.com")
    email_input = page.get_by_label("Email or phone")

    email_input.fill(EMAIL)

    next_btn = page.get_by_role("button", name="Next")
    next_btn.click()

    password_input = page.get_by_label("Enter your password")
    password_input.fill(PASSWORD)

    next_btn = page.get_by_role("button", name="Next")
    next_btn.click()