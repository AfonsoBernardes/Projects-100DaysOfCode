from menu import Menu
import sys
import machine

# Prompt user asking "What would you like?". Check user input.
menu = Menu()
coffee_machine = machine.Machine(menu)

while True:
    order_name = input('What would you like? Espresso, Latte or Cappuccino. ').lower()
    drink = menu.find_drink(order_name)
    if drink is not None:
        # Check if resources are sufficient.
        if coffee_machine.check_resources(drink):
            coffee_machine.make_drink(drink)
    elif order_name == 'report':
        coffee_machine.get_report()
    elif order_name == 'off':
        sys.exit("Machine is shutting down for maintenance.")
    else:
        print("Invalid input!\n")
