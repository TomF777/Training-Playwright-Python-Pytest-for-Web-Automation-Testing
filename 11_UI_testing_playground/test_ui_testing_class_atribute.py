#http://uitestingplayground.com/classattr

from playwright.sync_api import Page, expect

def test_class_atribute(page: Page):
    page.goto("http://uitestingplayground.com/classattr")

    # using CSS
    primary_button = page.locator("button.btn-primary")

    # using XPath
    primary_button = page.locator(
        "//button[ contains(@class, 'btn-primary') ]"
    )

    expect(primary_button).to_be_visible()
    primary_button.click()