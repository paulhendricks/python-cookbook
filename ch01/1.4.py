#!/usr/bin/python3
"""Finding the Largest or Smallest N Items

Complete!
"""
import heapq


if __name__ == '__main__':
    nums = [3, 7, 4, 2, 1, 94, 48, 34]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
