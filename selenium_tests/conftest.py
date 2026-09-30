import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.get("http://127.0.0.1:5000")
    driver.maximize_window()

    yield driver

    driver.quit()