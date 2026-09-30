def test_delete_student(driver):
    # First add a student for this test
    driver.get("http://127.0.0.1:5000/students/add")

    driver.find_element("id", "name").send_keys("Delete Test Student")
    driver.find_element("id", "age").send_keys("21")
    driver.find_element("id", "marks").send_keys("75")

    driver.find_element("id", "add-student-button").click()

    # Find the student in the table
    driver.get("http://127.0.0.1:5000/students")

    row = driver.find_element(
        "xpath",
        "//tr[td[normalize-space()='Delete Test Student']]"
    )

    # Click Delete
    row.find_element("class name", "delete-button").click()

    # Verify the student was deleted
    driver.get("http://127.0.0.1:5000/students")

    assert "Delete Test Student" not in driver.page_source
