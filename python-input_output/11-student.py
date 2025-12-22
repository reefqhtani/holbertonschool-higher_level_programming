#!/usr/bin/python3
"""Define a Student class that can serialize to dict and reload attributes."""


class Student:
    """Represent a student with basic public attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation, optionally filtered by attrs."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes using key/value pairs from a dict."""
        for key, value in json.items():
            setattr(self, key, value)
