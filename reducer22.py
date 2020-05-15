#!/usr/bin/env python

import sys
import operator

current_word = None
current_count = 0
word = None
d = {}

for line in sys.stdin:

    data = line

    if data not in d:
        d[data] = 1
    else:
        d[data] += 1


top_list = sorted(d.items(), key=operator.itemgetter(1))[len(d)-5:len(d)]
print(top_list)

