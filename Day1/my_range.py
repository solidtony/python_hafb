#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Make your noise here"""
    r = range(1, 5)
    for item in r:
        print(item)

    # Enumerate
    t = [1, 2, 5, 6, 7]
    for i, v in enumerate(t):
        print(f'Index {i}, value {v}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
