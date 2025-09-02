import random

def print_board(board):
    for i in board:
        print(i)

def safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def set_queen(board, row):
    if row == n:
        print_board(board)
        return True
    
    for col in random.sample(range(n), n):
        if safe(board, row, col):
            board[row][col] = 1
            if set_queen(board, row + 1):
                return True
            board[row][col] = 0
    return False

n = 8
if __name__ == "__main__":
    while True:
        board = [[0] * n for _ in range(n)]
        if set_queen(board, 0):
            break