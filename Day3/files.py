#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

import sys


# --------------------------------------------------
def main():
    """Make your noise here"""
    print(sys.getdefaultencoding())
    f = open('wasteland.txt', mode='wt', encoding='utf-8')
    print(type(f))

    f.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
