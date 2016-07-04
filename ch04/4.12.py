#!/usr/bin/python3
"""Iterating on Items in Separate Containers

Complete!
"""
import itertools


if __name__ == '__main__':
    foo = ['a', 'b', 'c']
    bar = [1, 2, 3]
    for x in itertools.chain(foo, bar):
        print(x)
