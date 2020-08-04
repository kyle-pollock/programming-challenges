import sys
from fractions import Fraction

for line in sys.stdin:
    target = Fraction(*[int(x) for x in line.split()])
    if target == 1:
        break

    left_most_parent = Fraction(0, 1)
    right_most_parent = 'infinity'
    curr = Fraction(1, 1)
    while (True):
        if target == curr:
            print()
            break
        elif target < curr:
            print('L', end='')
            right_most_parent = curr
            curr = Fraction(
                (left_most_parent.numerator + right_most_parent.numerator),
                (left_most_parent.denominator + right_most_parent.denominator))
        elif target > curr:
            print('R', end='')
            left_most_parent = curr
            if right_most_parent == 'infinity':
                curr = Fraction((left_most_parent.numerator + 1),
                                left_most_parent.denominator)
            else:
                curr = Fraction(
                    (left_most_parent.numerator + right_most_parent.numerator),
                    (left_most_parent.denominator +
                     right_most_parent.denominator))
