#Generating password Randomly in a Shuffled way
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Password Generator Project

password_list = []

#letters
for char in range(0, nr_letters + 1):
    password_list.append(random.choice(letters)) # 'append' means to add a value. And it is same as password_list = password_list + random.choice(letters) when we concatenate string but it cannot be used with lists.
# print(password_list)

#symbols
for char in range(0, nr_symbols + 1):
    password_list.append(random.choice(symbols))
# print(password_list)

#numbers
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
# print(password_list)

# Changing the order of List or Shuffling
random.shuffle(password_list)

# print(password_list) # display list of generated password

password = ""
for char in password_list:
    password = password + char
print(password)
