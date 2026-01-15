# http://uitestingplayground.com/click

from playwright.sync_api import Page, expect

def test_click_action(page: Page):
    page.goto("http://uitestingplayground.com/click")

    btn = page.get_by_role("button", name="Button That Ignores DOM Click Event")
    btn.click()

    expect(btn).to_have_class("btn btn-success")

