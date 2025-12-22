#!/usr/bin/python3
"""Add command-line arguments to a list and save them in add_item.json."""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Load list, add argv items, then save back to add_item.json."""
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
