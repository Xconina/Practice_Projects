#Silent Auction Project
import os
import random
os.system('cls||clear')
bids = {}
finished = False
items = ["luggage set", "painting", "diamond necklace"]
def silent_auction(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the silent Auction!")
print(f"Today we are auctioning a {random.choice(items)}")
while not finished:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    bids[name] = bid
    more_bidders = input("Are there any more bidders?\n").lower()
    if more_bidders == "no":
        finished = True
        silent_auction(bids)
    elif more_bidders== "yes":
        os.system('cls')