def test_search_student(driver):
    # Add a student for this test
    driver.get("http://127.0.0.1:5000/students/add")

    driver.find_element("id", "name").send_keys("Search Test Student")
    driver.find_element("id", "age").send_keys("21")
    driver.find_element("id", "marks").send_keys("80")

    driver.find_element("id", "add-student-button").click()

    # Verify that the student was actually added
    driver.get("http://127.0.0.1:5000/students")

    assert "Search Test Student" in driver.page_source

    # Now search for the student
    driver.get("http://127.0.0.1:5000/students/search")

    driver.find_element("id", "search").send_keys("Search Test Student")
    driver.find_element("id", "search-button").click()

    # Verify search result
    assert "Search Test Student" in driver.page_source