#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

import sys
sys.path.append('../Day1')
from itertools import islice, count
from my_comprehension import is_prime

# --------------------------------------------------
def main():
    # Task: Create a list of the first 1000 prime numbers
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(f'The sum of the first 1000 primes is {sum(thousand_primes)}')

    # Use the build-ins any, all
    print(any([False, False, True]))
    print(all([False, False, True]))
    cities = ['London', 'Madrid', 'New York', 'Ogden']
    print(f'cities list is {all(city == city.title() for city in cities)} to go')


    # Use built-in zip
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 20, 21, 20, 19, 16, 14, 12]

    for sun, mon in zip(sunday, monday):
        print(f'The average = {(sun+mon)/2.}')

    for temp in zip(sunday, monday, tuesday):
        print(f'minimum = {min(temp)}, maximum = {max(temp)}, and avg = {sum(temp)/len(temp)}')
# --------------------------------------------------
if __name__ == '__main__':
    main()
