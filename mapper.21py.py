#!/usr/bin/env python

import sys

for line in sys.stdin:

    line = line.strip()

    store = line.split()
    
    if store[len(store) - 1] != '-':
        print((int(store[len(store) - 1])))
    
    

