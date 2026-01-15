# Keyboard Shortcuts

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")

    text_area = page.get_by_label("Example textarea")
    time.sleep(3)
    text_area.fill("word")
    text_area.press("KeyW")      # press single key
    text_area.press("KeyO")      # press single key
    text_area.press("Shift+KeyD")     # press special key
    text_area.press("Control+ArrowLeft") # press combination of keys
    text_area.press("ArrowRight")
    time.sleep(6)