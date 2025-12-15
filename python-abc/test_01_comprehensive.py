#!/usr/bin/env python3
"""Comprehensive test for task 01 duck typing"""
from task_01_duck_typing import Circle, Rectangle, shape_info
from abc import ABC, abstractmethod

# Test 1: Basic test from instructions
print("=== Test 1 - Basic test from instructions ===")
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)
shape_info(circle)
shape_info(rectangle)
print()

# Test 2: Edge cases
print("=== Test 2 - Edge cases ===")
circle2 = Circle(radius=0)
rectangle2 = Rectangle(width=0, height=5)
shape_info(circle2)
shape_info(rectangle2)
print()

# Test 3: Other values
print("=== Test 3 - Other values ===")
circle3 = Circle(radius=1)
rectangle3 = Rectangle(width=3, height=3)
shape_info(circle3)
shape_info(rectangle3)
print()

# Test 4: Check if Shape is truly abstract
print("=== Test 4 - Try to instantiate Shape (should fail) ===")
try:
    class TestShape(ABC):
        @abstractmethod
        def area(self):
            pass
        
        @abstractmethod
        def perimeter(self):
            pass
    
    s = TestShape()
    print("ERROR: Should not be able to instantiate abstract class!")
except TypeError as e:
    print(f"GOOD: Got expected error: {e}")
print()

# Test 5: Duck typing test
print("=== Test 5 - Duck typing test ===")
class NotAShape:
    """Class that has area and perimeter but doesn't inherit from Shape"""
    def __init__(self, value):
        self.value = value
    
    def area(self):
        return self.value * 2
    
    def perimeter(self):
        return self.value * 4

not_a_shape = NotAShape(10)
print("Testing duck typing with non-Shape object:")
shape_info(not_a_shape)
