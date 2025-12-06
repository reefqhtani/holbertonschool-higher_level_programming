#!/usr/bin/python3
"""
This module provides a function to print a square with # characters.
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
        size: Size length of the square (must be a non-negative integer)

    Returns:
        None: Prints the square to stdout

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(1)
        #
    """
    # Check if size is an integer or a float that represents an integer
    if isinstance(size, float):
        # Check if float is negative (special case from requirements)
        if size < 0:
            raise TypeError("size must be an integer")
        # Check if float represents an integer (e.g., 4.0 but not 4.5)
        if size != int(size):
            raise TypeError("size must be an integer")
        # Convert to int for the rest of the function
        size = int(size)
    elif not isinstance(size, int):
        # Not an int or float
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
