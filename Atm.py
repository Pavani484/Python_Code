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

        new_balance = balance - amount
        cursor.execute("UPDATE users SET balance=%s WHERE username=%s", (new_balance, self.current_user))
        cursor.execute("INSERT INTO history VALUES (%s, %s)", (self.current_user, f"Withdrew {amount}"))
        conn.commit()
        return f"Withdrawn. Balance: {new_balance}"

    def change_pin(self, old_pin, new_pin):
        cursor.execute("SELECT pin FROM users WHERE username=%s", (self.current_user,))
        current_pin = cursor.fetchone()[0]

        if old_pin != current_pin:
            return "Wrong old PIN"

        if len(str(new_pin)) == 4:
            cursor.execute("UPDATE users SET pin=%s WHERE username=%s", (new_pin, self.current_user))
            conn.commit()
            return "PIN changed"
        return "Invalid PIN"

    def get_history(self):
        cursor.execute("SELECT action FROM history WHERE username=%s", (self.current_user,))
        return [h[0] for h in cursor.fetchall()]

    def logout(self):
        self.current_user = None


atm = ATM()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("ATM System")
root.geometry("400x500")
root.configure(bg="#1e1e2f")

def clear():
    for w in root.winfo_children():
        w.destroy()


# -------- LOGIN SCREEN --------
def login_screen():
    clear()

    tk.Label(root, text="ATM Login", font=("Arial", 18, "bold"),
             bg="#1e1e2f", fg="white").pack(pady=10)

    tk.Label(root, text="Username", bg="#1e1e2f", fg="white").pack()
    user_entry = tk.Entry(root)
    user_entry.pack()

    tk.Label(root, text="PIN", bg="#1e1e2f", fg="white").pack()
    pin_entry = tk.Entry(root, show="*")
    pin_entry.pack()

    output = tk.Label(root, text="", bg="#1e1e2f", fg="yellow")
    output.pack()

    def handle_login():
        try:
            msg = atm.login(user_entry.get(), int(pin_entry.get()))
            output.config(text=msg)
            if msg == "Login successful":
                dashboard()
        except:
            output.config(text="Invalid input")

    tk.Button(root, text="Login", bg="#4CAF50", fg="white",
              width=15, command=handle_login).pack(pady=10)

    tk.Button(root, text="Register", bg="blue", fg="white",
              command=register_screen).pack()


# -------- REGISTER SCREEN --------
def register_screen():
    clear()

    tk.Label(root, text="Create Account", font=("Arial", 16, "bold"),
             bg="#1e1e2f", fg="white").pack(pady=10)

    tk.Label(root, text="Username", bg="#1e1e2f", fg="white").pack()
    user_entry = tk.Entry(root)
    user_entry.pack()

    tk.Label(root, text="PIN", bg="#1e1e2f", fg="white").pack()
    pin_entry = tk.Entry(root)
    pin_entry.pack()

    tk.Label(root, text="Initial Balance", bg="#1e1e2f", fg="white").pack()
    bal_entry = tk.Entry(root)
    bal_entry.pack()

    output = tk.Label(root, text="", bg="#1e1e2f", fg="yellow")
    output.pack()

    def handle_register():
        try:
            msg = atm.register(
                user_entry.get(),
                int(pin_entry.get()),
                int(bal_entry.get())
            )
            output.config(text=msg)
        except:
            output.config(text="Invalid input")

    tk.Button(root, text="Create Account", bg="green", fg="white",
              command=handle_register).pack(pady=10)

    tk.Button(root, text="Back", command=login_screen).pack()


# -------- DASHBOARD --------
def dashboard():
    clear()

    tk.Label(root, text=f"Welcome {atm.current_user}",
             font=("Arial", 14, "bold"),
             bg="#1e1e2f", fg="white").pack(pady=10)

    output = tk.Label(root, text="", bg="#1e1e2f", fg="cyan")
    output.pack()

    tk.Label(root, text="Amount", bg="#1e1e2f", fg="white").pack()
    amt_entry = tk.Entry(root)
    amt_entry.pack()

    def show_balance():
        output.config(text=f"Balance: {atm.get_balance()}")

    def deposit():
        try:
            output.config(text=atm.deposit(int(amt_entry.get())))
        except:
            output.config(text="Invalid input")

    def withdraw():
        try:
            output.config(text=atm.withdraw(int(amt_entry.get())))
        except:
            output.config(text="Invalid input")

    def change_pin():
        try:
            old = int(old_pin.get())
            new = int(new_pin.get())
            output.config(text=atm.change_pin(old, new))
        except:
            output.config(text="Invalid input")

    def show_history():
        hist = atm.get_history()
        output.config(text="\n".join(hist) if hist else "No transactions")

    def logout():
        atm.logout()
        login_screen()

    tk.Button(root, text="Check Balance", command=show_balance).pack(pady=5)
    tk.Button(root, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(root, text="Withdraw", command=withdraw).pack(pady=5)

    tk.Label(root, text="Old PIN", bg="#1e1e2f", fg="white").pack()
    old_pin = tk.Entry(root)
    old_pin.pack()

    tk.Label(root, text="New PIN", bg="#1e1e2f", fg="white").pack()
    new_pin = tk.Entry(root)
    new_pin.pack()

    tk.Button(root, text="Change PIN", command=change_pin).pack(pady=5)
    tk.Button(root, text="History", command=show_history).pack(pady=5)
    tk.Button(root, text="Logout", bg="red", fg="white", command=logout).pack(pady=10)


# Start App
login_screen()
root.mainloop()