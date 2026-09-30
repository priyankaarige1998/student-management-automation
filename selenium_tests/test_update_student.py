def test_update_student(driver):
    # First add a student for this test
    driver.get("http://127.0.0.1:5000/students/add")

    driver.find_element("id", "name").send_keys("Update Test Student")
    driver.find_element("id", "age").send_keys("20")
    driver.find_element("id", "marks").send_keys("80")

    driver.find_element("id", "add-student-button").click()

    # Find the newly added student's ID from the students table
    driver.get("http://127.0.0.1:5000/students")

    row = driver.find_element(
        "xpath",
        "//tr[td[normalize-space()='Update Test Student']]"
    )

    student_id = row.find_elements("tag name", "td")[0].text

    # Open update page
    driver.get(
        f"http://127.0.0.1:5000/students/update/{student_id}"
    )

    # Update the student
    driver.find_element("id", "name").clear()
    driver.find_element("id", "name").send_keys("Updated Student")

    driver.find_element("id", "age").clear()
    driver.find_element("id", "age").send_keys("22")

    driver.find_element("id", "marks").clear()
    driver.find_element("id", "marks").send_keys("95")

    driver.find_element("id", "update-student-button").click()

    # Verify the update
    driver.get("http://127.0.0.1:5000/students")

    assert "Updated Student" in driver.page_source