class Account:
    def __init__(self, acc_no, name):
        self.acc_no = acc_no
        self.name = name
        self.__balance = 0
        self.history = []

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.__balance += amount
        self.history.append(f"Deposited {amount} | Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if amount > self.__balance:
            raise ValueError("Not enough balance.")
        self.__balance -= amount
        self.history.append(f"Withdrawn {amount} | Balance: {self.__balance}")

    def show_history(self):
        if len(self.history) == 0:
            print("No transactions yet.")
            return
        for t in self.history:
            print("-", t)

class SavingsAccount(Account):
    MIN_BALANCE = 500

    def withdraw(self, amount):
        if self.get_balance() - amount < self.MIN_BALANCE:
            raise ValueError(f"Savings account must keep a minimum balance of {self.MIN_BALANCE}.")
        super().withdraw(amount)

def get_number(message):
    try:
        return int(input(message))
    except ValueError:
        print("Please enter a valid number.")
        return None


def find_account(accounts):
    acc_no = get_number("Enter account number: ")
    if acc_no is None:
        return None
    if acc_no not in accounts:
        print("Account not found.")
        return None
    return accounts[acc_no]


def create_account(accounts):
    name = input("Enter account holder name: ")
    print("1. Normal Account")
    print("2. Savings Account (minimum balance 500)")
    kind = input("Choose type (1/2): ")
    acc_no = 1001 + len(accounts)

    if kind == "1":
        accounts[acc_no] = Account(acc_no, name)
    elif kind == "2":
        accounts[acc_no] = SavingsAccount(acc_no, name)
    else:
        print("Invalid account type.")
        return

    print(f"Account created! Your account number is {acc_no}")

def main():
    accounts = {}

    while True:
        print("\n===== Banking System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            acc = find_account(accounts)
            if acc:
                amount = get_number("Enter amount to deposit: ")
                if amount is not None:
                    try:
                        acc.deposit(amount)
                        print("Deposit successful.")
                    except ValueError as e:
                        print("Error:", e)

        elif choice == "3":
            acc = find_account(accounts)
            if acc:
                amount = get_number("Enter amount to withdraw: ")
                if amount is not None:
                    try:
                        acc.withdraw(amount)
                        print("Withdrawal successful.")
                    except ValueError as e:
                        print("Error:", e)

        elif choice == "4":
            acc = find_account(accounts)
            if acc:
                print(f"Account holder: {acc.name}")
                print(f"Balance: {acc.get_balance()}")

        elif choice == "5":
            acc = find_account(accounts)
            if acc:
                acc.show_history()

        elif choice == "6":
            print("Thank you for using the bank. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main()