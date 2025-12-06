#!/usr/bin/python3
"""
This module provides a function to print text with special indentation.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text: The text to process (must be a string)

    Returns:
        None: Prints the processed text to stdout

    Raises:
        TypeError: If text is not a string

    Examples:
        >>> text_indentation("Hello. World")
        Hello.
        World
        >>> text_indentation("How are you? I'm fine.")
        How are you?
        I'm fine.
    """
    # Validate text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process the text
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            # Skip any spaces immediately after the separator
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print the result, stripping trailing spaces from each line
    lines = result.split('\n')
    for line in lines:
        print(line.rstrip())
