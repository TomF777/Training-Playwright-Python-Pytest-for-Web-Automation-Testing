# http://uitestingplayground.com/progressbar

from playwright.sync_api import Page, expect

def test_progressbar(page: Page):
    page.goto("http://uitestingplayground.com/progressbar")

    progressbar = page.get_by_role("progressbar")

    start_btn = page.get_by_role("button", name="Start")
    stop_btn = page.get_by_role("button", name="Stop")

    start_btn.click()

    while True:
        progressvalue = int(progressbar.get_attribute("aria-valuenow"))
        if progressvalue >= 75:
            break
        else:
            print(f"Percent: {progressvalue}%")

    stop_btn.click()
    assert progressvalue >= 75
