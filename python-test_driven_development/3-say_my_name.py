#!/usr/bin/python3
"""
This module provides a function to print a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>".

    Args:
        first_name: First name (must be a string)
        last_name: Last name (must be a string, defaults to empty string)

    Returns:
        None: Prints to stdout

    Raises:
        TypeError: If first_name or last_name is not a string

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob
    """
    # Validate first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Validate last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    print(f"My name is {first_name} {last_name}")
