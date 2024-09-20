import random

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','V','W','X','Y','Z']

number = ['0','1','2','3','4','5','6','7','8','9']
symboll = ['!','@','#','$','%','^','&','*','(',')','+']

print("Welcome to PyPassword generator!")

enter_letter = int(input("How many letters would you like in your password?\n"))
enter_number = int(input("How many number would you like ?\n"))
enter_symboll = int(input("How many symboll would you like ?\n"))


password = ""

for char in range(1, enter_letter+1):
    # random_char = random.choice(letter)
    # print(random_char)
    password += random.choice(letter)

for sym in range(1, enter_symboll+1):
    # random_symbol = random.choice(symboll)
    # print(random_symbol)
    password += random.choice(symboll)

for num in range(1, enter_number+1):
    # random_number = random.choice(number)
    # print(random_number)
    password += random.choice(number)



print(password)