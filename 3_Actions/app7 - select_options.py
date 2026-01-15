# select options

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    # select one option
    select = page.get_by_label("Example select")
    select.select_option("2")
    time.sleep(2)
    select.select_option("1")
    time.sleep(2)

    # select multiple options
    multi_select = page.get_by_label("Example multiple select")
    multi_select.select_option(["1", "3"])