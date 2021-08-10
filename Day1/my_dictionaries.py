#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Review dictionaries"""
    urls = {'Google': 'http://google.com',
            'Twitter': 'http://twitter.com',
            'WSU': 'http://weber.edu'}
    print(type(urls))
    print(urls)
    print(urls['Google'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
