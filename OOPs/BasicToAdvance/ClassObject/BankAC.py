class BankAC:
    def __init__ (self,balance):
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"Amount Deposite Successfully: {amount}")
        print(f"After deposite Total Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrow successfully.")
            print(f"Current Avalable balace: {self.balance}")
        else:
            print(f"Insuficient Balance\n")
            print(f"Current Balance Avalable only: {self.balance}")


acc = BankAC(50000)

acc.deposite(2000)
acc.withdraw(6000)

    