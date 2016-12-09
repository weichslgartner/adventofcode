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
    for i,char in enumerate(line):
        numbers = [1,1]
        if line[i] == '(':
            bracket=''
            while line[i] != '(':
                bracket += line[i]
                i+=1
            print(bracket)
            numbers = list(map(int,re.findall('\d+', bracket))) 
        for n in range(numbers[1]):
            for m in range(numbers[0]):
                result+=line[i+m]
    print(result)
    return calculateLength(result)

#print(padArray[1][1])
with open('input9.dat') as file:
    for line in file:
        calculateLength(line)