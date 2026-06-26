import sqlite3

from werkzeug.security import generate_password_hash

conn = sqlite3.connect(
    "App/database/ehr.db"
)

cursor = conn.cursor()

users = [
    ("admin", generate_password_hash("admin123")),
    ("doctor", generate_password_hash("doctor123")),
    ("nurse", generate_password_hash("nurse123"))
]

for username, password in users:

    cursor.execute(
        """
        UPDATE users
        SET password = ?
        WHERE username = ?
        """,
        (password, username)
    )

conn.commit()
conn.close()

print("Passwords Hashed Successfully")