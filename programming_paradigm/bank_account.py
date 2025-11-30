class BankAccount:
    def __init__(self, starting_money=0):
        self.account_balance = starting_money   # this is private money!

    def deposit(self, amount):
        self.account_balance += amount
        # no need to return anything, just add the money

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True                     # success!
        else:
            return False                    # not enough money :(

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")