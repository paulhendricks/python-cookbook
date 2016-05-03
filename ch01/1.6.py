#!/usr/bin/python3
"""Mapping Keys to Multiple Values in a Dictionary

Complete!
"""
from collections import defaultdict


if __name__ == '__main__':
    d = defaultdict(list)
    d['a'].append(2)
    d['a'].append(2)
    d['a'].append(1)
    d['b'].append(4)
    print(d)

    d = defaultdict(set)
    d['a'].add(2)
    d['a'].add(2)
    d['a'].add(1)
    d['b'].add(4)
    print(d)
