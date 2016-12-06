'''
Created on 02.12.2016

@author: weichslgartner



'''
import re

listofdics =[]


def sortDicsAndPrintFrequent(listofdics):
    mostFrequent = ''
    leastFrequent = ''
    for dic in listofdics:
        sortedDics = sorted(dic.items(),key = lambda x: x[1],reverse=True)
        mostFrequent +=sortedDics[0][0]
        leastFrequent  +=sortedDics[len(dic)-1][0]
    print("Part 1: "+mostFrequent)    
    print("Part 2: "+leastFrequent)
    
def addToDict(dic, char):
    if char in dic:
        dic[char] = dic[char]+1
    else:    
        dic[char] =1

with open('input6.dat') as file:
    i = 0
    for line in file:
        line = re.sub('\n','',line)
        for j in range(0, len(line)):
            if i==0:
                listofdics.append({})  
            addToDict(listofdics[j],line[j])
                #print(line[j])
        i+=1        
    #print(listofdics)
    sortDicsAndPrintFrequent(listofdics)