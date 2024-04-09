#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_n_queens(board, row, N):
    if row == N:
        print_solution(board, N)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_n_queens(board, row + 1, N)
            board[row][col] = '.'
            
def print_solution(board, N):
    for row in board:
        print(' '.join(row))
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_n_queens(board, 0, N)

if __name__ == "__main__":
    main()
