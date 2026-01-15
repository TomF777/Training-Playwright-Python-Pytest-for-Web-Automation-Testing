# Playwright Handling Dialogs

from playwright.sync_api import sync_playwright
import time

def on_dialog(dialog):
    print("Dialog opened:", dialog.message)
    dialog.accept()     # click OK button
    #dialog.dismiss()    # click Cancel button

with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # create a new page
    page = browser.new_page()

    page.goto("https://testpages.herokuapp.com/pages/basics/alerts-javascript/")
    page.on("dialog", on_dialog)

    alert_btn = page.get_by_text("Show alert box")
    alert_btn.click()

    alert_btn = page.get_by_text("Show confirm box")
    alert_btn.click()
