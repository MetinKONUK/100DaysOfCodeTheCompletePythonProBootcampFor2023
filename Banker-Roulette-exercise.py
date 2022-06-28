from random import seed, randint

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rand_idx = randint(0, len(names)-1)
person_name = names[rand_idx]
print(f"{person_name} is going to buy the meal today!")