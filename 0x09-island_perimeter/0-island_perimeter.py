#!/usr/bin/python3
"""
Module that defines the island_perimeter function.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the given grid.

    Args:
        grid (list of list of int): The grid representing the map,
                                    where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four directions (top, bottom, left, right)
                # Add to the perimeter if the cell is on the edge or next to water
                if i == 0 or grid[i - 1][j] == 0:  # Top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
