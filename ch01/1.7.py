#!/usr/bin/python3
"""Keeping Dictionaries in Order

Complete!
"""
from collections import OrderedDict


if __name__ == '__main__':
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])
