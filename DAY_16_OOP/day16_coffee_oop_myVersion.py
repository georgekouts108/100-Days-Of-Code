class Order():
    def __init__(self, drink, money_paid, order_num):
        self.order_num = order_num
        self.drink = drink
        self.money_paid = money_paid
        self.change = round(money_paid - drink.price, 2)
        self.approved = money_paid >= drink.price

    def print_message(self):
        if self.approved:
            print(f"Here is ${self.change} in change.")
            print(f"Here is your order #{self.order_num} for a{'n' if self.drink.name[0].lower() in ['a','e','i','o'] else ''} {self.drink.name} ☕️ Enjoy!")
        else:
            print("That's not enough money. Money refunded.")

class Drink():
    def __init__(self, name, water, milk, coffee, price):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.price = price

class CoffeeMachine():
    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = float(money)

    def print_report(self):
        print("The Coffee Machine has:")
        print(f"- Water: {self.water} mL")
        print(f"- Milk: {self.milk} mL")
        print(f"- Coffee: {self.coffee} g")
        print(f"- Money: ${self.money}")

    def use_ingredient(self,ingredient_name,amount):
        if ingredient_name == 'water':
            self.water -= amount
        elif ingredient_name == 'milk':
            self.milk -= amount
        elif ingredient_name == 'coffee':
            self.coffee -= amount

    def has_enough_of_ingredient(self, ingredient_name, amount):
        if ingredient_name == 'water':
            return (self.water >= amount)
        elif ingredient_name == 'milk':
            return (self.milk >= amount)
        elif ingredient_name == 'coffee':
            return (self.coffee >= amount)

    def can_make_drink(self, drink):
        enough_water = self.water >= drink.water
        enough_milk = self.milk >= drink.milk
        enough_coffee = self.coffee >= drink.coffee

        if not enough_water:
            print("The machine is low on water.")
        if not enough_milk:
            print("The machine is low on milk.")
        if not enough_coffee:
            print("The machine is low on coffee.")
            
        return (enough_water and enough_milk and enough_coffee)

    def pay_for_drink(self, price, payment):
        self.money += price
        #change = payment - price
        #return change

    def insert_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        amount_paid = quarters + dimes + nickels + pennies
        return amount_paid
        
    def make_drink(self, drink, payment):
        self.use_ingredient('water',drink.water)
        self.use_ingredient('milk',drink.milk)
        self.use_ingredient('coffee',drink.coffee)
        self.pay_for_drink(drink.price, payment)
        
class CoffeeShop():
    def __init__(self, menu, machine):
        self.order_count = 0
        self.menu = menu
        self.machine = machine

    def make_order(self, drink_name, payment):
        self.order_count += 1
        for drink in self.menu:
            if drink.name.lower() == drink_name.lower():
                if self.machine.can_make_drink(drink):
                    _order = Order(drink, payment, self.order_count)
                    if _order.approved:
                        self.machine.make_drink(drink, payment)
                    return _order
                else:
                    return None
                
##############################################################
############################################################## 
print("Welcome to the Coffee Machine!")
espresso = Drink(name='Espresso', water=50, milk=0, coffee=18, price=1.50)    
latte = Drink(name='Latte', water=200, milk=150, coffee=24, price=2.50)
cappuccino = Drink(name='Cappuccino', water=250, milk=100, coffee=24, price=3.00)
machine = CoffeeMachine(300,200,100,0)

shop = CoffeeShop(menu=[espresso,latte,cappuccino],machine=machine)

while True:
    command = input("""
- Type \'espresso\', \'latte\', or \'cappuccino\' to order a drink
- Type \'report\' to see the coffee machine's stock
- Type \'off\' to turn off the machine
""")
    
    if command.lower() in ['espresso'.lower(), 'latte'.lower(), 'cappuccino'.lower()]:
        ##
        drink_order = None
        if command.lower()=='espresso':
            payment = shop.machine.insert_coins()
            drink_order = shop.make_order('espresso',payment)
        elif command.lower()=='latte':
            payment = shop.machine.insert_coins()
            drink_order = shop.make_order('latte',payment)
        else:
            payment = shop.machine.insert_coins()
            drink_order = shop.make_order('cappuccino',payment)
        if drink_order != None:
            drink_order.print_message()
        ##
    elif command.lower() == 'report':
        shop.machine.print_report()
    elif command.lower() == 'off':
        break
    else:
        print("Invalid input.")
    
    


