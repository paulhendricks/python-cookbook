#!/usr/bin/python3
"""Combining Multiple Mappings into a Single Mapping

Complete!
"""
from collections import ChainMap


if __name__ == '__main__':
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    # (a) Simple example of combining
    c = ChainMap(a, b)
    print(c['x'])  # Outputs 1  (from a)
    print(c['y'])  # Outputs 2  (from b)
    print(c['z'])  # Outputs 3  (from a)
