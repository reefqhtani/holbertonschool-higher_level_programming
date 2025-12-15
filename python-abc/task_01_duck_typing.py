#!/usr/bin/env python3
"""Shapes, interfaces, and duck typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Return area of shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Return perimeter of shape"""
        pass


class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        """Initialize with radius"""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius
    
    def area(self):
        """Calculate area: πr²"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate perimeter (circumference): 2πr"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        """Initialize with width and height"""
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("width and height must be numbers")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area: width × height"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter: 2(width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter using duck typing
    
    Args:
        shape: Any object with area() and perimeter() methods
    """
    # Pure duck typing - no type checking!
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
