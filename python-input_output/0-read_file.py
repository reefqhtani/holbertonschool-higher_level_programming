#!/usr/bin/python3
"""Read and print a UTF-8 text file to stdout."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
