from itertools import product


def solution(board):
    answer = 0
    mine = set()
    ysize = len(board)
    xsize = len(board[0])
    for i in range(ysize):
        for j in range(xsize):
            if board[i][j]: mine.add((i, j))

    while mine:
        y, x = mine.pop()
        dlist = product([-1, 0, 1], repeat=2)
        for dy, dx in dlist:
            ty, tx = y + dy, x + dx
            if 0 <= tx and tx < xsize:
                if 0 <= ty and ty < ysize:
                    board[ty][tx] = 1

    for col in board:
        answer += col.count(0)

    return answer