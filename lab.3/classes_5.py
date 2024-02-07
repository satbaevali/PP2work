class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} tenge. New balance: {self.balance} tenge")
        else:
            print("Amount to deposit must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} tenge. New balance: {self.balance} tenge")
            else:
                print("Insufficient funds")
        else:
            print("Amount to withdraw must be positive")

owner = str(input("Enter owner name: "))
balance = int(input("Enter initial balance: "))

my_balance = Account(owner, balance)

deposit_amount = int(input("Enter the amount to deposit: "))
my_balance.deposit(deposit_amount)

withdraw_amount = int(input("Enter the amount to withdraw: "))
my_balance.withdraw(withdraw_amount)
