# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - age
in_days = int(years_left * 365)
in_weeks = int(years_left * 52)
in_months = int(years_left * 12)

result_text = f"You have {in_days} days, {in_weeks} weeks, and {in_months} months left."
print(result_text)