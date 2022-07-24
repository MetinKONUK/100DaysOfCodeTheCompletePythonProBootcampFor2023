from data import data, resources


def report(obj):
    print(f"Water: {obj['water']}\nMilk: {obj['milk']}\nCoffee: {obj['coffee']}\nMoney: {obj['money']}")


def evaluate(quarters, dimes, nickels, pennies):
    total = quarters * 0.25
    total += dimes * 0.1
    total += nickels * 0.05
    total += pennies * 0.01
    return total


def subtract(obj, beverage):
    obj["water"] -= data[beverage]["ingredients"]["water"]
    obj["coffee"] -= data[beverage]["ingredients"]["coffee"]
    if "milk" in data:
        obj["milk"] -= data[beverage]["ingredients"]["milk"]


def handle_money(cost):
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    return evaluate(quarters, dimes, nickels, pennies) - cost


def handle_resources(obj, beverage):
    lacking = list()
    if data[beverage]["ingredients"]["water"] > obj["water"]:
        lacking.append("water")
    if data[beverage]["ingredients"]["coffee"] > obj["coffee"]:
        lacking.append("coffee")
    if "milk" in data and data[beverage]["ingredients"]["milk"] > obj["milk"]:
        lacking.append("milk")
    return lacking


def handle_drink(machine, beverage):
    lacking = handle_resources(machine, beverage)
    if len(lacking) > 0:
        print(f"Sorry we are lack of following items: {', '.join(lacking)}.")
        return
    
    cost = data[beverage]["cost"]
    change = handle_money(cost)
    if change:
        print(f"Here is ${round(change, 3)} dollar in change.\nHere is your {beverage} ☕️. Enjoy!")
        subtract(machine, beverage)
        machine["money"] += cost
    else:
        print("Sorry that's not enough money. Money refunded.")


def main():
    machine = resources
    machine["money"] = 0

    while True:
        cmd = input(" What would you like? (espresso/latte/cappuccino): ")
        if cmd == "report":
            report(machine)
        else:
            handle_drink(machine, cmd)


main()
