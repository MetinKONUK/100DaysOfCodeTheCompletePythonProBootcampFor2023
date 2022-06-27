# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
y = "Leap year."
n = "Not leap year."

if not year % 4:
    if not year % 100:
        if not year % 400: print(y)
        else: print(n)
    else:
        print(y)
else:
    print(n)

