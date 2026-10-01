def test_invalid_marks(student_page):

    student_page.add_student(
        "Invalid Playwright Student",
        20,
        150
    )

    assert not student_page.is_student_present(
        "Invalid Playwright Student"
    )