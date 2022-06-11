even_number = 0
for number in range(0,101,2):
    if number % 2 == 0:
        #Divisible by 2
        even_number = even_number + number # I wrote 'even_number = even_number + number' because to replace previous value of even_number
print(f"The sum of Even numbers is: {sum_even_number}")