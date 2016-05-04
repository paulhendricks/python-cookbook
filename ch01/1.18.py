#!/usr/bin/python3
"""Mapping Names to Sequence Elements

Complete!
"""
from collections import namedtuple


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(recs):
    total = 0.0
    for rec in recs:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


if __name__ == '__main__':
    # Some Data
    records = [('GOOG', 100, 490.1),
               ('ACME', 100, 123.45),
               ('IBM', 50, 91.15)]
    print(compute_cost(records))
