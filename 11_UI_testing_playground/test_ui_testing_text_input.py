# http://uitestingplayground.com/textinput

from playwright.sync_api import Page, expect

def test_text_input(page: Page):
    page.goto("http://uitestingplayground.com/textinput")

    query = "new button label"

    #input = page.get_by_label("Set New Button Name") - # why accessing by label and not by placeholder ???
    input = page.get_by_placeholder("MyButton")
    input.fill(query)

    btn = page.locator("button.btn-primary")
    btn.click()

    expect(btn).to_have_text(query)
