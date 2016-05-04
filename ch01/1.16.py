#!/usr/bin/python3
"""Filtering Sequence Elements

Complete!
"""


if __name__ == '__main__':
    items = [1, 2, 3, 4, 5, 6]
    filtered = [i for i in items if i < 3]
    print(filtered)
    filtered = [i if i < 3 else None for i in items]
    print(filtered)
