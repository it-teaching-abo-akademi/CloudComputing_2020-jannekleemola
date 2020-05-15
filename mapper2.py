#!/usr/bin/env python

import sys
store = {}
for line in sys.stdin:

    line = line.strip()

    words = line.split()

   

    for word in words:
        if word not in store:
            store[word] = 1
        else:
            store[word] += 1

    for word in store:
    
        print("%s\t%s" % (word, store[word]))
