from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=500,
        channel='msedge',
        args=["--disable-dev-shm-uasge", "--disable-blink-features=AutomationControlled"])
    # save authentication state
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://accounts.google.com")

    # enter the email
    email_input = page.get_by_label("Email or phone")
    email_input.fill(EMAIL)

    page.get_by_role("button", name="Next").click()

    # enter the password
    password_input = page.get_by_label("Enter your password")
    password_input.fill(PASSWORD)

    page.get_by_role("button", name="Next").click()

    # wait for manual 2FA if needed
    page.pause()

    # save authentication state
    context.storage_state(path="playwright/.auth/storage_state.json")

    context.close()