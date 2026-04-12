import tkinter as tk
import mysql.connector

# ---------------- MYSQL CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pavani@9312",
    database="atm_db"
)
cursor = conn.cursor()


# ---------------- ATM LOGIC ----------------
class ATM:
    def __init__(self):
        self.current_user = None

    def login(self, username, pin):
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if not user:
            return "User not found"

        if user[4]:
            return "Account locked"
