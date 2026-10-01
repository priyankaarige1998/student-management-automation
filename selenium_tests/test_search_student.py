def test_search_student(student_page):

    # Add student
    student_page.add_student(
        "Search Test Student",
        21,
        80
    )

    # IMPORTANT: verify that ADD really created the student
    assert student_page.is_student_present(
        "Search Test Student"
    )

    # Now perform search
    student_page.search_student(
        "Search Test Student"
    )

    # Verify search result
    assert "Search Test Student" in student_page.driver.page_source


def test_search_nonexistent_student(student_page):

    student_page.search_student(
        "Student Does Not Exist"
    )

    assert "No student found." in student_page.driver.page_source