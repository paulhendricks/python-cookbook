#!/usr/bin/python3
"""Determining the Most Frequently Occurring Items

Complete!
"""
from collections import Counter


if __name__ == '__main__':
    items = [1, 5, 2, 9, 10, 1, 3, 6, 5, 1, 1, 1, 1, 4, 5, 5, 5]
    c = Counter(items)
    print(c.most_common(3))
