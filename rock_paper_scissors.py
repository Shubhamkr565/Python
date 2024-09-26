import random

Rock = '''
    _______
---'   ____)
       (___)
       (___)
       (__)
---.__ (__)

'''

Paper = '''
    _____
---'  ___)_____
         ______)
         ________)
         (_______)
----  :__(______)

'''



Scissors = '''
    _____
---' ____)______
         _______)
    ______________)
    (_____)
--.__(___)
    
'''

game_image = [Rock, Paper, Scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n "))
print("User choice:")
print(game_image[user_choice])

computer_input = random.randint(0,2)
print("Computer choice:")
print(game_image[computer_input])

if user_choice < 0 or user_choice > 2:
    print("Invalid entry. Please choose a number between 0 and 2.")
elif user_choice == computer_input:
    print("Draw!")
elif user_choice == 0 and computer_input == 1:
    print("You lose!")
elif user_choice == 0 and computer_input == 2:
    print("You win!")
elif user_choice == 1 and computer_input == 0:
    print("You win!")
elif user_choice == 1 and computer_input == 2:
    print("You lose!")
elif user_choice == 2 and computer_input == 0:
    print("You lose!")
elif user_choice == 2 and computer_input == 1:
    print("You win!")
