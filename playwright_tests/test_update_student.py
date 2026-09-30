def test_update_student(page):
    # Add a student for this test
    page.goto("http://127.0.0.1:5000/students/add")

    page.locator("#name").fill("Playwright Update Student")
    page.locator("#age").fill("20")
    page.locator("#marks").fill("80")

    page.locator("#add-student-button").click()

    # Find the student's ID
    page.goto("http://127.0.0.1:5000/students")

    row = page.locator(
        "tr",
        has_text="Playwright Update Student"
    )

    student_id = row.locator("td").first.text_content()

    # Open update page
    page.goto(
        f"http://127.0.0.1:5000/students/update/{student_id}"
    )

    # Update the student
    page.locator("#name").fill("Updated Playwright Student")
    page.locator("#age").fill("22")
    page.locator("#marks").fill("95")

    page.locator("#update-student-button").click()

    # Verify update
    page.goto("http://127.0.0.1:5000/students")

    assert "Updated Playwright Student" in page.content()