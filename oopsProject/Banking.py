# Create Account class with 2 attrbutes-balance and account no.
# Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.acc_no = acc_no

    def debit(self,amount):
        self.balance -= amount
        print("Rs. ", amount, " was debited!") 
        print("Totla balance = ",self.get_balance())


    def created(self,amount):
        self.balance += amount
        print("Rs. ", amount, " was created!") 
        print("Totla balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

    

acc1 = Account(10000, 123)
acc1.debit(5000)
acc1.created(2000)
acc1.created(150000)
