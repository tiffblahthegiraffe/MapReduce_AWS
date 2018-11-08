#!/usr/bin/env python
import sys
import re
from email.utils import parseaddr

groupby = {} #This is use to store the output key,value pairs

for line in sys.stdin:
    line = line.strip()
    headers, ID= line.split('\t',1) #split the input format by tab
    
    #Let the email be the key and the Message ID associate with it as value
    groupby[headers] = ID 
    if headers in groupby:
        #Attach the Message ID having the same header and email to it
        groupby[headers] += ID
        
for k,v in groupby.items():
    print '%s\t%s' %(k,v)  