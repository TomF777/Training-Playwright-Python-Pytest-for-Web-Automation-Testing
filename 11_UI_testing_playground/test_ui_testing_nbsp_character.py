# http://uitestingplayground.com/nbsp
# testing of non breaking space character
from playwright.sync_api import Page, expect


def test_nbsp(page: Page):
    page.goto("http://uitestingplayground.com/nbsp")

    page.locator("//button[text()='My\u00a0Button']").click(
        timeout=2000
    )





