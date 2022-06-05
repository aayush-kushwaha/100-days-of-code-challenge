print("Welcome to Rock, Paper,")
print('''

            d88b               __     __
           /78889            d7 7b  d7 7b
          d88889           d8`8b  d8`-8b _
         d888889         d8888b d8888b d7 7b
        d888888        d88888b d8888b d888b
       d8888884_____d888888b d888b  d888b
      d88888888888888888888,d888b  d888b _
     d888888888888888888888888b  d888b d7_b
   d8 88888888888888888888888,d8888b d888b
 d888 888888888888888888888888888b d8888b
   888 8888888888888888888888888b d888b
  88888888888888888888888888888,8888b
  8888888888 8888888888888888888888b
 888888888888 88888888888888888p8"
88888888888888`pj998ppppp88888"
8888888hjw888b
 88888888888b
''')
import random
player_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissor: "))
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("Computer chose Rock")
    # Rock
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice == 1:
    print("Computer chose Paper")
    # Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif computer_choice == 2:
    print("Computer chose Scissor")
    # Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    

if player_choice == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif player_choice == 1:
    # Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif player_choice == 2:
    # Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if computer_choice == 0 and player_choice == 0:
    print("Draw")
elif computer_choice == 0 and player_choice == 1:
    print("Player Won")
elif computer_choice == 0 and player_choice == 2:
    print("Computer Won")
elif computer_choice == 1 and player_choice == 0:
    print("Player Won")
elif computer_choice == 1 and player_choice == 1:
    print("Draw")
elif computer_choice == 1 and player_choice == 2:
    print("Player Won")
elif computer_choice == 2 and player_choice == 0:
    print("Player Won")
elif computer_choice == 2 and player_choice == 1:
    print("Computer Won")
elif computer_choice == 2 and player_choice == 2:
    print("Draw")