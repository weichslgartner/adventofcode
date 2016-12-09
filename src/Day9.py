'''
Created on 02.12.2016

@author: weichslgartner



'''
import re
import copy

def calculateLength(line):
    if '(' not in line:
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
            print(bracket)
            numbers = list(map(int,re.findall('\d+', bracket))) 
        for n in range(numbers[1]):
            for m in range(numbers[0]):
                i+=m
                result+=line[i]
    print(result)
    return calculateLength(result)

#print(padArray[1][1])
with open('input9.dat') as file:
    for line in file:
        print(calculateLength(line))