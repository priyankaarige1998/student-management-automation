def test_view_students(page):
    page.goto("http://127.0.0.1:5000/students")

    table = page.locator("#students-table")

    assert table.is_visible()