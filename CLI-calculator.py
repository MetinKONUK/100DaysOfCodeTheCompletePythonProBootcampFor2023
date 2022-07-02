from art import logo
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

print(logo)

def calculate(ans = False):
    num1 = int(input("What's the first number?: ")) if not ans else ans
    
    
    for key in operations:
        print(key)
        
    operation = input("Pick an operation from the line above: ")
    
    num2 = int(input("What's the second number?: "))
    
    function = operations[operation]
    
    ans = function(num1, num2)
    
    print(f"{num1} {operation} {num2} = {ans}")
    
    char = input(f"Type 'y' to continue calculation with {ans}, or type 'n' to exit.: ").lower()
    return calculate(ans) if char == 'y' else None
calculate()