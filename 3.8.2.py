import sys

cases = int(sys.stdin.readline())

def check(grid, word, i, j, direction):
    if len(word) == 0:
        return True

    if direction == "TL" and grid[i - 1][j - 1] == word[0]:
        return check(grid, word[1:], i-1, j-1, direction)
    elif direction == "T" and grid[i - 1][j] == word[0]:
        return check(grid, word[1:], i-1, j, direction)
    elif direction == "TR" and grid[i - 1][j+1] == word[0]:
        return check(grid, word[1:], i-1, j+1, direction)

    elif direction == "L" and grid[i][j-1] == word[0]:
        return check(grid, word[1:], i, j-1, direction)
    elif direction == "R" and grid[i][j+1] == word[0]:
        return check(grid, word[1:], i, j+1, direction)

    elif direction == "BL" and grid[i + 1][j + 1] == word[0]:
        return check(grid, word[1:], i+1, j+1, direction)
    elif direction == "B" and grid[i + 1][j] == word[0]:
        return check(grid, word[1:], i+1, j, direction)
    elif direction == "BR" and grid[i + 1][j+1] == word[0]:
        return check(grid, word[1:], i+1, j+1, direction)

    else:
        return False

def getCoordinates(grid, word):
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if word[0] != grid[i][j]:
                continue
            if check(grid, word[1:], i, j, "TL") or check(grid, word[1:], i, j, "T") or check(grid, word[1:], i, j, "TR") or check(grid, word[1:], i, j, "L") or check(grid, word[1:], i, j, "R") or check(grid, word[1:], i, j, "BL") or check(grid, word[1:], i, j, "B") or check(grid, word[1:], i, j, "BR"):
                return i, j
    return 0, 0

for case in range(cases):
    sys.stdin.readline()
    if case > 0:
        print()

    m, n = [int(x) for x in sys.stdin.readline().strip().split()]

    grid = [ ['@'] * (n+2) for x in range(m+2) ]

    for i in range(m):
        line = sys.stdin.readline().strip()
        for j in range(n):
            grid[i+1][j+1] = line[j].lower()

    for i in range(int(sys.stdin.readline())):
        word = sys.stdin.readline().strip().lower()
        print(*getCoordinates(grid, word))
