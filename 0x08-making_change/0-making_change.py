#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest coins to meet total

    Args:
        coins (list): list of coins
        total (int): value to meet as total

    Returns:
        coins (int): fewest number of coins needed to meet total
        (0) if total is 0 or less
        (-1) if no number of the coins can meet the total
    """
    if total <= 0:
        return 0
    min_coins = [0] + [float('inf')] * total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                num_coins = min_coins[i - coin] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    if min_coins[-1] == float("inf"):
        return -1
    return min_coins[total]
