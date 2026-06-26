import sqlite3

# Create database connection
conn = sqlite3.connect("ehr.db")

cursor = conn.cursor()

# =====================================================
# USERS TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# =====================================================
# PATIENTS TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,

    hypertension INTEGER,
    diabetes INTEGER,
    cholesterol_level REAL,
    obesity INTEGER,
    waist_circumference REAL,
    family_history INTEGER,

    smoking_status TEXT,
    physical_activity TEXT,
    dietary_habits TEXT,
    stress_level TEXT,

    sleep_hours REAL,

    blood_pressure_systolic INTEGER,
    blood_pressure_diastolic INTEGER,

    fasting_blood_sugar REAL,

    cholesterol_hdl REAL,
    cholesterol_ldl REAL,

    triglycerides REAL,

    previous_heart_disease INTEGER,

    prediction TEXT,

    created_by TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# =====================================================
# PREDICTION HISTORY TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_id INTEGER,
    prediction TEXT,

    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(patient_id)
    REFERENCES patients(id)
)
""")

# =====================================================
# AUDIT LOG TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS audit_logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,
    role TEXT,
    action TEXT,

    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# =====================================================
# DEFAULT USERS
# =====================================================

cursor.execute("""
INSERT OR IGNORE INTO users
(username,password,role)
VALUES
('admin','admin123','Admin')
""")

cursor.execute("""
INSERT OR IGNORE INTO users
(username,password,role)
VALUES
('doctor','doctor123','Doctor')
""")

cursor.execute("""
INSERT OR IGNORE INTO users
(username,password,role)
VALUES
('nurse','nurse123','Nurse')
""")

# =====================================================
# SAVE
# =====================================================

conn.commit()
conn.close()

print("Database Created Successfully!")