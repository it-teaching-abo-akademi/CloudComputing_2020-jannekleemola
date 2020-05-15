#!/usr/bin/env python

import sys
import operator

current_word = None
word = None
five = 0
three = 0

for line in sys.stdin:

    line = line.strip()
    word, count = line.split('\t', 1)

    
    try:
        count = int(count)
    except ValueError:
        continue
    
    
    if len(word) == 3:
        three += 1
    if len(word) == 5:
        five += 1
    
        
print("Words with three letters %d" % (three))
print("Words with five letters %d" % (five))

