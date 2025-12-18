#!/usr/bin/env python3
"""
Module for demonstrating duck typing with abstract shapes.

This module implements an abstract Shape class and concrete implementations
for Circle and Rectangle, along with a shape_info function that uses duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area (π * r²)
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        
        Returns:
            float: The perimeter (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle with given width and height.
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (width * height)
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            float: The perimeter (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter information for a shape using duck typing.
    
    This function relies on duck typing - it doesn't check the type of the
    shape object, but simply calls its area() and perimeter() methods.
    Any object that implements these methods can be passed to this function.
    
    Args:
        shape: Any object that implements area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
