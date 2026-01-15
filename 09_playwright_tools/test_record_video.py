from playwright.sync_api import Browser, Page
import pytest

@pytest.fixture
def recordable_page(browser: Browser):
    context = browser.new_context(
    record_video_dir="video/"
    )
    page = context.new_page()
    yield page
    context.close()

def test_record_video(recordable_page):

    recordable_page.goto("https://playwright.dev/python")

    theme_btn = recordable_page.get_by_title("system mode")
    theme_btn.click()

    link = recordable_page.get_by_role("link", name="GET STARTED")
    link.click()

    assert recordable_page.url == "https://playwright.dev/python/docs/intro"