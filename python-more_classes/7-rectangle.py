#!/usr/bin/python3
"""
Module 7-rectangle
Defines a Rectangle class that tracks instances and uses custom print symbols.
"""


class Rectangle:
    """
    Class that defines a rectangle with width, height,
    instance counting, and configurable print symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle and increment instance counter.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter (0 if width or height is 0)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return rectangle as a string made of print_symbol.

        Returns empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string representation usable by eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print message when instance is deleted and decrement counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
