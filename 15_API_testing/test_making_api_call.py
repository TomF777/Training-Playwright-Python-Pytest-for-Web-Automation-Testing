import json
from playwright.sync_api import *

def test_users_api(page: Page):
    response = page.goto("https://dummyjson.com/user/1")

    user_data = response.json()

    print(user_data)
    assert "firstName" in user_data
    assert "lastName" in user_data

    assert user_data["firstName"] == "Emily"
    assert user_data["lastName"] == "Johnson"