#!/usr/bin/env python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been iterated
    """
    
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable
        
        Args:
            iterable: Any iterable object (list, tuple, etc.)
        """
        self.iterator = iter(iterable)  # Get the iterator from the iterable
        self.count = 0  # Initialize counter to 0
    
    def get_count(self):
        """
        Return the current count of items iterated
        
        Returns:
            int: Number of items iterated so far
        """
        return self.count
    
    def __next__(self):
        """
        Get the next item from the iterator and increment the counter
        
        Returns:
            The next item from the iterator
            
        Raises:
            StopIteration: When there are no more items
        """
        try:
            item = next(self.iterator)  # Get next item from wrapped iterator
            self.count += 1  # Increment counter
            return item
        except StopIteration:
            # Re-raise StopIteration to maintain normal iterator behavior
            raise
    
    def __iter__(self):
        """
        Return self to make CountedIterator iterable
        
        Returns:
            CountedIterator: self
        """
        return self
