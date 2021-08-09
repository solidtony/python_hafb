#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

# --------------------------------------------------
def main():
    r = [6, -2, 10, -18, 99, 234, 94]
    print(r[2::6])
    print(f'len of list {len(r)}')
    print(f'last element of list {r[-1]}')
    # Make a copy of a list
    t = r
    print(f'{t is r}')
    t = r.copy()
    print(f'{t == r}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
