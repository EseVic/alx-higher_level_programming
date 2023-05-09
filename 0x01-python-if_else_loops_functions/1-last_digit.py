#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = rnd(number) % 10
if number < 0:
    str = -str
print("Last digit of {} is {} and is ".format(number, str), end="")
if str > 5:
    print("greater than 5")
elif str == 0:
    print("0")
else:
    print("less than 6 and not 0")
