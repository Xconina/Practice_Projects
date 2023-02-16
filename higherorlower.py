from game_data import data
from art import vs
from art import higher_or_lower_logo
import random
import os
#logo
#Compare A  (person)(descr)(from)
#vs art
#Against B: (person) (descr)(from)
#Who has more followers? Type 'a' or 'b'

#if lose- Sorry that's wrong. final score: ()
#if right, put "thats right. current score: " and continue
def compare(choice, a_followers, b_followers):
    if a_followers > b_followers:
        return choice == "a"
    else:
        return choice == "b"

def get_account():
    # get random account from data set
   return random.choice(data)
    
def format_data(account):
    # format data into printable format
    name = account["name"]
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


# name , follower_count, description, country = random.choice([data.keys()])
def higher_or_lower():
    # main function
    print(higher_or_lower_logo)
    score = 0
    game_should_continue = True
    account_a = get_account()
    account_b = get_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_account()

        while account_a == account_b:
            account_b = get_account()
        
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        print(f"a = {account_a['follower_count']}")
        print(f"b = {account_b['follower_count']}")
        choice = input("Who has more followers? Type 'A' or 'B'").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        
        is_correct = compare(choice, a_follower_count, b_follower_count)
        os.system('cls')
        print(higher_or_lower_logo)
        if is_correct:
            score += 1
            
            print(f"That's right! Current score: {score}.")
  
        else:
            game_should_continue = False
            print(f"Sorry, that's incorrect. Final score: {score}")



   
#start main program

higher_or_lower()

