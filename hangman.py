#this is a game of hangman

###get variables ready
import random
from hangman_words import word_list
won = False
display =[]
life = 6
##art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
]
####logo
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
#game over function
def game_over():
    global won
    global life
    print("The game is over")
    if won == True:
        print("Congrats! You solved it.")
        
    else:
        print("You didn't guess the word. Maybe next time.")
        print(f"The word was {chosen_word}")
    answers = ["yes", "no"]
    yesno =""

    yesno = input("Would you like to play again?").lower
    if yesno=="yes":
        won = False
        life = 6
        start_program()
    elif yesno=="no":
        print("Maybe another time.")
        quit()
    else:
        print("I didn't understand")
       
"""need to fix the restart """
###start program

# print(display)
#ask user to guess letter
def guessing():
    global life
    global display
    global chosen_word
    global word_length
    global won
    guesses = []
    while '_' in display:
        guess = input("Guess a letter: ").lower()
        #if guess in display:
            # print(f"You already guessed that.\nYour previous guesses were: {guesses}")
            #print("Sorry, you have already guessed that.")
        #is letter in word?
        #yes, replace with letter
        for position in range(word_length):
            letter = chosen_word[position]
            
            # if letter in guesses:
            #     print(f"You already guessed that.\nYour previous guesses were: {guesses}")
            # else:
            # guesses.append(guess)
            if letter == guess:
                display[position]=letter
                print(stages[life])
                if "_" not in display:
                    display[position]=letter
                    print(stages[life])
                    won = True
                    game_over()        
           
                
        if guess not in chosen_word:
            print("Sorry. That letter isn't in the word. You lose one life.")
            life -= 1
            print(stages[life])
            if life == 0:
                game_over()
        print(" ".join(map(str, display)))


def start_program():
    global display
    global chosen_word
    global word_length
    print(logo)
    print("Let's play a game of hangman!")
    ready = input("Press enter when you are ready to begin")
    #generate random word
    chosen_word = random.choice(word_list)
    word_length= len(chosen_word)
    #generate blanks for word
    for _ in range(word_length):
        display += "_"
    print(" ".join(map(str, display)))
    guessing()
start_program()
