"""
Description:
Below example shows how to find out sum of each digit in the given number using recursion logic.
For example, if the number is 259, then the sum should be 2+5+9 = 16.
"""

import math


def calculateSumEachDigitRecursion(number):
    if number >= 1:
        digit = (math.floor(number)) % 10
        return digit + calculateSumEachDigitRecursion(number / 10)
    return 0


number = 259
sumEachDigitRecursion = calculateSumEachDigitRecursion(number)
print("Sum of each digit of a number " + str(number) + " equals " + str(sumEachDigitRecursion))
