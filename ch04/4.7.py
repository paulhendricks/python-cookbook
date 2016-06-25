#!/usr/bin/python3
"""

Complete!
"""
import itertools


def count(n):
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    c = count(0)
    for x in itertools.islice(c, 10, 20):
        print(x)
