#

def calculateFactorialNumber(number):
    if number == 0 or number == 1:
        return 1
    return calculateFactorialNumber(number - 1) * number


number = 7
print(calculateFactorialNumber(number))
