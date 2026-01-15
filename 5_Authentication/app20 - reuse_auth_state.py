from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=500,
        args=["--disable-dev-shm-uasge", "--disable-blink-features=AutomationControlled"])
    # save authentication state
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )

    page = context.new_page()
    page.goto("https://accounts.google.com")

    # wait for manual 2FA if needed
    page.pause()

    context.close()