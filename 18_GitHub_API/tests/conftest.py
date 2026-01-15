"""
 Shared fixture in test session using a Conftest module.
 Using the Conftest module, we can define the fixtures.
 Pytest will find this Conftest module, create all the fixtures inside of the file and
 provide it to all the test functions which request for the same.

 The feature has not been imported in any of these files and
 it's only been stored in the conftest module
"""

import pytest
from creds import *
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture
def feature():
    return "FEATURE"

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url="https://api.github.com/",
        extra_http_headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {GITHUB_ACCESS_TOKEN}"
        }
    )
    yield context
    context.dispose()


@pytest.fixture(autouse=True, scope="session")
def create_test_repository(api_context: APIRequestContext):
    # create a test repo
    post_response = api_context.post(
        "/user/repos",
        data={"name": GITHUB_REPO}
    )
    assert post_response.ok
    yield

    # delete test repo
    delete_response = api_context.delete(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}"
    )
    assert delete_response.ok