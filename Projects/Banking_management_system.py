"""Banking Management System"""

transactions = []


# create_account()

def create_account():
    print("===== Create Account Form =====")

    name = input("Enter Your Name: ")
    father_name = input("Enter Your Father Name: ")
    mother_name = input("Enter Your Mother Name: ")

    age = int(input("Enter Your Age: "))
    gender = input("Enter Your Gender: ")

    address = input("Enter Your Address: ")

    aadhar_no = input("Enter Your Aadhar Number: ")
    pan_no = input("Enter Your PAN Number: ")

    mobile_no = input("Enter Your Mobile Number: ")
    email = input("Enter Your Email ID: ")

    account_type = input("Enter Account Type (Saving/Current): ")

    opening_balance = float(input("Enter Opening Balance: "))

    pin = int(input("Create 4 Digit PIN: "))

    
    # Dictionary
    account = {
        "name": name,
        "father_name": father_name,
        "mother_name": mother_name,
        "age": age,
        "gender": gender,
        "address": address,
        "aadhar_no": aadhar_no,
        "pan_no": pan_no,
        "mobile_no": mobile_no,
        "email": email,
        "account_type": account_type,
        "balance": opening_balance,
        "pin": pin
    }

    return account


# deposit()

def deposit(account, amount):

    if amount > 0:
        account["balance"] += amount
        transactions.append(f"Deposited: {amount}")

        print(f"{amount} deposited successfully.")

    else:
        print("Deposit amount should be greater than 0.")


# withdraw()

def withdraw(account, amount):

    if amount > account["balance"]:
        print("Insufficient balance.")

    elif amount > 0:
        account["balance"] -= amount
        transactions.append(f"Withdraw: {amount}")

        print("Withdraw amount successfully.")

    else:
        print("Withdraw amount should be greater than 0.")


# check_balance()

def check_balance(account):

    print(f"Your current balance is: {account['balance']}")


# transaction_history()

def transaction_history():

    if not transactions:
        print("No transaction yet.")

    else:
        for transaction in transactions:
            print(transaction)



# Main Program

account = create_account()

deposit(account, 500)

withdraw(account, 200)

check_balance(account)

transaction_history()