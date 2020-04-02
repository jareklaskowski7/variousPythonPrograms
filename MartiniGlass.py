"""
Write the code to support the printing of a martini glass to the console using ASCII characters.
It should support the taking of an integer value that represents the size of martini glass to output.
The output should look like the examples below.

Example Output: PrintGlass(4);
0000000
00000
000
0
|
|
|
|
=======

Example Output: PrintGlass(5);
000000000
0000000
00000
000
0
|
|
|
|
|
=========
"""


def createMartiniGlass(sizeMartiniGlass):
    martiniGlass = str()
    topMartiniGlass = str()
    bottomMartiniGlass = str()
    halfMinusOneCharMartiniGlass = sizeMartiniGlass
    topDiameterMartiniGlass = sizeMartiniGlass * 2 - 1
    currentDiameterMartiniGlass = topDiameterMartiniGlass

    for level in range(sizeMartiniGlass):
        # Top 0
        for adx in range(sizeMartiniGlass - halfMinusOneCharMartiniGlass):
            topMartiniGlass += " "
        halfMinusOneCharMartiniGlass -= 1

        # Top 1
        for bdx in range(currentDiameterMartiniGlass):
            topMartiniGlass += "0"
        topMartiniGlass += "\n"
        currentDiameterMartiniGlass -= 2

        # Bottom 0
        for cdx in range(sizeMartiniGlass - 1):
            bottomMartiniGlass += " "
        bottomMartiniGlass += "|\n"

    # Bottom 1
    for ddx in range(topDiameterMartiniGlass):
        bottomMartiniGlass += "="
    bottomMartiniGlass += "\n"

    martiniGlass += topMartiniGlass
    martiniGlass += bottomMartiniGlass

    return martiniGlass


sizeMartiniGlass = 7
martiniGlass = createMartiniGlass(sizeMartiniGlass)
print(martiniGlass)

sizeMartiniGlass = 15
martiniGlass = createMartiniGlass(sizeMartiniGlass)
print(martiniGlass)
