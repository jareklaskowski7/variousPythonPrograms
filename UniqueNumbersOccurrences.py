#

def findUniqueNumbersOccurrences(numbers):
    uniqueNumbersOccurrences = {}
    for number in numbers:
        if not number in uniqueNumbersOccurrences:
            uniqueNumbersOccurrences[number] = 1
        else:
            uniqueNumbersOccurrences[number] += 1

    return uniqueNumbersOccurrences


numbers = [52, 8, 65, 0, 1, 4, -43, 3, 5, 7, 0, 65, -32, 1, 65, 0, -8, 987, 68, 0, 25]
uniqueNumbersOccurrences = findUniqueNumbersOccurrences(numbers)
print("More than one number occurrence:")
for key, value in uniqueNumbersOccurrences.items():
    if value > 1:
        print("\nNumber of occurrences: " + str(value) + " of number " + str(key))
