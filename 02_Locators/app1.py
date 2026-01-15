# locators

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the playwright website
    page.goto("https://playwright.dev/python")

    # locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")
    # check also get_by_text, get_by_link etc.
    docs_button.click()

    page.goto("https://unsplash.com")
    page.get_by_alt_text("a group of people sitting around a table with food").highlight()
    time.sleep(2)

    page.goto("https://bootswatch.com/default")
    page.get_by_title("Source Title").highlight()
    time.sleep(2)

    # select all buttons with name Primary
    page.get_by_role("button", name="Primary").highlight()

    # select first button with name Primary
    page.get_by_role("button", name="Primary").locator("nth=0").highlight()

    # filtering
    page.get_by_role("heading").filter(has_text="Heading").highlight()

    # select label with its parent ".."
    page.get_by_label("Email address").locator("..").highlight()

    # use CSS selector
    page.goto("https://bootswatch.com/default")
    page.locator("css=h1").highlight()
    page.locator("footer").highlight()
    # class selector with class name: btn-outline-success
    page.locator("button.btn-outline-success").highlight()
    
    # id selector
    page.locator("button#btnGroupDrop1").click()
    time.sleep(2)

    page.locator("id=btnGroupDrop1").highlight()
    time.sleep(2)

    # attribute selector
    page.locator("input[readonly]").highlight()
    time.sleep(2)

    # value selector
    page.locator("input[value='correct value']").highlight()

    # get the url
    print("Docs:", page.url)
    # close the browser
    browser.close()
