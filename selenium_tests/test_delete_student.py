def test_delete_student(student_page):

    student_page.add_student(
        "Delete Test Student",
        21,
        75
    )

    student_page.delete_student(
        "Delete Test Student"
    )

    assert not student_page.is_student_present(
        "Delete Test Student"
    )