# Number Guessing Game with three participants
print("Welcome to the Number Guessing Game!")

# User inputs a number they are thinking of between 1 and 100
user_think = int(input("User: Think of a number between 1 and 100: "))

def start():
    # Another player (or person) inputs an amount (acting as a guess)
    other_person = int(input("Second Person: Enter your number: "))

    # Third person inputs a number for the computer to use
    third_person_input = int(input("Third Person: Enter your number for the computer to use: "))
    
    # The computer will use the third person's number as its guess/input
    computer_guess = third_person_input

    # Calculate the sum of the user's number, the computer's (third person's) number, and the second person's number
    total_sum = user_think + computer_guess + other_person

    # Dividing the total sum by 2
    total_sum = total_sum / 2
    
    # Subtracting the second person's number from the sum
    final_value = total_sum - other_person

    # Display the result based on the input and calculations
    print(f"Based on all the inputs, the final result is: {final_value}")

    # Additionally, showing how much "value" the user has left after the calculation
    print(f"Your remaining value is: {computer_guess / 2}")

# Start the game by calling the start() function
start()
