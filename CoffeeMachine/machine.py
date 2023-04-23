class Machine:
    def __init__(self, resources: dict, menu: dict):
        """
        Creates a machine object with initialized with resources from a dictionary.
        """
        self.menu = menu
        self.accepted_coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
        self.water = resources['water']
        self.milk = resources['milk']
        self.coffee = resources['coffee']
        self.money = 0

    def get_menu(self):
        return self.menu

    def get_report(self):
        print(f'Water: {self.water}ml')
        print(f'Milk: {self.milk}ml')
        print(f'Coffee: {self.coffee}g')
        print(f'Money: {self.money}€\n')

    def check_resources(self, drink: str):
        """
        Checks if machine has enough resources to make drink.
        :param drink:
        :return: bool
        """
        if self.water < self.menu[drink]['ingredients']['water']:
            print('Sorry, there is not enough water.')
            return False

        if self.milk < self.menu[drink]['ingredients']['milk']:
            print('Sorry, there is not enough milk.')
            return False

        if self.milk < self.menu[drink]['ingredients']['coffee']:
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

    def make_drink(self, drink: str):
        """
        Get drink user wants. Ask for the coins. Check if resources are enough and if so make drink:
            deduct from resources, add money to machine, and give change.
        :param drink:
        :return:
        """
        total_money = self.get_coins()
        if total_money < self.menu[drink]['cost']:
            print(f'\nTotal amount inserted: {total_money}€')
            print(f"Drink's price: {self.menu[drink]['cost']}")
            print("Sorry, that's not enough money. Money refunded.\n")
            return

        # If machine can make drink: Deduct resources, add money, give change.
        self.water -= self.menu[drink]['ingredients']['water']
        self.milk -= self.menu[drink]['ingredients']['milk']
        self.coffee -= self.menu[drink]['ingredients']['coffee']
        self.money += self.menu[drink]['cost']

        change = total_money - self.menu[drink]['cost']
        print(f'\nTotal amount inserted: {total_money}€')
        print(f"Drink's price: {self.menu[drink]['cost']}")
        print(f"Here is {change:.2f}€ in change.")
        print(f"Here is your {drink} ☕. Enjoy!\n")
        return
