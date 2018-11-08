#!/usr/bin/env python
import sys
import re
from email.utils import parseaddr
                    
types = ['Cc:','From:','To:','Bcc:'] #These are the headers we concern 

for line in sys.stdin:
    line = line.strip() 
    header = line.split('\t')
    
    #---Modify the ID---
    ID = header[0]
    #Get the ID pattern we want
    ID = re.findall('\<\w+.+',ID)
    
    #---Get headers and email association with them---
    content = header[1:]
    for item in content:
        for x in types:
            
            #Find the headers that are the types we want
            if item.startswith(x): 
                
                #Strip the header
                item = item.lstrip(x) 
                
                #Split those line that contains several email
                emails = item.split(',') 
                
                for i in emails:
                    #Step1: parse  and get the email pattern
                    get_email = parseaddr(i)[1] 
                    #Step2: clean the email pattern and get rid of unnecessary numbers
                    pure_email =  re.findall(r'[a-zA-Z0-9_.]+@[^\t\s,0-9]+', get_email)
                    
                    if pure_email != []:
                        #Attach the headers back to those email
                        email = x+str(pure_email).lstrip("['").rstrip("']") 
                        
                        #Output format
                        print '%s\t%s' %(email,ID)