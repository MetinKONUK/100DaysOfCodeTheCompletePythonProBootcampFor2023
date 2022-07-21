from random import randint
from art import text

print(text)

def main():
    number = randint(1, 100)
    turns = 10
    while True:
        guess = int(input("Enter a number in a range of [1, 100]"))
        if guess == number:
            print(f"Correct! Number was {number}.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        turns -= 1
        if not turns:
            print(f"Out of turns! The number was {number}.")
            break