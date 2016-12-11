'''
Created on 02.12.2016

@author: weichslgartner






'''
import re
value1 = "value1"
value2 = "value2"
low = "low"
high = "high"
bot = "bot"

def addValue(value1, value2, botDict, val, key):
    start =""
    entry = botDict[key]
    if value1 in entry:
        entry[value2] = val
        start = key
    else:
        entry[value1] = val
    return entry, start

def solve(botDict,key,highVal,lowVal,outputs):
    entry = botDict[key]
    if not ((value1 in entry) and (value2 in entry)):
        return
    lower = min(entry[value1],entry[value2])
    higher = max (entry[value1],entry[value2])
    if lower == lowVal and higher == highVal:
        print("FOUND!!" +key)
        #return key
    
    nextLower = entry[low];
    nextHigher = entry[high];
    if "bot" in nextLower:
        addValue(value1, value2, botDict, lower, nextLower)
        solve(botDict,nextLower,highVal,lowVal,outputs)
    else:
        outputs[nextLower]= lower
        
    if "bot" in nextHigher:    
        addValue(value1, value2, botDict, higher, nextHigher)
        solve(botDict,nextHigher,highVal,lowVal,outputs)
    else:
        outputs[nextHigher]= higher
    
    
def traverse(botDict,current,visited):
    if current in visited:
        return;
    visited.append(current)
    if "output" in current:
        return;
    traverse(botDict,botDict[current]["low"],visited)
    traverse(botDict,botDict[current]["high"],visited)
    
botDict ={}
startList = {}
start =''
#print(padArray[1][1])
with open('input10.dat') as file:
    for line in file:
        line = re.sub('\n','',line)
        if line.startswith("value"):
            numbers = list(map(int,re.findall('\d+', line))) 
            key = bot + str(numbers[1])
            if key in botDict:
                entry, start = addValue(value1, value2, botDict, numbers[0], key)
            else:
                botDict[key]={}
                botDict[key][value1]=numbers[0] 
                
            startList[numbers[0]]=key
        else:
            tokens = line.split(" ")
            key = bot + str(tokens[1])
            if key in botDict:
                entry= botDict[key]
                entry[low]= tokens[5]+tokens[6]
                entry[high]= tokens[-2]+tokens[-1]
            else:
                botDict[key]={}
                botDict[key][low]= tokens[5]+tokens[6]
                botDict[key][high]= tokens[-2]+tokens[-1]
            #print(tokens) 

outputs = {}
destBot = solve(botDict, "bot190",61,17,outputs)
print(botDict)
print(outputs)
print(outputs['output0']*outputs['output1']*outputs['output2'])
