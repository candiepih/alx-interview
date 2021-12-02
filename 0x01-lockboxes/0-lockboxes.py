#!/usr/bin/python3
"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""


def canUnlockAll(boxes):
    """
    Function that determines if you can open all the lockboxes
    Args:
        boxes: list of lists of integers
    Returns:
        True if you can open all the lockboxes, False otherwise
    """
    unlocked = {}

    for box_id, box in enumerate(boxes):
        if len(box) == 0 or box_id == 0:
            unlocked[box_id] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != box_id:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
    return False
