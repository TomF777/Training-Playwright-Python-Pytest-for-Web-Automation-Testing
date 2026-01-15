from playwright.sync_api import Page, expect

def test_page_has_docs_link(browser_name: str, page: Page):
    if browser_name != "firefox":
        page.goto("https://playwright.dev/python")

        docs_link = page.get_by_role("link", name="Docs")
        expect(docs_link).to_be_visible()


def test_get_started_visits_docs(is_firefox:bool, page: Page):
    if is_firefox:
        page.goto("https://playwright.dev/python")

        get_started_link = page.get_by_role(
            "link", name="GET STARTED")
        get_started_link.click()

        expect(page).to_have_url("https://playwright.dev/python/docs/intro")

