#

def generatePrimeNumbers(numbers):
    primeNumbers = []
    for number in numbers:
        if number > 1:
            times = 1
            for someNumber in range(2, number - 1):
                if times == 1:
                    if number % someNumber == 0:
                        times += 1
                else:
                    break
            if times == 1:
                primeNumbers.append(number)

    return primeNumbers


numbers = list(range(1, 100))
primeNumbers = generatePrimeNumbers(numbers)
print(primeNumbers)
