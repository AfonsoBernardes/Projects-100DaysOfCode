class Machine:
    def __init__(self, resources: dict):
        """
        Creates a machine object with initialized with resources from a dictionary.
        """
        self.water = resources['water']
        self.milk = resources['milk']
        self.coffee = resources['coffee']
        self.money = 0

    def get_report(self):
        print(f'Water: {self.water}ml')
        print(f'Milk: {self.milk}ml')
        print(f'Coffee: {self.coffee}g')
        print(f'Money: {self.money}€\n')
