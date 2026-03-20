# child inherits from Parent

# parent
class BankAccount:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(f"\nAccount Holder name : {self.name}")
        print(f"Current Balance: {self.balance}")


# child
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05 # 5% interest
        self.balance += interest
        print(f"Interest Added: {interest}")


# create Object

acc1 = SavingsAccount("Shubham", 10000)

acc1.show_balance()

acc1.add_interest()

acc1.show_balance()