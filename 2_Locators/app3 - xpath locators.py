# Locators Xpath

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    # select all h1 elements using xpath
    page.locator("xpath=//h1").highlight()
    time.sleep(2)

    # select h1 element with id attribute
    page.locator("xpath=//h1[@id='navbars']").highlight()
    time.sleep(2)

    # select input element with readonly attribute
    page.locator("xpath=//input[@readonly]").highlight()
    time.sleep(2)

    # select input element with attribute value = 'wrong value'
    page.locator("xpath=//input[@value='wrong value']").highlight()
    time.sleep(2)

    # Xpath functions: select h1 element with exact text = Heading 1
    page.locator("//h1[ text() = 'Heading 1' ]").highlight()
    time.sleep(2)

    # Xpath functions: select h1 element containing text 'Head'
    page.locator("//h1[ contains(text(), 'Head') ]").highlight()
    time.sleep(2)

    # select button element with class name 'btn-outline-primary'
    page.locator("//button[ contains(@class, 'btn-outline-primary') ]").highlight()
    time.sleep(4)

    # select input element with value attribute containing 'correct'
    page.locator("//input[ contains(@value, 'correct') ]").highlight()
    time.sleep(4)