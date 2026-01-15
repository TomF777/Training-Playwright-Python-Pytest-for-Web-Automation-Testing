from playwright.sync_api import Route, Page, expect

def on_route(route: Route):
    # change the request data
    #route.request.post_data = "data"
    #route.continue_()

    # cancel the navigation
    print("Request aborted: ", route.request)
    route.abort()

    # option for handling all images
    # if route.request.resource_type == "image":
    #     route.abort()
    # else:
    #     route.continue_()

def test_docs_link(page: Page):
    page.route(
        #"https://playwright.dev/python/img/playwright-logo.svg",
        "**/*.png",
        on_route
    )

    page.goto("https://playwright.dev/python")

    page.screenshot(path="playwright.jpg")

    # docs_link = page.get_by_role("link", name="Docs")
    # docs_link.click()

    # expect(page).to_have_url(
    #     "https://playwright.dev/python/docs/intro"
    # )

