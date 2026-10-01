def test_update_student(student_page):

    student_page.add_student(
        "Update Test Student",
        20,
        80
    )

    student_id = student_page.get_student_id(
        "Update Test Student"
    )

    student_page.update_student(
        student_id,
        "Updated Student",
        22,
        95
    )

    assert student_page.is_student_present(
        "Updated Student"
    )