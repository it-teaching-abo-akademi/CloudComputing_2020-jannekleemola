#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:

    line = line.strip()

    store = line.split()

    for word in store:
        
        print("%s\t%s" % (word, 1))

    

