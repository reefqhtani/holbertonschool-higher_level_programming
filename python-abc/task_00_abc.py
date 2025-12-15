#!/usr/bin/env python3
"""Defines an abstract Animal class and concrete Dog/Cat subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class implementing Animal's interface."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class implementing Animal's interface."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
