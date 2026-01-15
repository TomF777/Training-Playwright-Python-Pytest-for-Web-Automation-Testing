# Playwright Download Files

from playwright.sync_api import sync_playwright
import time

def on_download(download):
    print("Download received:", download)
    download.save_as("moon.jpg")

with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # create a new page
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/qe2RkzzMx9A")

    # event listener for download event
    page.once("download", on_download)

    btn = page.get_by_role("link", name="Download free")

    with page.expect_download() as download_info:
        btn.click()

    #download = download_info.value
    #download.save_as("moon.jpg")

    browser.close()