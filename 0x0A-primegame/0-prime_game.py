#!/usr/bin/python3
"""
Contains method to determine the winner of a game
of prime numbers.
"""


def prime_numbers_between(n):
    """
    calculate prime numbers between 1 and n

    Args:
        n (int): the number to calculate prime numbers up to

    Returns:
        int: the number of prime numbers between 1 and n
    """
    prime_numbers = 0

    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers += 1
    return prime_numbers


def isWinner(x, nums):
    """
    Determines the winner of a game of prime numbers.

    Args:
        x (int): the number of rounds to play
        nums (list): the list of numbers n to play

    Returns:
        string: the winner of the game (Ben or Maria)
    """
    if not x or not nums:
        return None
    ben = 0
    maria = 0
    for i in range(x):
        prime_nums = prime_numbers_between(nums[i])
        if prime_nums % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben == maria:
        return None
    winner = "Ben" if ben > maria else "Maria"
    return winner
