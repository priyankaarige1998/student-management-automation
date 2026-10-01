def test_view_students(student_page):

    student_page.open_students()

    assert student_page.is_students_table_visible()