# https://en.wikipedia.org/wiki/Multinomial_theorem
import sys
import math
from functools import reduce

for line in sys.stdin:
    numerator = math.factorial([int(x) for x in line.split()][0])
    denominator = reduce(
        lambda x, y: x * y,
        map(lambda x: math.factorial(x),
            [int(x) for x in sys.stdin.readline().split()]))
    print(int(numerator / denominator))
