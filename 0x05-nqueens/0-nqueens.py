#!/usr/bin/python3
"""
Contains methods that find the possible solutions to the n-queens can
be placed without them attacking each other(The n-queens problem).
"""
import sys


def is_valid(board, row, col):
    """
    Checks if a position of the queen is valid

    Args:
        board: 2D array representing the board
        row: row of the queen
        col: column of the queen

    Returns:
        Boolean: True if the position is valid, False otherwise
    """
    # Check this row on left side
    if 1 in board[row]:
        return False

    upper_diag = zip(range(row, -1, -1),
                     range(col, -1, -1))
    for i, j in upper_diag:
        if board[i][j] == 1:
            return False

    lower_diag = zip(range(row, len(board), 1),
                     range(col, -1, -1))
    for i, j in lower_diag:
        if board[i][j] == 1:
            return False

    return True


def nqueens_helper(board, col):
    """
    Helper function for nqueens

    Args:
        board: 2D array representing the board
        col: column to start from

    Returns:
        Boolean: True if a solution is found, False otherwise
    """
    if col >= len(board):
        print_board(board, len(board))
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            result = nqueens_helper(board, col + 1)
            if result:
                return True
            board[i][col] = 0
    return False


def print_board(board, n):
    """
    Prints positions of the queens

    Args:
        board: 2D array representing the board
        n: size of the board

    Returns:
        None
    """
    b = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b.append([i, j])
    print(b)


def nqueens(n):
    """
    Finds all possible solutions to the n-queens problem

    Args:
        n: size of the board

    Returns:
        None
    """
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    nqueens_helper(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    queens = sys.argv[1]
    if not queens.isnumeric():
        print("N must be a number")
        exit(1)
    elif int(queens) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(queens))
