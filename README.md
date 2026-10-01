# Student Management Automation

This project automates testing of a Student Management System using Python, pytest, Selenium, Playwright, and Page Object Model (POM).

## Technologies Used

- Python
- Flask
- PostgreSQL
- pytest
- Selenium
- Playwright
- Page Object Model (POM)
- pytest-html

## Project Features

The Student Management System supports:

- Add Student
- View Students
- Search Student
- Update Student
- Delete Student
- Input validation

The automation project contains Selenium and Playwright test structures using Page Object Model.

## Project Structure

```text
student-management-automation/
│
├── app.py
├── database.py
├── .env
├── requirements.txt
├── pytest.ini
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── students.html
│   ├── search.html
│   └── update_student.html
│
├── selenium_tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── pages/
│   │   ├── __init__.py
│   │   └── student_page.py
│   │
│   ├── test_add_student.py
│   ├── test_delete_student.py
│   ├── test_search_student.py
│   ├── test_update_student.py
│   ├── test_validation.py
│   └── test_view_student.py
│
└── playwright_tests/
    ├── __init__.py
    └── pages/