#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from math import sqrt
from pprint import pprint as pp

def is_prime(x):
    """

    :param x:
    :return:
    """
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# --------------------------------------------------
def main():
    """Review Iterables and Comprehensions"""
    words = "Today I am in class learning python at a slightly higher level.".split()
    print(words)
    totals = [len(word) for word in words if 'a' in word]

    primes = [num for num in range(1000) if is_prime(num)]

    pp(primes)

# --------------------------------------------------
if __name__ == '__main__':
    main()
