# Real-life flow (like opening a bank account)

# Step 1: Open a new Account (Class & Object)
# Go to union bank -> Create Account

class CreateAC:
    def __init__(self, name, adharNo, phoneNo, balance = 0):
        self.name = name
        self.adharNo = adharNo
        self.phoneNo = phoneNo
        self.balance = balance


    def Deposit(self):
    # def __init__(self, name, balance):
        depositAmount = int(input("Enter deposite Amount: "))
        self.balance += depositAmount
        print(f"You deposit Amount is : {depositAmount}, Current balance: {self.balance}")


    def Withdrow(self):
        WithdrowAmount = int(input("Enter Withdrow Amount: "))
        
        if WithdrowAmount > self.balance:
            print(f"Insufficient balance! Availabel: ",self.balance)
        elif WithdrowAmount <= 0:
            print("Invalid Amount!")
        else:
            self.balance -= WithdrowAmount
            print(f"Withdrow Amount: {WithdrowAmount}")
            print(f"Remaining balance: {self.balance}")


acc1 = CreateAC("Shubham", 42423, 12345)

print(f"Account Created for: ", acc1.name)
print(f"AdharNo: ",acc1.adharNo)
print(f"Phone Number: ",acc1.phoneNo)
print(f"balance: ", acc1.balance)

acc1.Deposit()

acc1.Withdrow()