import pytest
from selenium import webdriver

from selenium_tests.pages.student_page import StudentPage
from database import get_connection


@pytest.fixture(autouse=True)
def clean_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students")

    conn.commit()

    cur.close()
    conn.close()


@pytest.fixture
def driver():

    driver = webdriver.Edge()

    driver.get("http://127.0.0.1:5000")

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def student_page(driver):

    return StudentPage(driver)