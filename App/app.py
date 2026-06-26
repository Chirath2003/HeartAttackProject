from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
import joblib
import pandas as pd
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.secret_key = "ehr_secret_key"


# Database Connection
def get_db_connection():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    DB_PATH = os.path.join(
        BASE_DIR,
        "database",
        "ehr.db"
    )

    print("Database Path:", DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


# Login Page
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()

        user = conn.execute(
            """
            SELECT *
            FROM users
            WHERE username = ?
            """,
            (username,)
        ).fetchone()

        if user and check_password_hash(
            user["password"],
            password
        ):

            # Save session
            session["username"] = user["username"]
            session["role"] = user["role"]

            # Save login log
            conn.execute(
                """
                INSERT INTO audit_logs
                (username, role, action)
                VALUES (?, ?, ?)
                """,
                (
                    user["username"],
                    user["role"],
                    "User Login"
                )
            )

            conn.commit()
            conn.close()

            return redirect(url_for("dashboard"))

        conn.close()

        return "Invalid Username or Password"

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"],
        role=session["role"]
    )

# add Patient
@app.route("/add_patient", methods=["GET", "POST"])
def add_patient():

    if "username" not in session:
        return redirect(url_for("login"))
    
    if session["role"] not in ["Admin", "Doctor"]:
        return "Access Denied"

    if request.method == "POST":

        patient_name = request.form["patient_name"]
        age = request.form["age"]
        gender = request.form["gender"]
        hypertension = request.form["hypertension"]
        diabetes = request.form["diabetes"]
        cholesterol_level = request.form["cholesterol_level"]

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO patients
            (
                patient_name,
                age,
                gender,
                hypertension,
                diabetes,
                cholesterol_level,
                created_by
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                patient_name,
                age,
                gender,
                hypertension,
                diabetes,
                cholesterol_level,
                session["username"]
            )
        )

        conn.commit()
        conn.close()

        return "Patient Saved Successfully"

    return render_template("add_patient.html")

#View Patient
@app.route("/patients")
def patients():

    if "username" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    patients = conn.execute(
        "SELECT * FROM patients ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "patients.html",
        patients=patients
    )
#prediction
@app.route("/predict", methods=["GET", "POST"])
def predict():

    if "username" not in session:
        return redirect(url_for("login"))
    
    if session["role"] not in ["Admin", "Doctor"]:
        return "Access Denied"

    if request.method == "POST":

        age = int(request.form["age"])
        gender = int(request.form["gender"])
        hypertension = int(request.form["hypertension"])
        diabetes = int(request.form["diabetes"])
        cholesterol_level = float(request.form["cholesterol_level"])
        obesity = int(request.form["obesity"])
        family_history = int(request.form["family_history"])
        stress_level = int(request.form["stress_level"])
        sleep_hours = float(request.form["sleep_hours"])
        blood_pressure_systolic = int(request.form["blood_pressure_systolic"])
        blood_pressure_diastolic = int(request.form["blood_pressure_diastolic"])
        previous_heart_disease = int(
            request.form["previous_heart_disease"]
        )

        BASE_DIR = os.path.dirname(
            os.path.abspath(__file__)
        )

        MODEL_PATH = os.path.join(
            BASE_DIR,
            "..",
            "Models",
            "heart_attack_model.pkl"
        )

        model = joblib.load(MODEL_PATH)

        data = pd.DataFrame([{
            "age": age,
            "gender": gender,
            "hypertension": hypertension,
            "diabetes": diabetes,
            "cholesterol_level": cholesterol_level,
            "obesity": obesity,
            "family_history": family_history,
            "stress_level": stress_level,
            "sleep_hours": sleep_hours,
            "blood_pressure_systolic":
                blood_pressure_systolic,
            "blood_pressure_diastolic":
                blood_pressure_diastolic,
            "previous_heart_disease":
                previous_heart_disease
        }])

        prediction = model.predict(data)

        result = (
            "Heart Attack Risk: YES"
            if prediction[0] == 1
            else "Heart Attack Risk: NO"
        )

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO audit_logs
            (username, role, action)
            VALUES (?, ?, ?)
            """,
            (
                session["username"],
                session["role"],
                result
            )
        )

        conn.commit()
        conn.close()

        return render_template(
            "prediction_result.html",
            result=result
        )

    return render_template(
        "prediction.html"
    )

#log page
@app.route("/logs")
def logs():

    if "username" not in session:
        return redirect(url_for("login"))

    if session["role"] != "Admin":
        return "Access Denied"

    conn = get_db_connection()

    logs = conn.execute(
        "SELECT * FROM audit_logs ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "logs.html",
        logs=logs
    )

# Logout
@app.route("/logout")
def logout():

    if "username" in session:

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO audit_logs
            (username, role, action)
            VALUES (?, ?, ?)
            """,
            (
                session["username"],
                session["role"],
                "User Logout"
            )
        )

        conn.commit()
        conn.close()

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)