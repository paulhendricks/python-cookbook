#!/usr/bin/python3
"""Writing Functions That Accept Any Number of Arguments

Complete!
"""

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


if __name__ == '__main__':
    print(avg(1, 2, 3, 4))
