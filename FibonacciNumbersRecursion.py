#

# http://code.activestate.com/recipes/410692/
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


def calculateFibonacciNumbers1(sizeFibonacciNumbers, x, y):
    if sizeFibonacciNumbers > 0:
        fibonacciNumbers.append(x)
        x += y
        sizeFibonacciNumbers -= 1
        if sizeFibonacciNumbers > 0:
            fibonacciNumbers.append(y)
            y += x
            sizeFibonacciNumbers -= 1
            if sizeFibonacciNumbers > 0:
                calculateFibonacciNumbers1(sizeFibonacciNumbers, x, y)

    return fibonacciNumbers


def calculateFibonacciNumbers2(sizeFibonacciNumbers, x, y):
    fibonacciCounter = 0
    while sizeFibonacciNumbers > 0 and fibonacciCounter <= 2:
        for case in switch(fibonacciCounter):
            if case(0):
                fibonacciNumbers.append(x)
                x += y
                sizeFibonacciNumbers -= 1
                fibonacciCounter += 1
                break
            if case(1):
                fibonacciNumbers.append(y)
                y += x
                sizeFibonacciNumbers -= 1
                fibonacciCounter += 1
                break
            if case(2):
                calculateFibonacciNumbers2(sizeFibonacciNumbers, x, y)
                fibonacciCounter += 1
                break

    return fibonacciNumbers


x = 0
y = 1
fibonacciNumbers = []
sizeFibonacciNumbers = 9
fibonacciNumbers = calculateFibonacciNumbers1(sizeFibonacciNumbers, x, y)
print(fibonacciNumbers)

x = 0
y = 1
fibonacciNumbers = []
sizeFibonacciNumbers = 8
fibonacciNumbers = calculateFibonacciNumbers1(sizeFibonacciNumbers, x, y)
print(fibonacciNumbers)

x = 0
y = 1
fibonacciNumbers = []
sizeFibonacciNumbers = 7
fibonacciNumbers = calculateFibonacciNumbers2(sizeFibonacciNumbers, x, y)
print(fibonacciNumbers)

x = 0
y = 1
fibonacciNumbers = []
sizeFibonacciNumbers = 10
fibonacciNumbers = calculateFibonacciNumbers2(sizeFibonacciNumbers, x, y)
print(fibonacciNumbers)
