import sys
import math

for line in sys.stdin:
    n = int(line)

    while n > 1:
        winning_high = n - 1
        winning_low = math.ceil(n / 9)

        losing_high = winning_low - 1
        losing_low = math.ceil(n / 9 / 2)

        if winning_low == 1:
            print("Stan wins.")
            break

        if losing_low == 1:
            print("Ollie wins.")
            break

        n = losing_low
