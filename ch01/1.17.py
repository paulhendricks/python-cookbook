#!/usr/bin/python3
"""Extracting a Subset of a Dictionary

Complete!
"""


if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)
