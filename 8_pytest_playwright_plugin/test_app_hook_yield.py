from playwright.sync_api import Page
import pytest

@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python")
    yield page
    page.close()
    print("\n Fixture: page closed")

def test_page_has_docs_link(page: Page):
    link = page.get_by_role("link", name="Docs")
    assert link.is_visible()


def test_page_has_get_visits_docs(page: Page):
    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    assert page.url == "https://playwright.dev/python/docs/intro"

