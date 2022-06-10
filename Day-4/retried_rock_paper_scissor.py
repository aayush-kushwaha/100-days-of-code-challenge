import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissor]
computer_choice = random.randint(0,2)
user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor: \n"))
if user_choice >2:
    print("Your number is Invalid. So you lose!")
else:
    print("You chose:")
    print(game_images[user_choice])
    print("\nComputer chose:")
    print(game_images[computer_choice])

    #if computer_choice == 0 and user_choice == 0:
        #print("Draw")
    if computer_choice == user_choice:
        print("Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You Won")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer Won")
    elif computer_choice == 2 and user_choice == 0:
        print("You Won")
    elif computer_choice > user_choice:
        print("Computer Won")
    elif user_choice > computer_choice:
        print("You Won")
# else:
    
#elif computer_choice == 1 and user_choice == 1:
    #print("Draw")
#elif computer_choice == 2 and user_choice == 2:
    #print("Draw")




