class MenuItem:
    def __init__(self, name: str, cost: float, ingredients: dict):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = [MenuItem(name='espresso', cost=1.5, ingredients={"water": 50, "milk": 0, "coffee": 18}),
                     MenuItem(name='latte', cost=2.5, ingredients={"water": 200, "milk": 150, "coffee": 24}),
                     MenuItem(name='cappuccino', cost=3.0, ingredients={"water": 300, "milk": 200, "coffee": 100})]

    def find_drink(self, order_name):
        for item in self.menu:
            if order_name == item.name:
                return item
        return None
