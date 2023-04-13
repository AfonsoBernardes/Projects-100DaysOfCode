import os
from auction_logo import logo

# Ask for bidders name and their bid.
bidding_over = False
bidders_dict = {}
while not bidding_over:
    print(logo)
    name = input("Hello bidder, welcome to the auction. What is your name? ")
    bid_value = int(input("What is your bid? €"))
    bidders_dict[name] = bid_value

    while True:
        more_bidders = input("Are there any more bidders? ").upper()
        if more_bidders == "YES":
            break
        elif more_bidders == "NO":
            bidding_over = True
            break
        else:
            print("Invalid answer.")
    # This line clears screen to prevent too much scrolling. If not working, go to Run -> Edit Configs and toggle
    # "Emulate terminal in output console".
    os.system('cls')

print(logo)
highest_bidder, highest_bid = max(bidders_dict.items(), key=lambda k: k[1])
print(f"The highest bidder was {highest_bidder} with a bid of €{highest_bid}.")
