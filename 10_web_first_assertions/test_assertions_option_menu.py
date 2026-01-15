from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://bootswatch.com/default")

    # one item menu
    option_menu = page.get_by_label("Example select")
    expect(option_menu).to_have_value("1")

    # multiple items menu
    multi_option_menu = page.get_by_label("Example multiple select")
    multi_option_menu.select_option(["2", "4"])

    expect(multi_option_menu).to_have_values(["2", "4"])