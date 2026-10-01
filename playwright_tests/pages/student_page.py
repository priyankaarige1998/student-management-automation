class StudentPage:

    BASE_URL = "http://127.0.0.1:5000"

    def __init__(self, page):
        self.page = page

    def open_add_student(self):
        self.page.goto(
            f"{self.BASE_URL}/students/add"
        )

    def open_students(self):
        self.page.goto(
            f"{self.BASE_URL}/students"
        )

    def open_search(self):
        self.page.goto(
            f"{self.BASE_URL}/students/search"
        )

    def add_student(self, name, age, marks):

        self.open_add_student()

        self.page.locator("#name").fill(name)
        self.page.locator("#age").fill(str(age))
        self.page.locator("#marks").fill(str(marks))

        self.page.locator(
            "#add-student-button"
        ).click()

    def search_student(self, name):

        self.open_search()

        self.page.locator("#search").fill(name)

        self.page.locator(
            "#search-button"
        ).click()

    def get_student_id(self, name):

        self.open_students()

        row = self.page.locator(
            "tr",
            has_text=name
        )

        return row.locator(
            "td"
        ).first.text_content()

    def update_student(
        self,
        student_id,
        name,
        age,
        marks
    ):

        self.page.goto(
            f"{self.BASE_URL}/students/update/{student_id}"
        )

        self.page.locator("#name").fill(name)
        self.page.locator("#age").fill(str(age))
        self.page.locator("#marks").fill(str(marks))

        self.page.locator(
            "#update-student-button"
        ).click()

    def delete_student(self, name):

        self.open_students()

        row = self.page.locator(
            "tr",
            has_text=name
        )

        row.locator(
            ".delete-button"
        ).click()

    def is_student_present(self, name):

        self.open_students()

        return name in self.page.content()

    def is_students_table_visible(self):

        return self.page.locator(
            "#students-table"
        ).is_visible()