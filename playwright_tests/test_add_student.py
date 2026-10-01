def test_add_student(student_page):

    student_page.add_student(
        "Playwright Student",
        21,
        88
    )

    assert student_page.is_student_present(
        "Playwright Student"
    )