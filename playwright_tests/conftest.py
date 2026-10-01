import pytest
from playwright.sync_api import sync_playwright

from playwright_tests.pages.student_page import StudentPage


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            "http://127.0.0.1:5000"
        )

        yield page

        browser.close()


@pytest.fixture
def student_page(page):

    return StudentPage(page)