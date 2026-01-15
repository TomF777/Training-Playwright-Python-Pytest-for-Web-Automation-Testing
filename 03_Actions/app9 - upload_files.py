# upload files

from playwright.sync_api import sync_playwright
import time
with sync_playwright() as playwright:
    # launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new page
    page = browser.new_page()
    # visit the website
    page.goto("https://bootswatch.com/default")
    
    file_input = page.get_by_label("Default file input example")
    # upload single file
    file_input.set_input_files("file_to_upload.txt")
    time.sleep(4)

    # upload file via file chooser
    with page.expect_file_chooser() as fc_info:
        file_input.click()
        file_chooser = fc_info.value
        file_chooser.set_files("file_to_upload.txt")