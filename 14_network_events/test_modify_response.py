from playwright.sync_api import Route, Page


def on_route(route: Route):
    # route.fulfill(
    #     status=200,
    #     body="<html><body><h1>Custom Response!</h1></body></html>"
    # )

    response = route.fetch()
    body = response.text().replace(
        " enables reliable end-to-end testing for modern web apps.",
        " is an awesome framework for web automation"
    )

    route.fulfill(
        response=response,
        body=body,
    )


def test_docs_link(page: Page):
    page.route(
        "https://playwright.dev/python",
        on_route
    )

    page.goto("https://playwright.dev/python")
    page.pause()