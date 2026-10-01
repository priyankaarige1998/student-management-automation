from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StudentPage:

    BASE_URL = "http://127.0.0.1:5000"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_add_student(self):
        self.driver.get(
            f"{self.BASE_URL}/students/add"
        )

    def open_students(self):
        self.driver.get(
            f"{self.BASE_URL}/students"
        )

    def open_search(self):
        self.driver.get(
            f"{self.BASE_URL}/students/search"
        )

        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "search")
            )
        )

    def add_student(self, name, age, marks):

        self.open_add_student()

        self.driver.find_element(
            By.ID, "name"
        ).send_keys(name)

        self.driver.find_element(
            By.ID, "age"
        ).send_keys(str(age))

        self.driver.find_element(
            By.ID, "marks"
        ).send_keys(str(marks))

        self.driver.find_element(
            By.ID, "add-student-button"
        ).click()

    def search_student(self, name):

        self.open_search()

        search_box = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "search")
            )
        )

        search_box.clear()
        search_box.send_keys(name)

        self.driver.find_element(
            By.ID, "search-button"
        ).click()

    def get_student_id(self, name):

        self.open_students()

        row = self.driver.find_element(
            By.XPATH,
            f"//tr[td[normalize-space()='{name}']]"
        )

        cells = row.find_elements(
            By.TAG_NAME, "td"
        )

        return cells[0].text

    def update_student(
        self,
        student_id,
        name,
        age,
        marks
    ):

        self.driver.get(
            f"{self.BASE_URL}/students/update/{student_id}"
        )

        name_field = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "name")
            )
        )

        age_field = self.driver.find_element(
            By.ID, "age"
        )

        marks_field = self.driver.find_element(
            By.ID, "marks"
        )

        name_field.clear()
        age_field.clear()
        marks_field.clear()

        name_field.send_keys(name)
        age_field.send_keys(str(age))
        marks_field.send_keys(str(marks))

        self.driver.find_element(
            By.ID, "update-student-button"
        ).click()

    def delete_student(self, name):

        self.open_students()

        row = self.driver.find_element(
            By.XPATH,
            f"//tr[td[normalize-space()='{name}']]"
        )

        student_id = row.find_elements(
            By.TAG_NAME, "td"
        )[0].text

        self.driver.get(
            f"{self.BASE_URL}/students/delete/{student_id}"
        )

    def is_student_present(self, name):

        self.open_students()

        rows = self.driver.find_elements(
            By.XPATH,
            f"//tr[td[normalize-space()='{name}']]"
        )

        return len(rows) > 0

    def is_students_table_visible(self):

        return self.driver.find_element(
            By.ID, "students-table"
        ).is_displayed()