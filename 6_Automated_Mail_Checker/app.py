"""
App to handling of new emails in an automated way.
"""

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        slow_mo=500,
        args=["--disable-dev-shm-uasge", "--disable-blink-features=AutomationControlled"])

    # save authentication state
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )

    page = context.new_page()
    page.goto("https://gmail.com")

    new_emails = []
    # locate all emails in the inbox
    emails = page.locator("div.ae4 table tr")

    for email in emails.all():
        is_new_email = email.locator(
            "td li[data-tooltip='Mark as read']"
            ).count() == 1

        if is_new_email:
            # get email sender
            sender = email.locator("td span[email]:visible").inner_text()

            # get message subject
            subject = email.locator("td span[data-thread-id]:visible").inner_text()

            new_emails.append([sender, subject])


    if len(new_emails) == 0:
        print("No new emails")
    else:
        print(f"{len(new_emails)} new emails ")

        for new_email in new_emails:
            print(new_email[0], new_email[1])
            print("-" * 30)

    context.close()

    time.sleep(4)