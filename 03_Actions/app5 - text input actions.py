# Text input actions

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    input = page.get_by_label("Email address").first

    # fill the input
    input.fill("me@that.site")
    time.sleep(3)

    # clear the input
    input.clear()
    time.sleep(2)

    # type characters with delay into input field
    input.type("you@that.site", delay=400)
    time.sleep(2)

    # select text input containing text
    valid_input = page.get_by_label("Valid input").first
    # get the value of the input field
    valid_input.input_value()