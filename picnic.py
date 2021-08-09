#!/usr/bin/env python3
"""
Author : t26 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',  # one or more arguments
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    print(args.item)
    items = args.item

    # Check if the list needs to be sorted
    if args.sorted:
        items.sort()

    # Prepare list to print
    #1 Item, just print item
    #2 Items: item 1 and item 2
    #3 or more items: item1, item2, itemx, and itemLast
    bringing = ', '.join(items[0:-1])
    bringing += " and " if len(items) > 1 else ''
    bringing += f'{items[-1]}'

    # Print info
    print(f'You are bringing {bringing}.')



# --------------------------------------------------
if __name__ == '__main__':
    main()
