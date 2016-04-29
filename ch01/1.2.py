#!/usr/bin/python3
"""Unpacking Elements from Iterables of Arbitrary Length

Complete!
"""


if __name__ == '__main__':
    p = range(10)
    x, y, *z = p
    print(x)
    print(y)
    print(z)
