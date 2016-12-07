'''
Created on 02.12.2016

@author: weichslgartner



'''
import re

def isSSL(candidates, brackets):
    ssl = False
    for candidate in candidates:
        bab=candidate[1]+candidate[0]+candidate[1]
        for bracket in brackets:
            if bab in bracket:
                return True
    return ssl
def sslCandidates(word):
    candidates = []
    for i in range(1,len(word)-1):
        cond1= word[i] != word[i-1]
        cond2= word[i-1] == word[i+1]
        if cond1 and cond2:
            candidates.append(word[i-1]+ word[i]+word[i+1])
    return candidates
        
def isTLS(word):
    tls = False
    for i in range(1,len(word)-2):
        
        cond1= word[i] == word[i+1]
        cond2= word[i-1] == word[i+2]
        cond3= word[i] != word[i-1]
       
        if cond1 and cond2 and cond3:
            tls = True
       
        
    return tls        
         
         
countTLS =0     
countSSL =0       
with open('input7.dat') as file:
    i = 0
    for line in file:
        brackets = re.findall('\[[a-z]+\]', line)
        inBracketTLS = False
        for bracket in brackets:
            #bracket = re.sub('\[|\]','',bracket)
            inBracketTLS = isTLS(bracket)
            if inBracketTLS:
                break
            
            
        line_clean = re.sub('\[[a-z]+\]',' ',line)
        tls  = isTLS(line_clean)
        if tls and not inBracketTLS:
            countTLS+=1
        if isSSL(sslCandidates(line_clean),brackets):
            countSSL+=1
print("# TLS: {0}".format(countTLS))
print("# SSL: {0}".format(countSSL))