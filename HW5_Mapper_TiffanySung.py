#!/usr/bin/python
import sys
import numpy as np


for line in sys.stdin:

    line = line.strip().lower()
    words = line.split()

    for word in set(words): #---for each word we print word and their counts---
        print '%s\t%s'% (word, words.count(word))