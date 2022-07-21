from random import randint
from art import text

print(text)

def main():
    diff_level = input("Choose a difficulty level. Easy or Hard: ").lower()
    turns = 10 if diff_level == "easy" else 8
    number = randint(1, 100)
    while True:
        guess = int(input("Enter a number in a range of [1, 100]: "))
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

main()