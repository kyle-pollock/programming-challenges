import sys
import copy

def drawRectangle(bitmap, x1, y1, x2, y2, color):
    for row in range(y1, y2+1):
        for col in range(x1, x2+1):
            bitmap[row][col] = color


def createBitmap(m, n):
    matrix = [[ 1 for x in range(0, m+2)] for y in range(0, n+2)]
    for row in range(1, n+1):
        for col in range(1, m+1):
            matrix[row][col] = 'O'
    return matrix


def renderBitmap(bitmap):
    for row in bitmap[1:-1]:
        print(*row[1:-1], sep="")

def fill(bitmap, x, y, color):
    cache = {}
    stack = []
    originalBitmap = copy.deepcopy(bitmap)
    originalColor = bitmap[y][x]

    stack.append((x,y))

    while stack:
        xx, yy = stack.pop()
        key = "{0}-{1}".format(xx,yy)
        if key in cache:
            continue
        cache[key] = True

        if originalBitmap[yy][xx] != originalColor:
            continue
        bitmap[yy][xx] = color
        stack.append((xx-1, yy-1))
        stack.append((xx, yy-1))
        stack.append((xx+1, yy-1))

        stack.append((xx-1, yy))
        stack.append((xx, yy))
        stack.append((xx+1, yy))

        stack.append((xx-1, yy+1))
        stack.append((xx, yy+1))
        stack.append((xx+1, yy+1))


for line in sys.stdin:
    tokens = line.split()

    if tokens[0] == 'I':
        m = int(tokens[1])
        n = int(tokens[2])
        bitmap = createBitmap(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == 'C':
        drawRectangle(bitmap, 1, 1, m, n, 'O')
    elif tokens[0] == 'L':
        drawRectangle(bitmap, int(tokens[1]), int(tokens[2]), int(tokens[1]), int(tokens[2]), tokens[3])
    elif tokens[0] == 'V':
        if int(tokens[2]) < int(tokens[3]):
            y1 = int(tokens[2])
            y2 = int(tokens[3])
        else:
            y2 = int(tokens[2])
            y1 = int(tokens[3])
        drawRectangle(bitmap, int(tokens[1]), y1, int(tokens[1]), y2, tokens[4])
    elif tokens[0] == 'H':
        if int(tokens[1]) < int(tokens[2]):
            x1 = int(tokens[1])
            x2 = int(tokens[2])
        else:
            x2 = int(tokens[1])
            x1 = int(tokens[2])
        drawRectangle(bitmap, x1, int(tokens[3]), x2, int(tokens[3]), tokens[4])

    elif tokens[0] == 'K':
        if int(tokens[1]) < int(tokens[3]):
            x1 = int(tokens[1])
            x2 = int(tokens[3])
        else:
            x2 = int(tokens[1])
            x1 = int(tokens[3])
        if int(tokens[2]) < int(tokens[4]):
            y1 = int(tokens[2])
            y2 = int(tokens[4])
        else:
            y2 = int(tokens[2])
            y1 = int(tokens[4])
        drawRectangle(bitmap, x1, y1, x2, y2, tokens[5])

    elif tokens[0] == 'F':
        fill(bitmap, int(tokens[1]), int(tokens[2]), tokens[3])
    elif tokens[0] == 'S':
        print(tokens[1])
        renderBitmap(bitmap)
    elif tokens[0] == 'X':
        break
