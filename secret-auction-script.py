from art import logo
import os

print(logo)
finished = False
bids = {}
def find_highest_bidder(bids):
    highest = 0
    winner = ""
    for key in bids:
        if bids[key] > highest:
            highest = bids[key]
            winner = key
    print(f"The winner is {winner} with a bid of {highest}")
    
        

    
while not finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    finished = False if input("Are there any other bidders? Type 'yes' or 'no'.") == "yes" else True
    if not finished:
        os.system('cls||clear')
find_highest_bidder(bids)