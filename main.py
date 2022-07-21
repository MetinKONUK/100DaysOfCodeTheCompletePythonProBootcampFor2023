from random import randint
from art import text

print(text)

def main():
    number = randint(1, 100)
    guess = int(input("Enter a number in a range of [1, 100]"))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct! Number was {number}.")