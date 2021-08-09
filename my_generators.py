#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


def gen246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About ot return')


def gen123():
    yield 1
    yield 2
    yield 3


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('Iterable is empty')

# --------------------------------------------------
def main():
    """Review Iterator and Generators"""
    #iterable = ['spring', 'summer', 'fall', 'winter']
    #iterator = iter(iterable)

    g = gen123()
    for v in gen123():
        print(f'Value is {v}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
