#!/usr/bin/python3
"""N-Queens problem solver"""

import sys


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursive backtracking function to find all solutions."""
    if row == n:
        # Found a solution; add it to solutions list
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1  # Reset the row


def print_solutions(solutions):
    """Print each solution in the specified format."""
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Input validation
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

    # Initialize board and list to store solutions
    board = [-1] * N
    solutions = []

    # Solve the N-Queens problint the solutions
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)
