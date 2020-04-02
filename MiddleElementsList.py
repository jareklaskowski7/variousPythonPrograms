#

def findMiddleElementList(lst):
    halfSize = int(len(lst) / 2)
    middleElementsList = []
    if halfSize * 2 == len(lst):
        middleElementsList.append(lst[halfSize - 1])
        middleElementsList.append(lst[halfSize])
    else:
        middleElementsList.append(lst[halfSize])

    return middleElementsList


lst = [7, 4, 16, 9, 28, 17, 35]
middleElementsList = findMiddleElementList(lst)
print(middleElementsList)

lst = [7, 4, 16, 9, 56, 28, 17, 35]
middleElementsList = findMiddleElementList(lst)
print(middleElementsList)
