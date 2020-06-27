import sys

def topColumn(s, c):
    if c in [1, 4]:
        print(' ' * (s + 2), end='')
    else:
        print(' ' + ('-' * s) + ' ', end='')

def midColumn(s, c):
    if c in [1, 7, 0]:
        print(' ' * (s + 2), end='')
    else:
        print(' ' + ('-' * s) + ' ', end='')

def bottomColumn(s, c):
    if c in [1, 4, 7]:
        print(' ' * (s + 2), end='')
    else:
        print(' ' + ('-' * s) + ' ', end='')

def topRows(s, c):
    if c in [5, 6]:
        print('|' + ' ' * (s + 1), end='')
    elif c in [1, 2, 3, 7]:
        print(' ' * (s + 1) + '|', end='')
    else:
        print('|' + ' ' * s + '|', end='')

def bottomRows(s, c):
    if c in [2]:
        print('|' + ' ' * (s + 1), end='')
    elif c in [1, 3, 4, 5, 7, 9]:
        print(' ' * (s + 1) + '|', end='')
    else:
        print('|' + ' ' * s + '|', end='')

for line in sys.stdin:
    s, n = [int(x) for x in line.split()]

    if s == 0 and n == 0:
        break;

    string = str(n)

    first = True;
    for c in string:
        if first:
            first = False
        else:
            print(' ', end='')
        topColumn(s, int(c))
    print()

    for i in range(0, s):
        first = True;
        for c in string:
            if first:
                first = False
            else:
                print(' ', end='')
            topRows(s, int(c))
        print()

    first = True;
    for c in string:
        if first:
            first = False
        else:
            print(' ', end='')
        midColumn(s, int(c))
    print()

    for i in range(0, s):
        first = True;
        for c in string:
            if first:
                first = False
            else:
                print(' ', end='')
            bottomRows(s, int(c))
        print()

    first = True;
    for c in string:
        if first:
            first = False
        else:
            print(' ', end='')
        bottomColumn(s, int(c))
    print()
    print()
