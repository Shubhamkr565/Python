import random  # Import random module to generate random numbers

print("Welcome to the Number Guessing Game!\n")

def start():
    print("I'm thinking of a number between 1 and 100\n")
    computer_choice = random.randint(1, 100)  # Random number between 1 and 100
    
    choice = input("Choose a difficulty. type 'easy' or 'hard': ")  # Difficulty selection
    if choice == "easy":
        print("You have 10 moves: ")
        i = 10  # 10 guesses for easy mode
    elif choice == "hard":
        print("You have 5 moves: ")
        i = 5  # 5 guesses for hard mode
    else:
        return  # Exit if invalid input

    # Main game loop
    while i >= 1:
        user_choice = int(input("Make a guess: "))
        if user_choice == computer_choice:
            print("Yes!!!")
            return  # End game if guessed correctly
        elif user_choice > computer_choice:
            print("Too high.")
        else:
            print("Too low.")
        
        i -= 1  # Reduce moves
        print(f"You have only {i} moves left.")
    
    print("Out of moves, you lost!!!!")  # If user runs out of moves

start()  # Start the game
