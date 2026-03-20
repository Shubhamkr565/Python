class ATM:

    def __init__(self):
        self.balance = 10000    #initial balance

    def start(self):
        while True:
            print("\nWelcome to ATM ")
            print("Insert Your Card ")

            pin = int(input("Enter Your PIN: "))
            if pin == 1234:
                print("\nChoose Options")
                print("1: Check Balance ")
                print("2. Withdrow ")
                print("3. Exit")

                choice =int(input("Enter Your Choice: "))
                if choice == 1:
                    print(f"\nYour balance is {self.balance}\n")
                elif choice == 2:
                    amount = int(input("\nEnter withdrow amount: "))
                    if amount > self.balance:
                        print("\nInsufficient Balance!")
                    elif amount <= 0:
                        print("\nInvalid amount!")
                    else:
                        self.balance -= amount
                        print(f"You withdrow {amount}")
                        print(f"Remaining balance: {self.balance}")
                elif choice == 3:
                    print("Thank you! Visit again")
                    break
                else:
                    print("Invalid Input")
            else:
                print("\nWrong PIN\n")
                print("Thank you! Visit again")
                break

atm = ATM()
atm.start()