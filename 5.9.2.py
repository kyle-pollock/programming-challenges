import sys
import math


def isPalindrome(number):
    s = str(number)
    r = s[::-1]

    middle = math.floor(len(s) / 2)
    left = s[:middle]
    right = r[:middle]

    return left == right


for case in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())

    for i in range(1000):
        reverse = int(str(number)[::-1])
        number += reverse

        if isPalindrome(number):
            print(f'{i+1} {number}')
            break
