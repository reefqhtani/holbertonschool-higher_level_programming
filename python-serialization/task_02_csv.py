#!/usr/bin/env python3
"""Convert CSV data to JSON format and save it to data.json."""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and write the result to data.json.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True if conversion succeeded, otherwise False.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file, indent=4)

        return True
    except (FileNotFoundError, PermissionError, OSError, csv.Error):
        return False
