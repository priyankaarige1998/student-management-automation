def test_add_student(student_page):

    student_page.add_student(
        "Selenium Student",
        21,
        85
    )

    assert student_page.is_student_present(
        "Selenium Student"
    )