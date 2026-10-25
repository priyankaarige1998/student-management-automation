from database import get_connection


def test_invalid_marks(student_page):
    student_page.add_student(
        "Invalid Student",
        20,
        150
    )

    # Verify that the validation error is displayed.
    error = student_page.wait.until(
        lambda driver: driver.find_element(
            "id", "validation-error"
        )
    )

    assert "marks must be between 0 and 100" in error.text

    # Verify that the invalid student was not saved.
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT COUNT(*) FROM students WHERE name = %s",
            ("Invalid Student",)
        )
        count = cur.fetchone()[0]
    finally:
        cur.close()
        conn.close()

    assert count == 0

