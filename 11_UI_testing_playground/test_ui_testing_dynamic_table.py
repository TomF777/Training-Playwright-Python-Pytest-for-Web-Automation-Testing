# http://uitestingplayground.com/dynamictable

from playwright.sync_api import Page, expect

def test_dynamic_table(page: Page):
    page.goto("http://uitestingplayground.com/dynamictable")

    label = page.locator("p.bg-warning").inner_text()
    percentage = label.split()[-1]

    column_headers = page.get_by_role("columnheader")
    cpu_column = None

    for idx in range(column_headers.count()):
        column_header = column_headers.nth(idx)

        if column_header.inner_text() == "CPU":
            cpu_column = idx
            break

    assert cpu_column != None

    rowgroup = page.get_by_role("rowgroup").last
    chrome_row = rowgroup.get_by_role("row").filter(
        has_text="Chrome"
    )

    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    expect(chrome_cpu).to_have_text(percentage)
