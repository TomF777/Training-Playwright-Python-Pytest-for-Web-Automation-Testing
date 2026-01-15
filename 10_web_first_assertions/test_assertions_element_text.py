from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    heading = page.locator("h1.hero__title")

    expect(heading).to_contain_text("testing")
    # expect exactly text
    expect(heading).to_have_text("Playwright enables reliable end-to-end testing for modern web apps.")