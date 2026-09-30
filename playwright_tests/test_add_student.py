def test_add_student(page):
    page.goto("http://127.0.0.1:5000/students/add")

    page.locator("#name").fill("Playwright Student")
    page.locator("#age").fill("21")
    page.locator("#marks").fill("88")

    page.locator("#add-student-button").click()

    page.goto("http://127.0.0.1:5000/students")

    assert "Playwright Student" in page.content()