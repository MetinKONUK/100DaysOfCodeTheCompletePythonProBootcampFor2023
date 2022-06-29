#Step 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
from random import choice
words = ["elephant", "lion", "salamander", "penguin"]
word = choice(words)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in word:
    if letter == guess:
        print("Yes")
    else:
        print("No")