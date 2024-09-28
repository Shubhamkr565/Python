def check_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It's is a prime number.")
    else:
        print("It's is not a prime number.")

number = int(input("Enter any number to check prime or not:"))
check_prime(number)