#!/usr/bin/env python

import sys
import operator

current_word = None
current_count = 0
word = None
total = 0
count = 0

for line in sys.stdin:

    line = line.strip()
    data = line

    try:
        data = int(data)
    except ValueError:
        continue

    total += data
    count += 1

print("Total data in bytes %d" % (total))
print("Number of requests %d" % (count))
