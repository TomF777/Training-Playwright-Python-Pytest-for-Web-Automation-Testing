import pytest
from playwright.sync_api import *

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={'Content-Type': 'application/json'}
    )
    yield api_context
    api_context.dispose()


def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
            "users/add",
            data={
                "firstName": "Muhammad",
                "lastName": "Ovi",
                "age": 250
            }
        )

    # another option for POST with fetch method:
    # api_context.fetch(
    #     "users/add",
    #     method="POST",
    #     data={
    #         "firstName": "Muhammad",
    #         "lastName": "Ovi",
    #         "age": 250
    #     }
    # )
    
    user_data = response.json()
    print(f"\n {user_data}")
    assert user_data["id"] == 209
    assert user_data["firstName"] == "Muhammad"

def test_update_user(api_context: APIRequestContext):
        response = api_context.put(
            "users/1",
            data={
                "lastName": "Smith",
                "age": 20,
            }
        )

        user_data = response.json()
        print(user_data)
        assert user_data["lastName"] == "Smith"
        assert user_data["age"] == 20