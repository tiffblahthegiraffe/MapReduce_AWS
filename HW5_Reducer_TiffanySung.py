#!/usr/bin/python
import sys
import numpy as np


raw_counts = {} # store the counts from mapper
message = {} # store the message count for each word
Maximum = {} # store max occurence for each word
minimum = {} # store min occurence for each word
totalcount = {} # store total count of words across document
mean = {} # store average occrence for each word
variance = {} # store variance of occurence for each word
SS = {} # store sum of square of occurence for each word
reducer = []

files = open("dataSet2Small.txt",'r')

#for line in sys.stdin:
for line in files:

    line = line.strip().lower()#---convert to lower case, strip newline characters---

    words = line.split()#---split into individual words---


    for word in set(words): #---for each word we print word and their counts---
        output =  '%s\t%s'% (word, words.count(word))
        reducer.append(output)
#print reducer

#for line in sys.stdin:
for line in reducer:
    line = line.strip()# remove spaces

    word, count = line.split('\t', 1)# split on tabs

    # convert raw_count to integer
    try:
        count = int(count)
    except ValueError:
        continue

    # put count of words in each message into dictionary
    if word in raw_counts:
        raw_counts[word].append(count)
    else:
        raw_counts[word] = [count]

    # get message counts
    try:
        message[word] = message[word] + 1
    except:
        message[word] = 1


    # Find maximum occurences of each word
    if word in Maximum:
        if Maximum[word] < count:
            Maximum[word] = count
    else:
        Maximum[word] = count


    # Find minimum occurences of each word
    if word in minimum:
        if minimum[word] > count:
            minimum[word] = count
    else:
        minimum[word] = count

    # get total counts
    if word in totalcount:
        totalcount[word] += count
    else:
        totalcount[word] = count

# get mean
for word in message:
    mean[word] = round(1.0*totalcount[word]/message[word],2)

# adjust the minimum so that the min of words that does not appear in a message is 0
for word in message:
    if message[word] < max(message.values()):
        minimum[word] = 0

# get variance
for word in raw_counts:
    SS[word] = round(((np.array(raw_counts[word]) - mean[word])**2).sum(),2)
    variance[word] = round(float(SS[word])*1.0/message[word],2)

# statistics of words
for word in message.keys():
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'% (word, message[word], totalcount[word], SS[word], minimum[word], Maximum[word], mean[word], variance[word])

