"""
Please implement this method to return the number in the array that is closest to zero.
If there are two equally far from zero elements like 2 and -2,
consider the positive element to be "closest" to zero.
"""

import math


def getNumberClosestToZero(numbers):
    numberClosestToZero = 0
    if len(numbers) >= 1:
        numberClosestToZero = math.floor(math.fabs(numbers[0]))
        for idx in range(len(numbers) - 1):
            if numberClosestToZero > math.floor(math.fabs(numbers[idx + 1])):
                numberClosestToZero = math.floor(math.fabs(numbers[idx + 1]))

    return numberClosestToZero


def getNegPosNumberClosestToZero(numbers):
    uniqueNumbers = set(numbers)

    negativeNumbers = []
    for uniqueNumber in uniqueNumbers:
        if uniqueNumber < 0:
            negativeNumbers.append(uniqueNumber)
    negativeNumbers.sort()

    positiveNumbers = []
    for uniqueNumber in uniqueNumbers:
        if uniqueNumber > 0:
            positiveNumbers.append(uniqueNumber)
    positiveNumbers.sort()

    negPosNumberClosestToZero = [0, 0]
    if len(negativeNumbers) >= 1:
        negPosNumberClosestToZero[0] = negativeNumbers[len(negativeNumbers) - 1]
    if len(positiveNumbers) >= 1:
        negPosNumberClosestToZero[1] = positiveNumbers[0]

    return negPosNumberClosestToZero


def getNumbersClosestToGivenNumber(numbers, number):
    uniqueNumbers = set(numbers)
    numbersLessThanGivenNumber = []
    numbersGreaterThanGivenNumber = []

    for uniqueNumber in uniqueNumbers:
        if uniqueNumber < number:
            numbersLessThanGivenNumber.append(uniqueNumber)
        elif uniqueNumber > number:
            numbersGreaterThanGivenNumber.append(uniqueNumber)

    numbersClosestToGivenNumber = [number, number]

    if len(numbersLessThanGivenNumber) >= 1:
        numberLessThanGivenNumber = numbersLessThanGivenNumber[0]
        for idx in range(len(numbersLessThanGivenNumber) - 1):
            if math.fabs(number - numberLessThanGivenNumber) > math.fabs(number - numbersLessThanGivenNumber[idx + 1]):
                numberLessThanGivenNumber = numbersLessThanGivenNumber[idx + 1]
        numbersClosestToGivenNumber[0] = numberLessThanGivenNumber

    if len(numbersGreaterThanGivenNumber) >= 1:
        numberGreaterThanGivenNumber = numbersGreaterThanGivenNumber[0]
        for idx in range(len(numbersGreaterThanGivenNumber) - 1):
            if math.fabs(number - numberGreaterThanGivenNumber) > math.fabs(
                    number - numbersGreaterThanGivenNumber[idx + 1]):
                numberGreaterThanGivenNumber = numbersGreaterThanGivenNumber[idx + 1]
        numbersClosestToGivenNumber[1] = numberGreaterThanGivenNumber

    return numbersClosestToGivenNumber


numbers1 = [81, -25, -37, -1, 6, 92, 73, 14, -9, -64, -53, -5, 8, -6, 57, -8, 1, 12]
numberClosestToZero = getNumberClosestToZero(numbers1)
print("The number closest to zero is: " + str(numberClosestToZero))

numbers2 = [81, -25, -37, 6, 92, 73, 14, -9, -64, -53, -5, 8, -6, 57, -8, 1, 12]
negPosNumberClosestToZero = getNegPosNumberClosestToZero(numbers2)
print("The numbers closest to zero are: " + str(negPosNumberClosestToZero[0]) + " and " +
      str(negPosNumberClosestToZero[1]) + ".")

numbers3 = [81, -25, -37, -1, 6, 92, 73, 14, -9, -64, -53, 40, -5, 8, -6, 57, -8, 1, 12]
number = 54
numbersClosestToGivenNumber = getNumbersClosestToGivenNumber(numbers3, number)
print("The numbers closest to " + str(number) + " are: " + str(numbersClosestToGivenNumber[0]) + " and " +
      str(numbersClosestToGivenNumber[1]) + ".")
