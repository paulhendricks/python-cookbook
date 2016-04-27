#!/usr/bin/python3
"""Keeping the last N items
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open('somefile.txt') as f:
        for l, prevlines in search(f, 'python'):
            for pline in prevlines:
                print(pline, end='')
            print(l, end='')
            print('-' * 20)
