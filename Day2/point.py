#!/usr/bin/env python3
"""
Author : t27 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

from math import sqrt


class Point:
    """Represents a point in a 2-D geometric coordinates"""
    def __init__(self, x=0, y=0):
        """
        Initializes that position of a new point. If they are not specified,
        the point defaults to the origin
        :param x: x-coordinate, Default = 0
        :param y: y-coordinate, Default = 0
        """
        self._x = x
        self._y = y
        pass

    def reset(self):
        """
        Resets the point to the new location in 2-D space
        :return: Nothing
        """
        self.move(0, 0)

    def move(self, x, y):
        """
        Move point to a new location in 2D space
        :param x: x-coordinate
        :param y: y-coordinate
        :return: Nothing
        """
        self._x = x
        self._y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point
        passed as a parameter.
        This function uses Pythagorean Theorem to calculate
        the distance between the two points.
        :param other_point: second object of type Point
        :return: distance between two point (float)
        """
        return sqrt((self._x - other_point._x)**2 + (self._y - other_point._x)**2)

    def calculate_dot_product(self, other_point):
        return Point(self._x * other_point._x, self._y * other_point._y)

    def calculate_magniutude(self):
        return sqrt(self.calculate_dot_product(self))


# --------------------------------------------------
def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1._x, p1._y)
    print(p2._x, p2._y)
    p2.reset()
    print(p2._x, p2._y)
    p2.move(20, 30)
    print(p2._x, p2._y)

    print(p1.caclulate_distance(p2))

# --------------------------------------------------
if __name__ == '__main__':
    main()
