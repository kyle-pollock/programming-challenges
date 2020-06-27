import sys

game = 0
newBoard = True

def printBoard(board):
    for row in board:
        print(*row, sep='')

def checkBlackTopLeft(board, row, col):
    row -= 1
    col -= 1
    while board[row][col] == '.':
        row -= 1
        col -= 1
    return board[row][col] in [ 'B', 'Q' ]


def checkBlackTop(board, row, col):
    row -= 1
    while board[row][col] == '.':
        row -= 1
    return board[row][col] in [ 'Q', 'R']

def checkBlackTopRight(board, row, col):
    row -= 1
    col += 1
    while board[row][col] == '.':
        row -= 1
        col += 1
    return board[row][col] in [ 'B', 'Q']

def checkBlackLeft(board, row, col):
    col -= 1
    while board[row][col] == '.':
        col -= 1
    return board[row][col] in [ 'R', 'Q']

def checkBlackRight(board, row, col):
    col += 1
    while board[row][col] == '.':
        col += 1
    return board[row][col] in [ 'R', 'Q']

def checkBlackBottomLeft(board, row, col):
    row += 1
    col -= 1
    if board[row][col] == 'P':
        return True

    while board[row][col] == '.':
        row += 1
        col -= 1
    return board[row][col] in [ 'B', 'Q']

def checkBlackBottom(board, row, col):
    row += 1
    while board[row][col] == '.':
        row += 1
    return board[row][col] in [ 'Q', 'R']

def checkBlackBottomRight(board, row, col):
    row += 1
    col += 1
    if board[row][col] == 'P':
        return True
    while board[row][col] == '.':
        row += 1
        col += 1
    return board[row][col] in [ 'B', 'Q']

def checkBlackKnights(board, row, col):
    if board[row - 2][col - 1] == 'N':
        return True
    if board[row - 2][col + 1] == 'N':
        return True
    if board[row - 1][col - 2] == 'N':
        return True
    if board[row - 1][col + 2] == 'N':
        return True
    if board[row + 1][col - 2] == 'N':
        return True
    if board[row + 1][col + 2] == 'N':
        return True
    if board[row + 2][col - 1] == 'N':
        return True
    if board[row + 2][col + 1] == 'N':
        return True

    return False


#WHITE
def checkWhiteTopLeft(board, row, col):
    row -= 1
    col -= 1
    if board[row][col] == 'p':
        return True
    while board[row][col] == '.':
        row -= 1
        col -= 1
    return board[row][col] in [ 'b', 'q']


def checkWhiteTop(board, row, col):
    row -= 1
    while board[row][col] == '.':
        row -= 1
    return board[row][col] in [ 'q', 'r']

def checkWhiteTopRight(board, row, col):
    row -= 1
    col += 1
    if board[row][col] == 'p':
        return True
    while board[row][col] == '.':
        row -= 1
        col += 1
    return board[row][col] in [ 'b', 'q']

def checkWhiteLeft(board, row, col):
    col -= 1
    while board[row][col] == '.':
        col -= 1
    return board[row][col] in [ 'r', 'q']

def checkWhiteRight(board, row, col):
    col += 1
    while board[row][col] == '.':
        col += 1
    return board[row][col] in [ 'r', 'q']

def checkWhiteBottomLeft(board, row, col):
    row += 1
    col -= 1
    while board[row][col] == '.':
        row += 1
        col -= 1
    return board[row][col] in [ 'b', 'q']

def checkWhiteBottom(board, row, col):
    row += 1
    while board[row][col] == '.':
        row += 1
    return board[row][col] in [ 'q', 'r']

def checkWhiteBottomRight(board, row, col):
    row += 1
    col += 1
    while board[row][col] == '.':
        row += 1
        col += 1
    return board[row][col] in [ 'b', 'q']

def checkWhiteKnights(board, row, col):
    if board[row - 2][col - 1] == 'n':
        return True
    if board[row - 2][col + 1] == 'n':
        return True
    if board[row - 1][col - 2] == 'n':
        return True
    if board[row - 1][col + 2] == 'n':
        return True
    if board[row + 1][col - 2] == 'n':
        return True
    if board[row + 1][col + 2] == 'n':
        return True
    if board[row + 2][col - 1] == 'n':
        return True
    if board[row + 2][col + 1] == 'n':
        return True

    return False


def checkBlackKing(board, row, col):
    if checkBlackKnights(board, row, col):
        return True
    if checkBlackTopLeft(board, row, col):
        return True
    if checkBlackTop(board, row, col):
        return True
    if checkBlackTopRight(board, row, col):
        return True
    if checkBlackLeft(board, row, col):
        return True
    if checkBlackRight(board, row, col):
        return True
    if checkBlackBottomLeft(board, row, col):
        return True
    if checkBlackBottom(board, row, col):
        return True
    if checkBlackBottomRight(board, row, col):
        return True
    return False

def checkWhiteKing(board, row, col):
    if checkWhiteKnights(board, row, col):
        return True

    if checkWhiteTopLeft(board, row, col):
        return True
    if checkWhiteTop(board, row, col):
        return True
    if checkWhiteTopRight(board, row, col):
        return True
    if checkWhiteLeft(board, row, col):
        return True
    if checkWhiteRight(board, row, col):
        return True
    if checkWhiteBottomLeft(board, row, col):
        return True
    if checkWhiteBottom(board, row, col):
        return True
    if checkWhiteBottomRight(board, row, col):
        return True
    return False

def isEmpty(board):
    for row in range(12):
        for col in range(12):
            if board[row][col] in ['p', 'r', 'b', 'q', 'k', 'n', 'P', 'R', 'B', 'Q', 'K', 'N',]:
                return False
    return True


def checkKings(board):

    for row in range(12):
        for col in range(12):
            if board[row][col] == 'k':
                if checkBlackKing(board, row, col):
                    print("Game #{0}: black king is in check.". format(game))
                    return

            if board[row][col] == 'K':
                if checkWhiteKing(board, row, col):
                    print("Game #{0}: white king is in check.". format(game))
                    return
    print("Game #{0}: no king is in check.". format(game))


for line in sys.stdin:
    line = line.strip()

    if newBoard:
        game += 1
        board = []
        board.append(['@' for c in range(12)])
        board.append(['@' for c in range(12)])
        newBoard = False

    elif len(line) == 0:
        board.append(['@' for c in range(12)])
        board.append(['@' for c in range(12)])
        if not isEmpty(board):
            printBoard(board)
            checkKings(board)
            newBoard = True
        else:
            break;
        continue

    board.append([c for c in '@@' + line + '@@'])

board.append(['@' for c in range(12)])
board.append(['@' for c in range(12)])
printBoard(board)

