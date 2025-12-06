#!/usr/bin/python3
"""
Matrix division module.

This module provides a function to divide all elements
of a matrix by a given number. The function performs
validation on the input matrix and divisor, and returns
a new matrix with results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix: A list of lists containing integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is zero
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(err_msg)

    if len(matrix) == 0:
        raise TypeError(err_msg)

    row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_msg)

        if len(row) == 0:
            raise TypeError(err_msg)

        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(err_msg)

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            msg = "Each row of the matrix must have the same size"
            raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new.append(new_row)

    return new
