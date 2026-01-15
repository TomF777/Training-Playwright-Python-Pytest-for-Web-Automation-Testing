from playwright.sync_api import Page

def test_take_screenshot(page: Page):
    page.goto("https://playwright.dev/python")

    # screenshot of a page
    page.screenshot(path="playwright.jpg")
    page.screenshot(path="playwright.jpg", full_page=True)

    # screenshot of a link button
    link = page.get_by_role("link", name="GET STARTED")
    link.screenshot(path="get_started.png")
    link.click()

    assert page.url == "https://playwright.dev/python/docs/intro"