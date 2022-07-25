class MenuItem:
    def __init__(self, name, water, milk, coffee, cost) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = dict(water=water, milk=milk, coffee=coffee)


class Menu:
    def __init__(self) -> None:
        self.menu = (MenuItem("latte", 200, 150, 24, 2.5),
                     MenuItem("espresso", 50, 0, 18, 1.5),
                     MenuItem("cappuccino", 250, 50, 24, 3))

    def get_items(self) -> str:
        return "\\".join([item.name for item in self.menu])

    def find_drink(self, order_name) -> object:
        for item in self.menu:
            if item.name == order_name:
                return item
        return None
