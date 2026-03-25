class Password:
    def __init__(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password
    
user = Password("1234")

print(user.check_password("1234"))



# ✅ 1. Check for Private Variables (Data Hiding)
# 👉 Rule:

# __variable → Encapsulation
# variable → Not encapsulation


# ✅ 2. Check Access Through Methods Only

# def deposit(self, amount):
#     self.__balance += amount

# 👉 Data is controlled using methods → ✅ Encapsulation


# ✅ 3. Look for Getter and Setter Methods

# def get_balance(self):
#     return self.__balance

# ✔ Optional setter:

# def set_balance(self, amount):
#     self.__balance = amount

# 👉 Getter/Setter present → strong encapsulation

# 👉 Encapsulation =
# Private Data + Controlled Access + Protection

# If your class has:

# __variable ✔
# methods to access ✔
# no direct access ✔

# 👉 Then YES, it is Encapsulation ✅