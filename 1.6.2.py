import sys

field = 0


def printBoard(field, board):
    print("Field #{0}:".format(field))
    for row in board:
        print(*row, sep='')


def increment(board, row, col):
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if (r < 0 or c < 0):
                continue
            if (r >= len(board)) or (c >= len(board[0])):
                continue
            if (board[r][c] == '*'):
                continue
            board[r][c] += 1


for line in sys.stdin:
    rows, cols = [int(x) for x in line.split()]

    if rows == 0 and cols == 0:
        break
    board = [[0] * cols for _ in range(rows)]
    for row in range(0, rows):
        line = sys.stdin.readline()
        for col in range(0, cols):
            if line[col] == '*':
                board[row][col] = '*'

    for row in range(0, rows):
        for col in range(0, cols):
            if board[row][col] == '*':
                increment(board, row, col)

    field += 1
    if field > 1:
        print()

    printBoard(field, board)
