print('''



                                               _
                 ___                          (_)
               _/XXX\
_             /XXXXXX\_                                    __
X\__    __   /X XXXX XX\                          _       /XX\__      ___
    \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX\
  \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \
 ___/   \__/   \ \__     \\__           /  \_//  _ _ \  \     __  /  \____/
/  __    \  /     \ \_   _//_\___    __/    //           \___/  \/     __/
__/_______\________\__\_/________\__/_/____/_____________/_______\____/____
                                  ___
                                 /L|0\
                                /  |  \
                               /       \
                              /    |    \
                             /           \
                            /  __  | __   \
                           /  __/    \__   \
                          /  /__   |  __\   \
                         /___________________\
                         /          |         \
                              /   _|_   \
                      /      ____/___\____     \
                      ___________[o0o]___________
                               O   O    O

''')
print("Welcome to Treasure Island!!!")
print("Your mission is to find the treasure.")
start_game = input("You are at a cross road. Where do you want to go? Type 'Left' or 'Right'\n")
start_game_lower = start_game.lower()
if start_game_lower == "left":
    b = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    b_lower = b.lower()
    if b == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        color_lower = color.lower()
        if color_lower == "red":
            print("Game Over")
        elif color_lower == "blue":
            print("Game Over")
        else:
            print("You win!!!")
    else:
        print("Game Over")
else:
    print("Game Over")    

