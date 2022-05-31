print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
if height > 120:
    print("You can ride the Rollercoaster.")
    age = int(input("Enter your age:\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age > 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12.")

    want_photos = input("Do you want photos? y/n:\n")
    if want_photos == "y":
        total_bill = bill + 3
    print(f"The total bill is {total_bill}")
else:
    print("You can't ride the Rollercoaster.")