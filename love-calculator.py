# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#for loops and custom defined functions are not used

trueCount = 0
loveCount = 0
#concatenate the strings
text = name1 + name2
#upper the string
text = text.upper()

#count the T, R, U, E occurings
trueCount += text.count('T')

trueCount += text.count('R')

trueCount += text.count('U')

trueCount += text.count('E')

#count the L, O, V, E occurings
loveCount += text.count('L')

loveCount += text.count('O')

loveCount += text.count('V')

loveCount += text.count('E')

#print the compatibility percentage
compaPerc = trueCount * 10 + loveCount
if compaPerc < 10 or 90 < compaPerc:
    print(f"Your score is {compaPerc}, you go together like coke and mentos.")
elif 40 < compaPerc and compaPerc < 50:
    print(f"Your score is {compaPerc}, you are alright together.")
else:
    print(f"Your score is {compaPerc}.")