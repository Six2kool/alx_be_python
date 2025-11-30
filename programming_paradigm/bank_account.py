# bank_account.py
class BankAccount:
    def __init__(self, starting_money=0):
        # This is the key fix! Store as float, not int
        self.account_balance = float(starting_money)

    def deposit(self, amount):
        self.account_balance += float(amount)   # make sure we add as float

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

