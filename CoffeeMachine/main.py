from menu import MENU, resources
import sys
import machine

# Prompt user asking "What would you like?". Check user input.
coffee_machine = machine.Machine(resources, MENU)
while True:
    user_choice = input('What would you like? Espresso, Latte or Cappuccino. ').lower()
    if user_choice in coffee_machine.get_menu():
        # Check if resources are sufficient.
        if coffee_machine.check_resources(drink=user_choice):
            coffee_machine.make_drink(drink=user_choice)
    elif user_choice == 'report':
        coffee_machine.get_report()
    elif user_choice == 'off':
        sys.exit("Machine is shutting down for maintenance.")
    else:
        print("Invalid input!\n")
