#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

def is_even(num):
    return num % 2 == 0


def main():
    print(callable(is_even))
    is_odd = lambda num: num % 2 != 0
    print(callable(is_odd))

# --------------------------------------------------
if __name__ == '__main__':
    main()
