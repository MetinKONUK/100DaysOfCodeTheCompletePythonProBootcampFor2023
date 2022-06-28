from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n Enter your move: "))

if move not in range(0, 3):
    print("Invalid move!")
else:
    ascii = [rock, paper, scissors]
    comps_move = randint(0, 2)
    print("Your move", ascii[move])
    print("Computer's move", ascii[comps_move])
    res = move - comps_move
    if res == -2 or res == 1:
        print("You won!")
    elif res == 2 or res == -1:
        print("You lost!")
    else:
        print("Draw!")
    

