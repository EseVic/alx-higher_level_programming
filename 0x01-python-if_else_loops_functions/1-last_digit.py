#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
first_digit = " and is greater than 5"
second_digit = " and is 0"
third_digit = " and is less than 6 and not 0"
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print("Last digit of {} is {}".format(number, last) +first_digit)
elif last == 0:
    print("Last digit of {} is {}".format(number, last) + second_digit)
else:
    print("Last digit of {} is {}".format(number, last) + third_digit)
