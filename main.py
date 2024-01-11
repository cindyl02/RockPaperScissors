import random
from game_images import game_images


def get_user_choice():
    return int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


def get_computer_choice():
    return random.randint(0, 2)


def compare_choice(computer_choice, user_choice):
    if computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif computer_choice == 2 and user_choice == 0:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("It's a draw.")


def run_program():
    user_choice = get_user_choice()
    if user_choice >= 3 or user_choice < 0:
        print("Valid numbers are 0, 1, and 2. You lose.")
    else:
        print(game_images[user_choice])
        computer_choice = get_computer_choice()
        print(f"Computer chose: {game_images[computer_choice]}")
        compare_choice(computer_choice, user_choice)


if __name__ == '__main__':
    run_program()
