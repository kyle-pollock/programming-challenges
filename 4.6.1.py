import sys
from statistics import median

cases = int(sys.stdin.readline())
for case in range(cases):
    line = [int(x) for x in sys.stdin.readline().split()]
    num_relatives = int(line.pop(0))
    street_numbers = line
    m = int(median(street_numbers))
    sum = 0
    for street in street_numbers:
        sum += abs(m - street)
    print(sum)
