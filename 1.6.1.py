import sys

solved = {}

for line in sys.stdin:
    a, b = [int(x) for x in line.split()]
    if a < b:
        i = a
        j = b
    else:
        j = a
        i = b
    max = -1
    for n in range(i, j+1):
        item = n
        count = 0
        while n != 1:
            if n in solved:
                count = count + solved[n]
                break
            else:
                count = count + 1
                if (n % 2) == 0:
                    n = n / 2
                else:
                    n = (n * 3) + 1

        if n == 1:
            count = count + 1
        solved[item] = count
        if count > max:
            max = count
    print("{0} {1} {2}".format(a, b, max))
