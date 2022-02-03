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
    mask = 1
    top = grid[i - 1][j] ^ mask if i > 0 else 1
    bottom = grid[i + 1][j] ^ mask if i < (len(grid) - 1) else 1
    left = grid[i][j - 1] ^ mask if j > 0 else 1
    right = grid[i][j + 1] ^ mask if j < (len(grid[i]) - 1) else 1
    positions = top + bottom + right + left
    return positions


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
            if grid[i][j] == 1:
                perimeter += check_perimeter(grid, i, j)

    return perimeter
