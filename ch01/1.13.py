#!/usr/bin/python3
"""Sorting a List of Dictionaries by a Common Key

Complete!
"""
from operator import itemgetter


if __name__ == '__main__':
    items = [{'fname': 'a', 'lname': 'z'},
             {'fname': 'b', 'lname': 'y'},
             {'fname': 'c', 'lname': 'x'},
             {'fname': 'd', 'lname': 'w'}]
    print(sorted(items, key=itemgetter('fname')))
    print(sorted(items, key=itemgetter('lname')))
