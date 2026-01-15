"""
This example saves all steps during steps as trace 
and put it into trace.zip file.

To see the trace launch the command:
playwright show-trace trace.zip

or

visit the page: trace.playwright.dev
and upload the trace.zip file
"""

import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    yield
    context.tracing.stop(path="trace.zip")

def test_page_has_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == "https://playwright.dev/python/docs/intro"

