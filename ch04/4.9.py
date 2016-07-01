#!/usr/bin/python3
"""Iterating Over All Possible Combinations or Permutations

Complete!
"""
import itertools


if __name__ == '__main__':
    items = ['a', 'b', 'c']
    for p in itertools.permutations(items):
        print(p)
