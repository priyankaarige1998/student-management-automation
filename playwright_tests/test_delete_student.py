def test_delete_student(student_page):

    student_page.add_student(
        "Playwright Delete Student",
        21,
        75
    )

    student_page.delete_student(
        "Playwright Delete Student"
    )

    assert not student_page.is_student_present(
        "Playwright Delete Student"
    )