class Bank:
    def __init__(self):
        self.__balance = 0

    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    

b = Bank()

b.deposite(1000)

print(b.get_balance())
