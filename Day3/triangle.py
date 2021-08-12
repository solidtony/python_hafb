#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

import math

class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)

    def __str__(self):
        return f"'{self.args[0]}' for sides {self._sides}"

    def __repr__(self):
        return f'TriangleError {self.args[0]},{self._sides}'

def triangle_area(a, b, c):
    sides = sorted((a,b,c))
    if sides [2] > sides[0] + sides[1]:
        raise TriangleError('Illegal Triangle')
    p=(a+b+c)/2
    a=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return a

# --------------------------------------------------
def main():
    """Make your noise here"""



# --------------------------------------------------
if __name__ == '__main__':
    main()
