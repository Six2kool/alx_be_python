import sys
from bank_account import BankAccount

def main():
    # You start with $100 pocket money (you can change this number to test)
    account = BankAccount(100)

    # If the user forgot to type a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands:")
        print("   deposit:50    → put $50 in")
        print("   withdraw:20   → take $20 out")
        print("   display       → check balance")
        return

    # Example: user types  deposit:75
    command_part = sys.argv[1]          # "deposit:75" or "display"
    if ":" in command_part:
        command, amount_str = command_part.split(":")
        amount = float(amount_str)
    else:
        command = command_part
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds. You're broke lol")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command. Try again!")

if __name__ == "__main__":
    main()