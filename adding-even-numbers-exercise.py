#Write your code below this row 👇

#first way
acc = 0
for number in range(2, 101, 2):
    acc += number
print(acc)

#second way
acc = 0
for number in range(2, 101):
    if not number % 2:
        acc += number
print(acc)