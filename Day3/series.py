import sys
from itertools import count, islice


def sequence():
    """
        Recaman sequence:
        a_0 = 0,
        a_n=a_(n-1) - n: if result is positive AND not already in the list
        a_n = a_(n-1) + n
    """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a-n
        if c < 0 or c in seen:
            c = a+n
        a = c

def write_sequence(filename, num):
    f = open(filename, mode='wt', encoding='utf-8')

    f.writelines([f'{i}\n' for i in islice(sequence(), num)])

    f.close()

def main():
    write_sequence("sequence.txt", 100)

if __name__ == '__main__':
    main()