#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Less than 6 and not 0"
if number < 0:
    number = -1 * number
    last_digit = -1 * (number % 10)
    number = -1 * number
elif number > 0:
    last_digit = number % 10
elif number == 0:
    last_digit = number
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
elif last_digit < 6:
    print(f"Last digit of {number:d} is {last_digit:d} and is {str}")
