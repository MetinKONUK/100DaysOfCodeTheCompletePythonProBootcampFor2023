from random import choice

words = ["beekeeper", "astral", "elephant" ,"basically"]
word = choice(words)
model = ['_' for _ in range(0, len(word))]
rights = 7
done = False
left = len(word)

#todo-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while True:
    if not left:
        print("You won!")
        break
    if not rights:
        print("You lost!")
        break
    guess = input("Enter your letter guess: ").lower()
    if guess in word:
        for i in range(0, len(word)):
            if word[i] == guess:
                model[i] = guess
                left -= 1
        print(model)
    else:
        rights -= 1
        print("Rights left: ", rights)
