# dropdown menu

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    time.sleep(2)

    # open dropdown menu
    dropdown = page.locator("button#btnGroupDrop1")
    dropdown.click()

    # click on last dropdown link
    dropdown_link = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last
    dropdown_link.click()
    time.sleep(4)