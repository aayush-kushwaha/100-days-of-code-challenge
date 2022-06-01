name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_name = name1+name2
lower_combined_name = combined_name.lower()
t = lower_combined_name.count("t")
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")
l = lower_combined_name.count("l")
o = lower_combined_name.count("o")
v = lower_combined_name.count("v")
e = lower_combined_name.count("e")
sum1 = t + r + u + e
sum2 = l + o + v + e
sum1_string = str(sum1)
sum2_string = str(sum2)
combined_con = sum1_string + sum2_string
combined_sum_as_int = int(combined_con)


if combined_sum_as_int < 10 and combined_sum_as_int > 90:
    print(f"Your score is {combined_sum_as_int}, you go together like coke and mentos.")
elif combined_sum_as_int >= 40 and combined_sum_as_int <= 50:
    print(f"Your score is {combined_sum_as_int}, you are alright together.")
else:
    print(f"Your score is {combined_sum_as_int}.")