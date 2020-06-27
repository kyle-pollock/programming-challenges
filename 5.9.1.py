import sys
import math

for line in sys.stdin:
    a, b = [int(x) for x in line.split()]
    if a == 0 and b == 0:
        break
    count = 0
    carry = 0
    while a != 0 or b != 0:
        if carry + (a % 10) + (b % 10) > 9:
            count += 1
            carry = 1
        else:
            carry = 0
        a = math.floor(a / 10)
        b = math.floor(b / 10)

    if count == 0:
        print('No carry operation.')
    elif count == 1:
        print('1 carry operation.')
    else:
        print(f'{count} carry operations.')
