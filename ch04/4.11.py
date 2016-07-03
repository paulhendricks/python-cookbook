#!/usr/bin/python3
"""Iterating Over Multiple Sequences Simultaneously

Complete!
"""


if __name__ == '__main__':
    foo = ['a', 'b', 'c']
    bar = [1, 2, 3]
    for x, y in zip(foo, bar):
        print(x, y)
