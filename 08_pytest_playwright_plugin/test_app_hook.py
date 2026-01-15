from playwright.sync_api import Page
import pytest

@pytest.fixture
def playwright_page(page: Page):
    page.goto("https://playwright.dev/python")
    return page

def test_page_has_docs_link(playwright_page: Page):
    link = playwright_page.get_by_role("link", name="Docs")
    assert link.is_visible()


def test_page_has_get_visits_docs(playwright_page: Page):
    link = playwright_page.get_by_role("link", name="GET STARTED")
    link.click()
    assert playwright_page.url == "https://playwright.dev/python/docs/intro"

