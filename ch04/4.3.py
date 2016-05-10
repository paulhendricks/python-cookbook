#!/usr/bin/python3
"""Creating New Iteration Patterns with Generators

Complete!
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == '__main__':
    for i in frange(0, 10, 3):
        print(i)
