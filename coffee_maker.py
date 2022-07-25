from menu import MenuItem


class CoffeeMaker:
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        res = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                res = False
        return res

    def make_coffee(self, order: MenuItem) -> None:
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def report(self) -> None:
        print(f"Water: {self.resources['water']}\nMilk: {self.resources['milk']}\nCoffee: {self.resources['coffee']}")