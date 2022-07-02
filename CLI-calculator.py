operations = dict()

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations['+'] = add
operations['-'] = substract
operations['*'] = multiply
operations['/'] = divide

num1 = int(input("What's the first number?: "))

for key in operations:
    print(key)

operation = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

function = operations[operation]

print(f"{num1} {operation} {num2} = {function(num1, num2)}")