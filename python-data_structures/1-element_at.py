#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list at a specific index.
    
    Args:
        my_list: The list to retrieve from
        idx: The index position to retrieve
        
    Returns:
        The element at index idx, or None if idx is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
