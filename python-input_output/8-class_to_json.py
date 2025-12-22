#!/usr/bin/python3
"""Return a dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary representation of a simple-serializable object."""
    return obj.__dict__
