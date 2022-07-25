from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main() -> None:
    menu = Menu()
    machine = CoffeeMaker()
    till = MoneyMachine()
    while True:
        order = input(f"What would you like? ({menu.get_items()}): ")
        if order == "report":
            machine.report()
            till.report()
        elif order in menu.get_items():
            item: MenuItem = menu.find_drink(order)
            if machine.is_resource_sufficient(item) and till.make_payment(item.cost):
                machine.make_coffee(item)
        elif order == "stop":
            break
        else:
            print("Insufficient request!")
    print("Serving you was a pleasure...\n\t-Coffee Machine")


main()
