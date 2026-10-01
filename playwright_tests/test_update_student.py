def test_update_student(student_page):

    student_page.add_student(
        "Playwright Update Student",
        20,
        80
    )

    student_id = student_page.get_student_id(
        "Playwright Update Student"
    )

    student_page.update_student(
        student_id,
        "Updated Playwright Student",
        22,
        95
    )

    assert student_page.is_student_present(
        "Updated Playwright Student"
    )