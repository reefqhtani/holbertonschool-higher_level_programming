#!/usr/bin/python3
"""
Text Indentation Module

This module provides a function that prints text with 2 new lines
after each '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None: This function only prints the formatted text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return

    i = 0
    length = len(text)
    result = ""

    # Skip leading spaces
    while i < length and text[i] == ' ':
        i += 1

    while i < length:
        result += text[i]

        if text[i] in ".?:":
            result += "\n\n"
            i += 1

            # Skip ALL whitespace characters (space, tab, newline)
            while i < length and text[i] in " \t\n":
                i += 1

            # If next char is also a separator, add it without new lines
            # This handles cases like "..."
            while i < length and text[i] in ".?:":
                result += text[i]
                i += 1

            continue

        i += 1

    # Remove trailing spaces from each line and print
    lines = result.split('\n')
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            # Last line - strip trailing spaces
            print(line.rstrip(), end="")
        else:
            # Not last line - strip trailing spaces and print with newline
            print(line.rstrip())
