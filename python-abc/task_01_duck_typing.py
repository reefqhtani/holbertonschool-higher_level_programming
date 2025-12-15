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
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
