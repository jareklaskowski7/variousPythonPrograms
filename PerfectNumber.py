"""
 A perfect number is a positive integer that is equal to the sum
of its proper positive divisors, that is, the sum of its positive
divisors excluding the number itself. Equivalently, a perfect number
is a number that is half the sum of all of its positive divisors.
The first perfect number is 6, because 1, 2 and 3 are its proper
positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6
is equal to half the sum of all its positive divisors:
		( 1 + 2 + 3 + 6 ) / 2 = 6.
"""

import math


def checkPerfectNumber(number):
    isPerfectNumber = False
    halfNumber = math.trunc(number / 2)
    if 6 <= number == halfNumber * 2:
        positiveDivisors = []
        for idx in range(0, halfNumber):
            positiveDivisor = idx + 1
            remainder = math.fmod(number, positiveDivisor)
            if remainder == 0:
                positiveDivisors.append(positiveDivisor)

        sumNumberPositiveDivisors = 0
        for positiveDivisor in positiveDivisors:
            sumNumberPositiveDivisors += positiveDivisor

        if number == sumNumberPositiveDivisors:
            isPerfectNumber = True

    return isPerfectNumber


number = 6
if checkPerfectNumber(number):
    print("Number " + str(number) + " is perfect number")
else:
    print("Number " + str(number) + " is not perfect number")

number = 20
if checkPerfectNumber(number):
    print("Number " + str(number) + " is perfect number")
else:
    print("Number " + str(number) + " is not perfect number")

number = 51
if checkPerfectNumber(number):
    print("Number " + str(number) + " is perfect number")
else:
    print("Number " + str(number) + " is not perfect number")

number = -28
if checkPerfectNumber(number):
    print("Number " + str(number) + " is perfect number")
else:
    print("Number " + str(number) + " is not perfect number")

number = 358
if checkPerfectNumber(number):
    print("Number " + str(number) + " is perfect number")
else:
    print("Number " + str(number) + " is not perfect number")

number = 496
if checkPerfectNumber(number):
    print("Number " + str(number) + " is perfect number")
else:
    print("Number " + str(number) + " is not perfect number")
