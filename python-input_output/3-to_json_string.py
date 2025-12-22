#!/usr/bin/python3
"""Convert a Python object to a JSON string representation."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object."""
    return json.dumps(my_obj)
