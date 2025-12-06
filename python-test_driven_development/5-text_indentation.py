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

    Examples:
        >>> text_indentation("Hello. World? Good: Morning")
        Hello.
        <BLANKLINE>
        World?
        <BLANKLINE>
        Good:
        <BLANKLINE>
        Morning
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return

    # Remove leading and trailing spaces
    text = text.strip()

    i = 0
    length = len(text)

    while i < length:
        # Print current character
        print(text[i], end="")

        # Check if current character is a separator
        if text[i] in ".?:":
            # Print two new lines
            print("\n")

            # Skip any spaces immediately after the separator
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue

        i += 1
