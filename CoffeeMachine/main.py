from menu import MENU, resources
import sys
import machine

# TODO-1: Prompt user asking "What would you like?". Check user input.
coffee_machine = machine.Machine(resources)
while True:
    user_choice = input('What would you like? Espresso, Latte or Cappuccino. ').lower()
    if user_choice in MENU:
        break
    elif user_choice == 'report':
        coffee_machine.get_report()
    elif user_choice == 'off':
        sys.exit("Machine is shutting down for maintenance.")
    else:
        print("Invalid input!\n")

# TODO-4: Check if resources are sufficient.
#         Print:"Sorry there is not enough {resource}.
#
# TODO-5: If there are enough resources to make drink, prompt user to insert coins.
#         Quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

# TODO-6: Check if user inserted enough money.
#         Add drink's money to machine.money.
#         Offer change.

# TODO-7: Make the coffee.
#         Deduct resources from machine.
