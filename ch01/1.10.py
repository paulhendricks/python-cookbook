#!/usr/bin/python3
"""Removing Duplicates from a Sequence while Maintaining Order

Complete!
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


if __name__ == '__main__':
    a = [1, 5, 2, 9, 10, 1, 3, 6, 5]
    print(a)
    print(list(dedupe(a)))
