def test_search_student(page):
    # Add a student for this test
    page.goto("http://127.0.0.1:5000/students/add")

    page.locator("#name").fill("Playwright Search Student")
    page.locator("#age").fill("21")
    page.locator("#marks").fill("82")

    page.locator("#add-student-button").click()

    # Verify student was added
    page.goto("http://127.0.0.1:5000/students")

    assert "Playwright Search Student" in page.content()

    # Search for the student
    page.goto("http://127.0.0.1:5000/students/search")

    page.locator("#search").fill("Playwright Search Student")
    page.locator("#search-button").click()

    assert "Playwright Search Student" in page.content()