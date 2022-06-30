#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number//2 + 1):
        if not number % i: is_prime = False
    print("It's a prime number." if is_prime and number > 0 and number != 1 else "It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
