#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    lastd = abs(number) % 10
    lastd = -1 * lastd
else:
    lastd = number % 10

if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif lastd == 0:
    print(f"Last digit of {number} is {lastd} and is 0")
elif lastd != 0 and lastd < 6:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
