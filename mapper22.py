#!/usr/bin/env python

import sys
import re

for line in sys.stdin:

    line = line.strip()

    store = line.split()

    p = re.compile(r'.[a-z]$')
    match = re.search(p, store[0])

    if match:
        print(store[0])    

