def calculator(): # def is a keyword used to define a function.
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Enter choice")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divided")

    choice = input("Enter Choice (1/2/3/4):")

    if choice == "1":
        print(f"{num1} + {num2} = {num1+num2}")
    elif choice == "2":
        print(f"{num1} - {num2} = {num1-num2}")
    elif choice == "3":
        print(f"{num1} * {num2} = {num1*num2}")
    elif choice == "4":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1/ num2}")
        else:
            print(f"num2 is not equal to 0")
    else:
        print("Invaild number")

calculator()