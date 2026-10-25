from flask import Flask, render_template, request, redirect, url_for
from database import get_connection

app = Flask(__name__)


# -------------------------
# Home Page
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# View All Students
# -------------------------
@app.route("/students")
def view_students():
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT id, name, age, marks
            FROM students
            ORDER BY id
        """)
        students = cur.fetchall()

    finally:
        cur.close()
        conn.close()

    return render_template(
        "students.html",
        students=students
    )


# -------------------------
# Add Student
# -------------------------
@app.route("/students/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        marks = request.form.get("marks", "").strip()

        if not name or not age or not marks:
            return render_template(
                "add_student.html",
                error="Please fill in all fields."
            )

        try:
            age = int(age)
            marks = int(marks)

        except ValueError:
            return render_template(
                "add_student.html",
                error="Age and marks must be numbers."
            )

        if age < 0 or not 0 <= marks <= 100:
            return render_template(
                "add_student.html",
                error="Age cannot be negative and marks must be between 0 and 100."
            )

        conn = get_connection()
        cur = conn.cursor()

        try:
            cur.execute("""
                INSERT INTO students (name, age, marks)
                VALUES (%s, %s, %s)
            """, (name, age, marks))

            conn.commit()

        finally:
            cur.close()
            conn.close()

        return redirect(url_for("view_students"))

    return render_template("add_student.html")


# -------------------------
# Search Page
# -------------------------
@app.route("/students/search", methods=["GET"])
def search_page():
    return render_template(
        "search.html",
        results=None
    )


# -------------------------
# Search Student by ID or Name
# -------------------------
@app.route("/students/search-result", methods=["POST"])
def search_result():

    search = request.form.get("search", "").strip()

    if not search:
        return render_template(
            "search.html",
            results=[],
            error="Please enter a student ID or name."
        )

    conn = get_connection()
    cur = conn.cursor()

    try:
        if search.isdigit():

            search_id = int(search)

            cur.execute("""
                SELECT id, name, age, marks
                FROM students
                WHERE id = %s
                ORDER BY id
            """, (search_id,))

        else:

            search_text = search.lower()

            cur.execute("""
                SELECT id, name, age, marks
                FROM students
                WHERE LOWER(TRIM(name)) LIKE %s
                ORDER BY id
            """, (f"%{search_text}%",))

        results = cur.fetchall()

    finally:
        cur.close()
        conn.close()

    return render_template(
        "search.html",
        results=results
    )


# -------------------------
# Update Student
# -------------------------
@app.route(
    "/students/update/<int:student_id>",
    methods=["GET", "POST"]
)
def update_student(student_id):

    conn = get_connection()
    cur = conn.cursor()

    try:
        if request.method == "POST":

            name = request.form.get("name", "").strip()
            age = request.form.get("age", "").strip()
            marks = request.form.get("marks", "").strip()

            if not name or not age or not marks:
                cur.execute("""
                    SELECT id, name, age, marks
                    FROM students
                    WHERE id = %s
                """, (student_id,))

                student = cur.fetchone()

                if student is None:
                    return "Student not found.", 404

                return render_template(
                    "update_student.html",
                    student=student,
                    error="Please fill in all fields."
                )

            try:
                age = int(age)
                marks = int(marks)

            except ValueError:
                cur.execute("""
                    SELECT id, name, age, marks
                    FROM students
                    WHERE id = %s
                """, (student_id,))

                student = cur.fetchone()

                if student is None:
                    return "Student not found.", 404

                return render_template(
                    "update_student.html",
                    student=student,
                    error="Age and marks must be numbers."
                )

            if age < 0 or not 0 <= marks <= 100:
                cur.execute("""
                    SELECT id, name, age, marks
                    FROM students
                    WHERE id = %s
                """, (student_id,))

                student = cur.fetchone()

                if student is None:
                    return "Student not found.", 404

                return render_template(
                    "update_student.html",
                    student=student,
                    error="Age cannot be negative and marks must be between 0 and 100."
                )

            cur.execute("""
                UPDATE students
                SET name = %s, age = %s, marks = %s
                WHERE id = %s
            """, (name, age, marks, student_id))

            if cur.rowcount == 0:
                conn.rollback()
                return "Student not found.", 404

            conn.commit()

            return redirect(url_for("view_students"))

        cur.execute("""
            SELECT id, name, age, marks
            FROM students
            WHERE id = %s
        """, (student_id,))

        student = cur.fetchone()

        if student is None:
            return "Student not found.", 404

    finally:
        cur.close()
        conn.close()

    return render_template(
        "update_student.html",
        student=student
    )


# -------------------------
# Delete Student
# -------------------------
@app.route(
    "/students/delete/<int:student_id>",
    methods=["POST"]
)
def delete_student(student_id):

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            DELETE FROM students
            WHERE id = %s
        """, (student_id,))

        conn.commit()

    finally:
        cur.close()
        conn.close()

    return redirect(url_for("view_students"))


# -------------------------
# Run Flask Application
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
