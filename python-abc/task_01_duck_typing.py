#!/usr/bin/env python3
"""Shapes, interfaces, and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Return area of circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize rectangle width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
