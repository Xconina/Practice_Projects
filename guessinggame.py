#guessing game
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
def game_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS



def game():
    chosen_number = random.randint(1,101)
    finished = False
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    turns = game_level()
    print(f"You have {turns} turns to guess the number.")
    while not finished:
        guess = int(input("Make a guess:\n"))
        if guess == chosen_number:
            print(f"You won! The number was {chosen_number}")
            finished = True
        elif guess < chosen_number or guess > chosen_number:
            if guess < chosen_number:
                print("Too low.\nGuess again")
            else:
                print("Too high.\nGuess again.")
            turns -= 1
            if guess == 0:
                print("Sorry, you are out of attempts. You lost.")
                finished = True
            else:
                print(f"You have {turns} attempts remaining to guess the number")
    # if input("would you like to play again? 'y' for yes, 'n' for no:\n").lower == 'y':
    #     game()

game()