#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """fewest number of operations needed to result in
    exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    root = 2
    mop = 0
    while n > 1:
        if n % root == 0:
            mop += root
            n = n / root
        else:
            root += 1

    return mop
