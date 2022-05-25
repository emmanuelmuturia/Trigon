#!/usr/bin/env python3

import math

print("Hello, what's your name?")

name = input()

print("Hello " + name + "! Nice to meet you. Ready for some Trigonometry?")

response = input()

print("Alright! Which trigonometric function do you want to invoke today?")
print("1. Sin\n2. Cos\n3. Tan")

choice = int(input())

if choice == 1:
    print("Please enter your number and hit ENTER...")
    sineNumber = float(input())
    sineResult = math.sin(sineNumber)
    print("The sine of your number is " + str(sineResult))

elif choice == 2:
    print("Please enter your number and hit ENTER...")
    cosineNumber = float(input())
    cosineResult = math.cos(cosineNumber)
    print("The cosine of your number is " + str(cosineResult))

elif choice == 3:
    print("Please enter your number and hit ENTER...")
    tanNumber = float(input())
    tanResult = math.tan(tanNumber)
    print("The tan of your number is " + str(tanResult))
