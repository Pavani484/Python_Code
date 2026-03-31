class ATM:
    def __init__(self,pin, balance):
        self.__pin = pin
        self.__balance = balance
        self.is_logged_in = False
        self.attempts = 0
        self.is_locked = False
    def login(self, pin):
        if self.is_locked:
            print("Account is locked. Try later.")
            return

        if pin == self.__pin:
            self.is_logged_in = True
            self.attempts = 0
            print("Login successful")
        else:
            self.attempts += 1
            print("Incorrect PIN")

            if self.attempts >= 3:
                self.is_locked = True
                print("Account locked due to 3 failed attempts")

    def logout(self):
        self.is_logged_in = False
        print("Logged out")
    def check_balance(self):
        if self.is_logged_in:
            print(self.__balance)
            print("balance check sucessful")
        else:
            print("login first")

    def deposit(self, amount):
        if not self.is_logged_in:
            print("Login first")
            return

        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if not self.is_logged_in:
            print("login first")
        elif amount<=0:
            print("invalid amount")
        elif amount>5000:
            print("maximum withdrawal limit is 5000")
        elif amount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= amount
            print("withdraw successful")
            print("Remaining balance:", self.__balance)
    def change_pin(self, old_pin, new_pin):
        if self.is_logged_in:
            if old_pin == self.__pin:
                if len(str(new_pin)) == 4:
                    self.__pin = new_pin
                    print("PIN changed successfully")
                else:
                    print("New PIN must be 4 digits")
            else:
                print("Incorrect old PIN")
        else:
            print("Login first")



atm = ATM(1234, 10000)

# ❌ Try without login
atm.withdraw(500)        # Login first
atm.check_balance()      # Login first

# ❌ Wrong PIN attempts
atm.login(1111)          # Incorrect PIN
atm.login(2222)          # Incorrect PIN

# ✅ Correct login
atm.login(1234)          # Login successful

# ✅ After login
atm.check_balance()      # Show balance

atm.withdraw(6000)       # Exceeds limit
atm.withdraw(500)        # Success

atm.deposit(1000)        # Deposit success
atm.check_balance()      # Updated balance

# 🔐 Change PIN
atm.change_pin(1234, 5678)   # Change PIN

# 🔓 Logout (if you implemented)
atm.logout()

# ❌ Try old PIN
atm.login(1234)          # Incorrect PIN

# ✅ Login with new PIN
atm.login(5678)          # Login successful
atm.check_balance()
atm.login(1111)
atm.login(2222)
atm.login(3333)
atm.login(1234)