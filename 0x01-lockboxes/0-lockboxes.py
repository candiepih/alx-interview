#!/usr/bin/python3
"""Lockboxes
Contains method that finds the keys to open other lockboxes
"""


def canUnlockAll(boxes):
    """
    Function that determines if you can open all the lockboxes
    Args:
        boxes: list of lists of integers
    Returns:
        True if you can open all the lockboxes, False otherwise
    """
    keys = list(range(1, len(boxes)))
    print(keys)
    for i in range(len(boxes)):
        for key in keys:
            if key in boxes[i]:
                keys.remove(key)
    if len(keys) == 0:
        return True
    return False
