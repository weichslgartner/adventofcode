'''
Created on 02.12.2016

@author: weichslgartner



'''
import re


def calculateLengthSymbolic(line):
    if '(' not in line:
        print(line)
        return len(line)
    length = 0 
    i=0
    while i < len(line):
        numbers = [1,1]
        if line[i] == '(':
            bracket=''
            while line[i] != ')':
                bracket += line[i]
                i+=1
            i+=1
            #print(bracket)
            numbers = list(map(int,re.findall('\d+', bracket))) 
        #for n in range(numbers[1]):
        if '(' in line[i:i+numbers[0]]*numbers[1]:
            length +=calculateLengthSymbolic( line[i:i+numbers[0]]*numbers[1])
        else: 
            length +=  numbers[0] *  numbers[1]
        i+= numbers[0]
    #print(result)
    return length

def calculateLength(line):
    if '(' not in line:
        print(line)
        return len(line)
    result =''
    i=0
    while i < len(line):
        numbers = [1,1]
        if line[i] == '(':
            bracket=''
            while line[i] != ')':
                bracket += line[i]
                i+=1
            i+=1
            #print(bracket)
            numbers = list(map(int,re.findall('\d+', bracket))) 
        #for n in range(numbers[1]):
        result+=line[i:i+numbers[0]]*numbers[1]
        i+= numbers[0]
    #print(result)
    return len(result)

#print(padArray[1][1])
with open('input9.dat') as file:
    for line in file:
        line = re.sub('\n','',line)
        print(calculateLengthSymbolic(line))
        #print(calculateLength(line))