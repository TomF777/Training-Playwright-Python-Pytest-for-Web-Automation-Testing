# CSS selectors

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")
    # element with parent 'nav-bg-dark' and 
    # child element 'a' with two classes 'nav-link' and 'active'
    page.locator("nav.bg-dark a.nav-link.active").highlight()
    time.sleep(3)

    # element with parent 'div.bs-component' and next child 'ul' with class 'list-group'
    page.locator("div.bs-component > ul.list-group").highlight()
    time.sleep(3)

    # loose pseudo selector - it selects all h1 elements containing text 'Navs'
    page.locator("h1:text('Navs')").highlight()
    time.sleep(3)

    # strict pseudo selector - it only selects element with exact text 'Navs'
    page.locator("h1:text-is('Navs')").highlight()
    time.sleep(3)

    # visible pseudo class selector - selects only visible elements
    page.locator("div.dropdown-menu:visible").highlight()
    time.sleep(3)

    # select CSS element based on its number: 4th button on the page with class 'btn-primary'
    page.locator(":nth-match(button.btn-primary, 4)").highlight()
    time.sleep(3)

    page.locator(":nth-match(button:text('Primary'), 3)").highlight()
    time.sleep(3)