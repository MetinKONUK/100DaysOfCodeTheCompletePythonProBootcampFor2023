from random import choice
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)


def game():
    user = list()
    dealer: list = list()
    game_over = False

    def deal_card():
        """returns a random int representing a card from the deck"""
        return choice(cards)

    def calculate_score(crds):
        if sum(crds) == 21 and len(crds) == 2:
            return 0
        if 11 in crds and sum(crds) > 21:
            crds.remove(11)
            crds.append(1)
        return sum(crds)

    def compare(u_score, d_score):
        if u_score == d_score:
            return "Push!"
        elif d_score == 0:
            return "Lost! Dealer got a Blackjack!"
        elif u_score == 0:
            return "Win with Blackjack!"
        elif u_score > 21:
            return "You went over! Lost!"
        elif d_score > 21:
            return "Dealer went over! Win!"
        elif u_score > d_score:
            return "Win!"

        else:
            return "Lost!"

    for _ in range(2):
        user.append(deal_card())
        dealer.append(deal_card())
    while not game_over:
        user_score = calculate_score(user)
        dealer_score = calculate_score(dealer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Dealer's first card: {dealer[0]}")
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            decision = input("Type 'y' to get another card, type 'n' to pass: ")
            if decision == 'y':
                user.append(deal_card())
            else:
                game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer.append(deal_card())
        dealer_score = calculate_score(dealer)
    print(compare(user_score, dealer_score))


while input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'y':
    game()
if __name__ == "__main__":
    pass
