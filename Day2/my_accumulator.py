#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Make your noise here"""

    accumulator = operator.add(positives[0], positives[1])
    for item in numbers[2:]:
        accumulator = operator.add(accumulator, item)
    print(accumulator)
    # Use reduce
    print(reduce operator.add, positives)


# --------------------------------------------------
if __name__ == '__main__':
    main()
