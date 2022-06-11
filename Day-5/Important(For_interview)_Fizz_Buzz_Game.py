for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        # Divisble by 3 and 5
        print("FizzBuzz")
    elif n % 3 == 0:
        # Divisible by 3
        print("Fizz")
    elif n % 5 == 0:
        # Divisible by 5
        print("Buzz")
    else:
        print(n)