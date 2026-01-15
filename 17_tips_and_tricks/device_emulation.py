from playwright.sync_api import sync_playwright, ViewportSize

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context(
        color_scheme="dark",
        viewport={
            "width":300,
            "height": 500,
        }
    )

    page = context.new_page()
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    page.set_viewport_size(
        {
            "width": 1000,
            "height": 1000,
        }
    )