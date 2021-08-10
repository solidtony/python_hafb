#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def main():
    m = map(ord, 'The purple Weber State')
    print(m)
    print(next(m))
    print(next(m))


# --------------------------------------------------
if __name__ == '__main__':
    main()
