def test_invalid_marks(page):
    page.goto("http://127.0.0.1:5000/students/add")

    page.locator("#name").fill("Invalid Playwright Student")
    page.locator("#age").fill("20")
    page.locator("#marks").fill("150")

    page.locator("#add-student-button").click()

    # The invalid student should not be added
    page.goto("http://127.0.0.1:5000/students")

    assert "Invalid Playwright Student" not in page.content()