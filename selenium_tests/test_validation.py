def test_invalid_marks(driver):
    driver.get("http://127.0.0.1:5000/students/add")

    driver.find_element("id", "name").send_keys("Invalid Student")
    driver.find_element("id", "age").send_keys("20")
    driver.find_element("id", "marks").send_keys("150")

    driver.find_element("id", "add-student-button").click()

    # The invalid student should not be added
    driver.get("http://127.0.0.1:5000/students")

    assert "Invalid Student" not in driver.page_source