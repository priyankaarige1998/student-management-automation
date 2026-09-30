def test_view_students(driver):
    driver.get("http://127.0.0.1:5000/students")

    table = driver.find_element("id", "students-table")

    assert table.is_displayed()