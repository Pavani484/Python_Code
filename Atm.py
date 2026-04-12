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

        if pin == user[1]:
            self.current_user = username
            cursor.execute("UPDATE users SET attempts=0 WHERE username=%s", (username,))
            conn.commit()
            return "Login successful"
        else:
            attempts = user[3] + 1
            cursor.execute("UPDATE users SET attempts=%s WHERE username=%s", (attempts, username))

            if attempts >= 3:
                cursor.execute("UPDATE users SET locked=1 WHERE username=%s", (username,))
                conn.commit()
                return "Account locked"

            conn.commit()
            return "Incorrect PIN"

    def register(self, username, pin, balance):
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            return "User already exists"

        if len(str(pin)) != 4:
            return "PIN must be 4 digits"

        cursor.execute(
            "INSERT INTO users (username, pin, balance) VALUES (%s, %s, %s)",
            (username, pin, balance)
        )
        conn.commit()
        return "Account created successfully"

    def get_balance(self):
        cursor.execute("SELECT balance FROM users WHERE username=%s", (self.current_user,))
        return cursor.fetchone()[0]

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"

        new_balance = self.get_balance() + amount
        cursor.execute("UPDATE users SET balance=%s WHERE username=%s", (new_balance, self.current_user))
        cursor.execute("INSERT INTO history VALUES (%s, %s)", (self.current_user, f"Deposited {amount}"))
        conn.commit()
        return "Deposit successful"

    def withdraw(self, amount):
        balance = self.get_balance()

        if amount <= 0:
            return "Invalid amount"
        if amount > 5000:
            return "Limit is 5000"
        if amount > balance:
            return "Insufficient balance"

