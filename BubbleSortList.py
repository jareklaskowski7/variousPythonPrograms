#

def bubbleSortList(numbers):
    for idx in range(len(numbers) - 1):
        for jdx in range(idx + 1, len(numbers)):
            if numbers[idx] > numbers[jdx]:
                tempNumber = numbers[idx]
                numbers[idx] = numbers[jdx]
                numbers[jdx] = tempNumber

    return numbers


numbers = [-3, 4, -10, 0, 7, 23, -19, -37, 41, 49, -52, 63, 27, -28, 0, 23]
# numbers.sort()
numbers = bubbleSortList(numbers)
print(numbers)
