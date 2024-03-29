print("Welcome to the Tip Calculator!\n")
bill = float(input("Enter the total amount of the bill: $"))

tip = int(input("Enter the percentage of tip you would like to give (10, 12, or 15): "))
total = bill * (1 + (tip / 100))

ppl = int(input("how many people are splitting the bill: "))

total_each = total / ppl
print()
print("Each person pays $%.2f" % total_each)
