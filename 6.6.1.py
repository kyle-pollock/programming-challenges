import sys
import math

golden_ratio = (1 + math.sqrt(5)) / 2
tolerance = 0.001

def isCloseEnough(value):
    return abs(value - round(value)) < tolerance

def fib_approx_term(value):
    if value == 0:
        return 0.5
    if value == 5:
        return value
    if value == 2 or value == 3:
        return value + 1
    if value == 8:
        return 6
    if value == 13:
        return 7
    return math.log(value * math.sqrt(5)) / math.log(golden_ratio)


for line in sys.stdin:
    a, b = sorted([int(x) for x in line.split()])
    if a == 0 and b == 0:
        break
    if a == 0 and b == 1:
        print(1)
        continue

    if a == b:
        if a == 1:
            print(1)
        elif isCloseEnough(fib_approx_term(a)):
            print(1)
        else:
            print(0)
        continue

    lower = fib_approx_term(a)
    if isCloseEnough(lower):
        lower = round(lower)
    else:
        lower = math.ceil(lower)

    higher = fib_approx_term(b)
    if isCloseEnough(higher):
        higher = round(higher)
    else:
        higher = math.floor(higher)

    if a == 0:
        print(higher - lower)
    else:
        print(higher - lower + 1)
