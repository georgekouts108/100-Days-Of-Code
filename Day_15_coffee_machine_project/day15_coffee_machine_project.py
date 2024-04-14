print("Welcome to the Coffee Machine!")

machine = {'water':300, 'milk':200, 'coffee':100, 'money':0.00}
ingredients = {'espresso':[50,18,0],'latte':[200,24,150],'cappuccino':[250,24,100]}
prices = {'espresso':1.50,'latte':2.50,'cappuccino':3.00}

def print_report():
    print(f"""
The Coffee Machine has:\n
- Water: {machine['water']} mL
- Milk: {machine['milk']} mL
- Coffee: {machine['coffee']} g
- Money: ${machine['money']}
""")

def are_resources_sufficient(coffee_type):
    water_rq, coffee_rq, milk_rq = tuple(ingredients[coffee_type])
    ok = True
    
    if machine['water'] < water_rq:
        print("There's not enough water.")
        ok = False
    if machine['milk'] < milk_rq:
        print("There's not enough milk.")
        ok = False
    if machine['coffee'] < coffee_rq:
        print("There's not enough coffee.")
        ok = False
    
    return ok

def pay(coffee_type):
    cost = prices[coffee_type]
    amount_paid = 0
    change = 0
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    amount_paid = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

    if amount_paid >= cost:
        change = round(amount_paid - cost, 2)
    else:
        print("That's not enough money. Money refunded.")
        return (0,0, False)

    return (amount_paid, change, True)

def make_coffee(coffee_type):
    if not are_resources_sufficient(coffee_type):
        print("Not enough resources in the coffee maker. Transaction cancelled.")
        return

    amount_paid, change, approved = pay(coffee_type)

    if approved:
        water_rq, coffee_rq, milk_rq = tuple(ingredients[coffee_type])
        
        machine['water'] = machine['water'] - water_rq
        machine['milk'] = machine['milk'] - milk_rq
        machine['coffee'] = machine['coffee'] - coffee_rq
        machine['money'] = machine['money'] + prices[coffee_type]

        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type} ☕️ Enjoy!")

while True:
    order = input("""
- Type \'espresso\', \'latte\', or \'cappuccino\' to order a drink
- Type \'report\' to see the coffee machine's stock
- Type \'off\' to turn off the machine
""")
    if order.lower() in ['espresso'.lower(), 'latte'.lower(), 'cappuccino'.lower()]:
        make_coffee(order.lower())

    elif order.lower() == 'report':
        print_report()
        
    elif order.lower() == 'off':
        break
    
    else:
        print("Invalid input.")
