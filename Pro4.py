class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number  # Private attribute
        self.__balance = 0.0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: {amount:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance


# Example usage
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("123456789")

    # Deposit money
    account.deposit(500.00)
    print(f"Current Balance: {account.get_balance():.2f}")

    # Withdraw money
    account.withdraw(200.00)
    print(f"Current Balance: {account.get_balance():.2f}")

    # Attempt to withdraw more than the balance
    account.withdraw(400.00)
    print(f"Current Balance: {account.get_balance():.2f}")

    # Attempt to deposit a negative amount
    account.deposit(-50.00)
    print(f"Current Balance: {account.get_balance():.2f}")
