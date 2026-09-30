def test_add_student(driver):
    driver.get("http://127.0.0.1:5000/students/add")

    driver.find_element("id", "name").send_keys("Selenium Student")
    driver.find_element("id", "age").send_keys("21")
    driver.find_element("id", "marks").send_keys("85")

    driver.find_element("id", "add-student-button").click()

    driver.get("http://127.0.0.1:5000/students")

    assert "Selenium Student" in driver.page_source