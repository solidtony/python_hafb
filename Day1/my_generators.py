#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from math import sqrt

def fibo():
    numbers = []
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        yield numbers[-1]
        continue


def take(count, iterable):
    """
    Take items for the front of the iterable
    :param count: The maximum number or items retrieved
    :param iterable: The source series
    :yield: At most 'count' items for 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """
    Return unique items by eliminating duplicates
    :param iterable: The source series
    :yield: Unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


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
    # Task: Create a list of the first 1 million square numbers
    m_sq = (x*x for x in range(1, 1001))
    l_sq = list(m_sq)
    print(type(m_sq))
    print(type(l_sq))
    print(f'The sum of the first 1000 square numbers is: {sum(l_sq)}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
