def test_search_student(student_page):

    student_page.add_student(
        "Playwright Search Student",
        21,
        82
    )

    student_page.search_student(
        "Playwright Search Student"
    )

    assert "Playwright Search Student" in student_page.page.content()


def test_search_nonexistent_student(student_page):

    student_page.search_student(
        "Student Does Not Exist"
    )

    assert "No student found." in student_page.page.content()