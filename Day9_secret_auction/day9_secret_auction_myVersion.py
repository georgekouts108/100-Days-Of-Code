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
name = input("What is your name? : ")
bid = float(input("What's your bid? : $"))

bids = {name:bid}

while True:
    more_bidders = input("Are there any other bidders? Type \'yes\' or \'no\' :")
    if more_bidders.upper() == 'no'.upper():
        break

    elif more_bidders.upper() == 'yes'.upper():
        next_bidder_name = input("What is your name? : ")
        next_bidder_bid = float(input("What's your bid? : $"))
        bids[next_bidder_name] = next_bidder_bid

highest_bid = 0
name_in_lead = ''
for name in bids.keys():
    if bids[name] >= highest_bid:
        name_in_lead = name
        highest_bid = bids[name]

print(f"\nThe winner is {name_in_lead} with a bid of ${highest_bid}")
    
