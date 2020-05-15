#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
import operator

current_word = None
current_count = 0
word = None
total = 0
d = {}
for line in sys.stdin:

    line = line.strip()
    word, count = line.split('\t', 1)

    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_word == word:
        current_count += count
        total = total + count
        d[word] += count
    else:
        total = total + count
        current_count = count
        d[word] = count
        current_word = word
        
print("Total %d" % (total))
top_list = sorted(d.items(), key=operator.itemgetter(1))[len(d)-100:len(d)]
print(top_list)
