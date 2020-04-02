"""
A number is called an Armstrong number if it is equal to the cube of its each digit.
// for example, 153 is an Armstrong number because 153= 1+ 125+27 which is equal to 1^3+5^3+3^3.
"""

import math


def checkArmstrongNumber(number):
    isArmstrongNumber = False
    strArmstrongNumber = str(number)
    lenArmstrongNumber = len(strArmstrongNumber)
    digits = []
    times = math.pow(10, lenArmstrongNumber)
    for idx in range(lenArmstrongNumber):
        digit = math.trunc(number % times / (times / 10))
        digits.append(digit)
        times /= 10
    sumCubeDigits = 0
    for digit in digits:
        sumCubeDigits += math.pow(digit, lenArmstrongNumber)
    if number == sumCubeDigits:
        isArmstrongNumber = True
    return isArmstrongNumber


number = 153
if checkArmstrongNumber(number):
    print("Number " + str(number) + " is armstrong number")
else:
    print("Number " + str(number) + " is not armstrong number")

number = 184
if checkArmstrongNumber(number):
    print("Number " + str(number) + " is armstrong number")
else:
    print("Number " + str(number) + " is not armstrong number")

number = 9474
if checkArmstrongNumber(number):
    print("Number " + str(number) + " is armstrong number")
else:
    print("Number " + str(number) + " is not armstrong number")

number = 54748
if checkArmstrongNumber(number):
    print("Number " + str(number) + " is armstrong number")
else:
    print("Number " + str(number) + " is not armstrong number")
