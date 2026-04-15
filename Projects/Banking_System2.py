import tkinter as tk
from tkinter import messagebox

# Initialize balance and transactions₹
balance = 0.0
transactions = []

# Functions
def check_balance():
    balance_label.config(text=f"Balance: ₹{balance}")

def deposit():
    global balance
    try:
        amount = float(entry.get())
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: {amount}")
            messagebox.showinfo("Success", f"{amount} deposited successfully!")
            check_balance()
        else:
            messagebox.showerror("Error", "Amount must be greater than 0")
    except:
        messagebox.showerror("Error", "Enter valid number")

def withdraw():
    global balance
    try:
        amount = float(entry.get())
        if amount > balance:
            messagebox.showerror("Error", "Insufficient balance")
        elif amount > 0:
            balance -= amount
            transactions.append(f"Withdrawn: {amount}")
            messagebox.showinfo("Success", f"{amount} withdrawn successfully!")
            check_balance()
        else:
            messagebox.showerror("Error", "Amount must be greater than 0")
    except:
        messagebox.showerror("Error", "Enter valid number")

def show_transactions():
    if not transactions:
        messagebox.showinfo("Transactions", "No transactions yet!")
    else:
        messagebox.showinfo("Transactions", "\n".join(transactions))

# GUI Window
root = tk.Tk()
root.title("Banking System GUI")
root.geometry("350x300")

# Widgets
tk.Label(root, text="Enter Amount:", font=("Arial", 12)).pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Deposit", command=deposit).pack(pady=5)
tk.Button(root, text="Withdraw", command=withdraw).pack(pady=5)
tk.Button(root, text="Check Balance", command=check_balance).pack(pady=5)
tk.Button(root, text="Transaction History", command=show_transactions).pack(pady=5)

balance_label = tk.Label(root, text="Balance: ₹0.0", font=("Arial", 12))
balance_label.pack(pady=10)

# Run GUI
root.mainloop()