print("Welcome to Tip Calculator!!!")
bill = float(input("What is the total bill?\n"))
tip = float(input("What percentage of tip would you like to give? 10, 12 or 15?"))
number_of_people = int(input("How many people to split the bill? "))
tip_in_amount = ((tip/100)*bill)
final_bill = ((bill+tip_in_amount)/number_of_people)
rounded_off_bill = round(final_bill, 2)
print(f"Each should pay $ {rounded_off_bill}")
