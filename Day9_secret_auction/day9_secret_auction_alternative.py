gavel = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\

"""

print(gavel)
print("Welcome to the secret auction program.")
bids = {}
bidding_done = False




while bidding_done:
    name = input("What is your name? : ")
    bid = float(input("What's your bid? : $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type \'yes\' or \'no\' :")
    if more_bidders.upper() == 'no'.upper():
        bidding_done = True

highest_bid = 0
name_in_lead = ''
for name in bids.keys():
    if bids[name] >= highest_bid:
        name_in_lead = name
        highest_bid = bids[name]

print(f"\nThe winner is {name_in_lead} with a bid of ${highest_bid}")
    
