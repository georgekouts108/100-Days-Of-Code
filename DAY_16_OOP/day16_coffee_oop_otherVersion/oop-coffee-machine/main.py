from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Coffee Machine!")

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    command = input("""
- Type \'espresso\', \'latte\', or \'cappuccino\' to order a drink
- Type \'report\' to see the coffee machine's stock
- Type \'off\' to turn off the machine
""")
    if command.lower() == 'report':
        coffee_maker.report()
    elif command.lower() == 'off':
        break
    else:
        drink_ordered = menu.find_drink(command.lower())
        if drink_ordered is not None:
            if coffee_maker.is_resource_sufficient(drink_ordered):
                approved = money_machine.make_payment(drink_ordered.cost)
                if approved:
                    coffee_maker.make_coffee(drink_ordered)
