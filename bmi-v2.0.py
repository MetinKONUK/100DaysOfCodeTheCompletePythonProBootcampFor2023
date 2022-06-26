# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)
model = f"Your BMI is {bmi}, you are "

if bmi < 18.5:
    print(model + "underweight.")
elif 18.5 < bmi and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 < bmi and bmi < 30:
    print(model + "slightly overweight.")

elif 30 < bmi and bmi < 35:
    print(model + "obese.")
else:
    print(model + "clinically obese.")
