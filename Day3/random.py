#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

import random


def median(iterable):
    """
    Obtain the central value of a series
    Sort the iterable and return the middle value
    if there is an odd number of elements, or the
    arithmetic mean of the middle two elements if
    there is an even number of elements.
    """

    if len(iterable) == 0:
        raise ValueError('median() arg is an empty sequence')

    s = sorted(iterable)
    if len(s) % 2 != 0:
        return (s[len(s)//2] + s[len(s)//2 + 1])/2.
    else:
        return s[len(s)//2 - 1]


def test_median():
    try:
        median([])
    except ValueError as e:
        print(f'{str(e)}')



def lookups():
    s = [1, 4, 5]
    try:
        item = s[5]
    except IndexError: #first
        print('Handled IndexError')

    d = dict(a=65, b = 33)
    try:
        value = d['x']
    #except KeyError:    # is a subclass of LookupError
    except LookupError:    #first
        print('Handled KeyError')


# --------------------------------------------------
def main():
    """Make your noise here"""

    number = random.randrange(5)
    while True:
        try:
            guess = int(input('guess number'))
        except ValueError:
            continue
        if guess == number:
            print("Guess was correct!")
            break


# --------------------------------------------------
if __name__ == '__main__':
    test_median()
