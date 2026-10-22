from flask import Flask, render_template, request, redirect
from database import get_db_connection
from health_ai import analyze_health

# PyWebView
import webview
import threading
import time

app = Flask(__name__)


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# REGISTER
# =========================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        password = request.form["password"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO users
        (name, password, age, gender, phone)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (name, password, age, gender, phone)
        )

        connection.commit()

        cursor.close()
        connection.close()

        return redirect("/login")

    return render_template("register.html")


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        name = request.form["name"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(buffered=True)

        query = """
        SELECT id, name, password
        FROM users
        WHERE name = %s AND password = %s
        LIMIT 1
        """

        cursor.execute(
            query,
            (name, password)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            return redirect("/dashboard")

        return "Invalid Name or Password ❌"

    return render_template("login.html")


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# =========================================================
# HEALTH ASSESSMENT
# =========================================================

@app.route("/assessment")
def assessment():
    return render_template("assessment.html")


# =========================================================
# HEALTH ANALYSIS
# =========================================================

@app.route("/analyze", methods=["POST"])
def analyze():

    # -----------------------------------------------------
    # Personal Details
    # -----------------------------------------------------

    age = int(request.form["age"])

    gender = request.form["gender"]

    height = float(request.form["height"])

    weight = float(request.form["weight"])


    # -----------------------------------------------------
    # Lifestyle Details
    # -----------------------------------------------------

    water = float(
        request.form.get("water", 0)
    )

    sleep = float(
        request.form.get("sleep", 0)
    )

    exercise = int(
        request.form.get("exercise", 0)
    )

    food_habit = request.form.get(
        "food_habit",
        "average"
    )

    stress_level = request.form.get(
        "stress_level",
        "medium"
    )


    # -----------------------------------------------------
    # Symptoms
    # -----------------------------------------------------

    symptoms = request.form.getlist(
        "symptoms"
    )


    # -----------------------------------------------------
    # AI Health Analysis
    # -----------------------------------------------------

    bmi, bmi_status, recommendations = analyze_health(

        age,

        gender,

        height,

        weight,

        symptoms,

        water,

        sleep,

        exercise,

        food_habit,

        stress_level
    )


    # -----------------------------------------------------
    # Convert Recommendations to Text
    # -----------------------------------------------------

    recommendation_text = " ".join(
        recommendations
    )


    # -----------------------------------------------------
    # Save Result to MySQL
    # -----------------------------------------------------

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO health_assessments
    (
        user_age,
        gender,
        height,
        weight,
        bmi,
        bmi_status,
        symptoms,
        recommendations
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(

        query,

        (
            age,

            gender,

            height,

            weight,

            bmi,

            bmi_status,

            ", ".join(symptoms),

            recommendation_text
        )
    )


    connection.commit()

    cursor.close()

    connection.close()


    # -----------------------------------------------------
    # Show Result Page
    # -----------------------------------------------------

    return render_template(

        "result.html",

        bmi=round(bmi, 2),

        bmi_status=bmi_status,

        recommendations=recommendations,

        symptoms=symptoms,

        water=water,

        sleep=sleep,

        exercise=exercise,

        food_habit=food_habit,

        stress_level=stress_level
    )


# =========================================================
# RESULT
# =========================================================

@app.route("/result")
def result():

    return render_template(
        "result.html"
    )


# =========================================================
# HISTORY
# =========================================================

@app.route("/history")
def history():

    connection = get_db_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    query = """
    SELECT *
    FROM health_assessments
    ORDER BY created_at DESC
    """

    cursor.execute(query)

    assessments = cursor.fetchall()

    cursor.close()

    connection.close()

    return render_template(

        "history.html",

        assessments=assessments
    )


# =========================================================
# START FLASK SERVER
# =========================================================

def run_flask():

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=False,

        use_reloader=False
    )


# =========================================================
# START DESKTOP APPLICATION
# =========================================================

if __name__ == "__main__":

    # Start Flask in background
    flask_thread = threading.Thread(
        target=run_flask
    )

    flask_thread.daemon = True

    flask_thread.start()


    # Give Flask a moment to start
    time.sleep(1)


    # Create Desktop Application Window
    webview.create_window(

        "AI Based Preventive Health Care Recommendation System",

        "http://127.0.0.1:5000/",

        width=1200,

        height=800,

        resizable=True,

        text_select=True
    )


    # Start PyWebView
    webview.start()