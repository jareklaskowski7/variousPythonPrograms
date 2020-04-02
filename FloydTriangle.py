"""
Note- Floyd Triangle is like
1
2 3
4 5 6
7 8 9 10
"""


def createFloydTriangle(floydTriangleHeight):
    floydTriangle = str()
    rowContent = [1]

    for idx in range(floydTriangleHeight):
        for jdx in range(len(rowContent)):
            floydTriangle += str(rowContent[jdx])
            if jdx != len(rowContent) - 1:
                floydTriangle += " "
        floydTriangle += "\n"

        rowContent.append(rowContent[- 1] + 1)
        for kdx in range(len(rowContent)):
            rowContent[kdx] = rowContent[-1] + kdx

    return floydTriangle


sizeFloydTriangle = 7
floydTriangle = createFloydTriangle(sizeFloydTriangle)
print(floydTriangle)

sizeFloydTriangle = 10
floydTriangle = createFloydTriangle(sizeFloydTriangle)
print(floydTriangle)
