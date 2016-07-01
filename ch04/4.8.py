#!/usr/bin/python3
"""Skipping the First Part of an Iterable

Complete!
"""
import itertools


if __name__ == '__main__':
    c = range(0, 10)
    for x in itertools.islice(c, 5, None):
        print(x)
