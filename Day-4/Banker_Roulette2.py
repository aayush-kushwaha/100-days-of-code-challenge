import random
names = input("Enter names separated by commas: ")
name_list = names.split(", ") #.split(", " is used to convert the name variable in list if the input is separated by comma.)
name_list_len = len(name_list) #len(name_list) counts the number of elements present in name_list
name_shuffle = random.randint(0, name_list_len - 1) #It will give a random integer output and here len - 1 is used because in python the positioning of values starts with 0th index as a result it will have one less position as it starts with 0
bill_payer = name_list[name_shuffle] #Here we have given index place which we want to select as output where name_list is the list provided by us and "name_shuffle" gives the output of random function

print(bill_payer + " is going to pay the bill today!!!")
