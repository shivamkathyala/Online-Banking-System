# online banking system using oops

# main/super class
class Account:
    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
        print(f"Bank account created. {self.name} your current balance is {balance}")

    # deposit method

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} Deposited {amount} Rs. Now the current balance is {self.balance} Rs.")

    # withdraw method

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount
            print(f"{self.name} withdraw {amount} Rs. Now the current balance is {self.balance} Rs.")
        else:
            print("You don't have enough funds to withdraw.")

# now creating sub/child class of Account class

class SavingsAccount(Account):
    def __init__(self, name, accountNumber, balance, interestRate):
        super().__init__(name, accountNumber, balance)
        self.interestRate = interestRate

# add interest method

    def addInterest(self):
        interest = self.balance * self.interestRate
        self.deposit(interest)

account1 = Account("Shivam Thakur", "123456789", 1000)
account1.deposit(500)
account1.withdraw(800)