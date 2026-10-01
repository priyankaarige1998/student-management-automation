@app.route("/students/search", methods=["GET"])
def search_page():
    return render_template(
        "search.html",
        results=None
    )


@app.route("/students/search-result", methods=["POST"])
def search_result():

    search = request.form.get("search", "").strip()

    results = []

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name, age, marks
        FROM students
        ORDER BY id
    """)

    students = cur.fetchall()

    cur.close()
    conn.close()

    if search.isdigit():

        search_id = int(search)

        results = [
            student
            for student in students
            if student[0] == search_id
        ]

    else:

        search_text = search.lower()

        results = [
            student
            for student in students
            if search_text in student[1].strip().lower()
        ]

    return render_template(
        "search.html",
        results=results
    )