# Radios, Ckeckboxes, and Switches

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    # select and click a radiobutton
    radio_option2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")

    radio_option2.check()
    time.sleep(2)

    # select and check a checkbox
    checkbox1 = page.get_by_label("Default checkbox")
    checkbox1.check()
    time.sleep(3)

    if checkbox1.is_checked() and \
        checkbox1.is_visible() and \
        checkbox1.is_enabled():
            checkbox1.uncheck()
            # another way to check/uncheck
            checkbox1.set_checked(True)
            checkbox1.set_checked(False)
            time.sleep(3)

    # select and check a switch
    switch = page.get_by_label("Checked switch checkbox input")
    switch.check()
    time.sleep(3)
    switch.uncheck()
    time.sleep(2)