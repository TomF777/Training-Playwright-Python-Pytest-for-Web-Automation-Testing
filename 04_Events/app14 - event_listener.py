# Playwright Event Listener

from playwright.sync_api import sync_playwright
import time

def on_load(page):
    print("Page loaded:", page)

with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # register event listener for 'load' event
    page.on("load", on_load)
    # another options: "domcontentloaded", "close", "response", "request", "filechooser"


    # visit the website - must be after event listener registration
    page.goto("https://bootswatch.com/default")

    #optionally remove listener
    page.remove_listener("load", on_load)

    browser.close()