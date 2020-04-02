"""
Write a program to identify common elements or numbers between two given arrays.
You should not use any inbuilt methods are list to find common values.
"""


def findCommonElementsTwoLists(lst1, lst2):
    commonElementsTwoLists = []
    for idx in lst1:
        for jdx in lst2:
            if idx == jdx:
                commonElementsTwoLists.append(idx)

    return commonElementsTwoLists


lst1 = [4, 8, 2, 9, 7, 1]
lst2 = [3, 6, 8, 9, 2, 5]

commonElementsTwoLists = findCommonElementsTwoLists(lst1, lst2)
print(commonElementsTwoLists)
