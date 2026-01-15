from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")

    #expect(link).to_be_visible()
    # another options:
    expect(link).to_be_enabled()
    #expect(link).not_to_be_visible()
    #expect(link).to_be_hidden()