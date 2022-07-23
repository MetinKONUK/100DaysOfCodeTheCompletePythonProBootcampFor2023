from game_data import data
from replit import clear
from art import logo, vs
from random import choice

def introduce(idx, person):
    print(f"Compare {idx}: {person['name']}, {person['description']} from {person['country']}.")

def main():
    print(logo)
    final_score = 0
    first = choice(data)
    second = choice(data)
    while True:
        answer = 'A' if first["follower_count"] > second["follower_count"] else 'B'
        while second == first:
            second = choice(data)
        introduce('A', first)
        print(vs)
        introduce('B', second)
        guess = input("Who has more followers? Type 'A' or 'B':").upper()
        if guess != answer:
            print(f"Sorry that's wrong final score: {final_score}.")
            break
        else:
            clear()
            final_score += 1
            
            if answer == 'A':
                second = choice(data)
            else:
                first = choice(data)
main()