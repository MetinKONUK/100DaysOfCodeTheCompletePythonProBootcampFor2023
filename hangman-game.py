from random import choice
from hangman_words import words
from hangman_art import stages, logo
word = choice(words)
model = ['_' for _ in range(0, len(word))]
rights = 7
done = False
left = len(word)
print(logo)
while True:
    #Check if user has got all letters.
    if not left:
        print("You won!")
        break
    if not rights:
        #If lives goes down to 0 then the game should stop and it should print "You lose."
        print("You lost!")
        break
    guess = input("Enter your letter guess: ").lower()
    if guess in word:
        for i in range(0, len(word)):
            if word[i] == guess:
                model[i] = guess
                left -= 1
        #Join all the elements in the list and turn it into a String.
        print("".join(model))
    else:
        #TODO-2: - If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1. 
        rights -= 1
        print(stages[rights])
