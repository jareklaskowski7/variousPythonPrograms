#

def createTriangle01(triangle01Height):
    triangle01 = str()
    x = 0
    for rowNum in range(triangle01Height):
        for rowLength in range(rowNum + 1):
            triangle01 += str(x)
            if x == 0:
                x = 1
            else:
                x = 0
        triangle01 += "\n"

    return triangle01


triangle01Height = 7
triangle01 = createTriangle01(triangle01Height)
print(triangle01)

triangle01Height = 10
triangle01 = createTriangle01(triangle01Height)
print(triangle01)
