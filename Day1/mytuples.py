#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose: Review tuples
"""

import argparse

def minmax(items):
    """
    Return the maximum and minimum of the collection
    :param items: collection of objects
    :return: min and max
    """
    return min(items), max(items)


def main():
    """Make your noise here"""
    # A tuple of any kind of object
    t = ("Ogden", 1.99, 2)
    print(f'Tuple is {len(t)} items long')
    print(t[0])
    print(t[1])
    for item in t:
        print(type(item))

    a = ((1, 2), (10, 20), (100, 200), "yo yo")
    for itemFirst in a:
        print('---')
        for itemSecond in itemFirst:
            print(itemSecond)

    minmax(items)


# --------------------------------------------------
if __name__ == '__main__':
    # main()
    items = (3, 88, 11, 22, 33)
    lower, upper = minmax(items)
    print(f'minimum {lower} and maximum {upper}')
    # Test for memebership: in, not in
    if 3 in items:
        print("I have a 3")