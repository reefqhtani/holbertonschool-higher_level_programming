#!/usr/bin/python3
"""
Module 6-square
Defines a Square class with size, position, area, and print functionality.
"""


class Square:
    """
    Class that defines a square with size and position attributes.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).
    position (tuple): A tuple of 2 positive integers (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The (x, y) position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with '#' characters, using position for alignment.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Print each row of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
