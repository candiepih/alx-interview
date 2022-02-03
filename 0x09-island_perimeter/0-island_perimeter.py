#!/usr/bin/python3
"""
Contains a method that returns the perimeter of the
island described in grid
"""


def check_perimeter(grid, i, j):
    """
    check surroundings for water. If water body
    on boundary, add 1 to perimeter otherwise add 0
    """
    top = grid[i - 1][j] ^ 1
    bottom = grid[i + 1][j] ^ 1
    left = grid[i][j - 1] ^ 1
    right = grid[i][j + 1] ^ 1
    total = top + bottom + left + right
    return total


def island_perimeter(grid):
    """
    Calculates the perimeter of an island given a grid

    Args:
        grid (list): list of lists of integers

    Returns:
        int: perimeter of island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 1:
                continue
            p = check_perimeter(grid, i, j)
            if perimeter > 1 and p == 4:
                return 0
            perimeter += p

    return perimeter
