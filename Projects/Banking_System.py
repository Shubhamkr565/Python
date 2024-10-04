# Initialize balance to 0.0 and an empty list for transaction history
balance = 0.0
transactions = []

# Function to check and display the current balance
def check_balance():
    print(f"Your current balance is: {balance}")

# Function to deposit a valid amount to the account
def deposit(amount):
    global balance
    if amount > 0:
        balance += amount  # Add the deposit amount to the balance
        transactions.append(f"Deposited: {amount}")  # Record the transaction
        print(f"{amount} deposited successfully!")
    else:
        print("Deposited amount should be greater than 0.")  # Handle invalid deposit

# Function to withdraw a valid amount from the account
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance.")  # Handle case where balance is not enough
    elif amount > 0:
        balance -= amount  # Subtract the withdrawal amount from balance
        transactions.append(f"Withdrawn: {amount}")  # Record the transaction
        print(f"{amount} withdrawn successfully!")
    else:
        print("Withdrawal amount should be greater than 0.")  # Handle invalid withdrawal

# Function to display the transaction history
def transactions_history():
    if not transactions:
        print("No transactions yet!")  # If no transactions, display this message
    else:
        for transaction in transactions:
            print(transaction)  # Print each transaction

# Main menu function for interacting with the user
def main_menu():
    while True:
        print("\n 1. Check Balance")
        print(" 2. Deposit money")
        print(" 3. Withdraw money")
        print(" 4. View Transaction History")
        print(" 5. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        # Call appropriate function based on user's choice
        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)
        elif choice == '4':
            transactions_history()
        elif choice == '5':
            print("Thank you for using the banking system.")
            break  # Exit the loop and program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid choice input

# Run the main menu
main_menu()
