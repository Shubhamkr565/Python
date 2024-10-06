import random

# Initialize two empty lists to store the user's and the computer's choices
user_list = []
computer_list = []

def start_game():
    # Adding two random numbers (cards) to the user's hand initially
    for i in range(2):
        user_choice = random.randint(1, 10)  # Random card between 1 and 10
        user_list.append(user_choice)
    print(user_list)  # Display user's initial cards

    # Adding two random numbers (cards) to the computer's hand initially
    for i in range(2):
        computer_choice = random.randint(1, 10)  # Random card between 1 and 10
        computer_list.append(computer_choice)

    # Asking the user if they want another card
    more_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # If the user chooses 'y', both user and computer get one more card
    if more_card == "y":
        user_choice = random.randint(1, 10)
        user_list.append(user_choice)

        computer_choice = random.randint(1, 10)
        computer_list.append(computer_choice)

    else:
        # If user chooses 'n', game proceeds without adding more cards
        print("")
    
    # Display the final hands of both the user and the computer
    print(f"Your final hand: {user_list}")
    print(f"Computer's final hand: {computer_list}")
    
    # Check for conditions where both have a total sum of more than 21
    if sum(user_list) > 21 and sum(computer_list) > 21:
        print("Match Draw")
    # Check if the user's total sum exceeds 21 (user loses)
    elif sum(user_list) > 21:
        print("You lose!")
    # Check if the computer's total sum exceeds 21 (user wins)
    elif sum(computer_list) > 21:
        print("You win!")
    # If neither exceeds 21, compare the sums of both lists
    elif sum(user_list) > sum(computer_list):
        print("You Win!")  # User wins if their sum is greater
    elif sum(user_list) < sum(computer_list):
        print("You lose!")  # User loses if their sum is lower
    else:
        print("Match Draw")  # If both sums are equal, it's a draw

# Start the game
start_game()
