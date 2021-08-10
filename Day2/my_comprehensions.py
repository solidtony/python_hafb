#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Make your noise here"""

    # List Comprehensions: [expr(item) for item in iterable]
    # Set comprehensions: (expr(item) for item in iterable)
    s = {i for i in range(10)}
    print(s)
    # Dict Comprehensions: {key_expr:value_expr for item in iterable}
    d = {i: i*2 for i in range(10)}
    print(d)
    # Comprehensions: (item for item in iterable)
    g = (i for i in range(10))
    print(g)

    # Multiple If-Clauses
    points = []
    for x in range(5):
        for y in range(x):
            points.append((x, y))
    print(points)

    points = [(x, y) for x in range(5) for y in range(x)]
    print(points)

    # Version 1: Loops
    values = []
    for x in range(100):
        if x > 50:
            for y in range(100):
                if x-y != 0:
                    values.append(x/(x-y))
    print(values)

    value = [x/(x-y)
             for x in range(100) if x > 50
             for y in range(100) if x-y != 0]
    print(values)

    # Task:
    outer = []
    for x in range(10):
        inner = []
        for y in range(x):
            inner.append((y*3))
        outer.append(inner)
    print(outer)

    outer = [[y*3 for y in range(x)]
             for x in range(10)]
    print(outer)

# --------------------------------------------------
if __name__ == '__main__':
    main()
