from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    dropdown_menu = page.locator("ul.dropdown__menu")

    expect(dropdown_menu).to_contain_text("Python")
    expect(dropdown_menu).to_contain_text("Java")
    expect(dropdown_menu).to_contain_text("Node.js")
    expect(dropdown_menu).to_contain_text(".NET")

