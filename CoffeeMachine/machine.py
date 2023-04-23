from menu import Menu, MenuItem


class Machine:
    def __init__(self, menu: Menu):
        """
        Creates a machine object with initialized with resources from a dictionary.
        """
        self.menu = menu
        self.accepted_coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.money = 0

    def get_menu(self):
        return self.menu

    def get_report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f'Money: {self.money}€\n')

    def check_resources(self, drink: MenuItem):
        """
        Checks if machine has enough resources to make drink.
        :param drink:
        :return: bool
        """
        if self.resources['water'] < drink.ingredients['water']:
            print('Sorry, there is not enough water.')
            return False

        if self.resources['milk'] < drink.ingredients['milk']:
            print('Sorry, there is not enough milk.')
            return False

        if self.resources['coffee'] < drink.ingredients['coffee']:
            print('Sorry, there is not enough coffee.')
            return False

        return True

    def get_coins(self):
        print('\nPlease, insert coins.')
        while True:
            try:
                num_quarters = int(input('How many quarters? '))
                num_dimes = int(input('How many dimes? '))
                num_nickles = int(input('How many nickles? '))
                num_pennies = int(input('How many pennies? '))
                break
            except ValueError:
                print("That is not a coin. try again.\n")

        return num_quarters * self.accepted_coins['quarters'] + num_dimes * self.accepted_coins['dimes'] + \
               num_nickles * self.accepted_coins['nickles'] + num_pennies * self.accepted_coins['pennies']

    def make_drink(self, drink):
        """
        Get drink user wants. Ask for the coins. Check if resources are enough and if so make drink:
            deduct from resources, add money to machine, and give change.
        :param drink:
        :return:
        """
        total_money = self.get_coins()
        if total_money < drink.cost:
            print(f'\nTotal amount inserted: {total_money}€')
            print(f"Drink's price: {drink.cost}")
            print("Sorry, that's not enough money. Money refunded.\n")
            return

        # If machine can make drink: Deduct resources, add money, give change.
        self.resources['water'] -= drink.ingredients['water']
        self.resources['milk'] -= drink.ingredients['milk']
        self.resources['coffee'] -= drink.ingredients['coffee']
        self.money += drink.cost

        change = total_money - drink.cost
        print(f'\nTotal amount inserted: {total_money:.2f}€')
        print(f"Drink's price: {drink.cost:.2f}€")
        print(f"Here is {change:.2f}€ in change.")
        print(f"Here is your {drink.name} ☕. Enjoy!\n")
        return
