#!/usr/bin/python3
"""Sorting Objects Without Native Comparison Support

Complete!
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)



if __name__ == '__main__':
    users = [User(23), User(3), User(99)]
    print(sorted(users, key=attrgetter('user_id')))
    print(min(users, key=attrgetter('user_id')))
    print(max(users, key=attrgetter('user_id')))
