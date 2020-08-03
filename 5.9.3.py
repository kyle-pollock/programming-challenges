import sys
import math

# n * (10**k) <= E**2 < (n+1) * (10**k)
for number_str in sys.stdin:
    number_str = number_str.strip()
    number_length = len(number_str)
    number = int(number_str)

    # let k be the number of RHS digits
    k = number_length + 1

    found = False
    while not found:

        low = math.log(number, 2) + (k * math.log(10, 2))
        high = math.log(number + 1, 2) + (k * math.log(10, 2))

        if int(low) < int(high):
            print(math.ceil(low))
            break
        k += 1
