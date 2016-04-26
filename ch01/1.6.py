#!/usr/bin/python3
"""Mapping keys to multiple values in a dictionary
"""
from collections import defaultdict


d = defaultdict(list)
d['a'].append(2)
d['a'].append(2)
d['a'].append(1)
d['b'].append(4)
d


d = defaultdict(set)
d['a'].add(2)
d['a'].add(2)
d['a'].add(1)
d['b'].add(4)
d
