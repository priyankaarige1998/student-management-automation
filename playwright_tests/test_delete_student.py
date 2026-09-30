def test_delete_student(page):
    # Add a student for this test
    page.goto("http://127.0.0.1:5000/students/add")

    page.locator("#name").fill("Playwright Delete Student")
    page.locator("#age").fill("21")
    page.locator("#marks").fill("75")

    page.locator("#add-student-button").click()

    # Find the student's row
    page.goto("http://127.0.0.1:5000/students")

    row = page.locator(
        "tr",
        has_text="Playwright Delete Student"
    )

    # Click Delete
    row.locator(".delete-button").click()

    # Verify deletion
    page.goto("http://127.0.0.1:5000/students")

    assert "Playwright Delete Student" not in page.content()