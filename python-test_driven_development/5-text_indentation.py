#!/usr/bin/python3
"""
Text Indentation Module

This module provides a function that prints text with 2 new lines
after each '.', '?', and ':' characters.
"""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1
            # Skip ONLY spaces
            while i < n and text[i] == " ":
                i += 1
            continue

        i += 1
