import re
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")


    docs_link = page.get_by_role("link", name="Docs")

    expect(docs_link).to_have_class("navbar__item navbar__link")
    # or using reg exp. expecting of only one class:
    expect(docs_link).to_have_class(
        re.compile(r"navbar__link")
    )
    #expect(docs_link).to_have_id("playwright")
    expect(docs_link).to_have_attribute("href", "/python/docs/intro")