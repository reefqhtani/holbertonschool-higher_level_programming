#!/usr/bin/env python3
"""
Extending the Python List with Notifications
"""


class VerboseList(list):
    """
    A list class that prints notifications for modification operations
    """

    def append(self, item):
        """
        Append item to the list and print notification
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend list with items from iterable and print notification
        """
        # Convert to list first to get length, but be careful with generators
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove first occurrence of item and print notification
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop item at index (default last) and print notification
        """
        # Get the item before popping to print it
        item = self[index]
        result = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return result
