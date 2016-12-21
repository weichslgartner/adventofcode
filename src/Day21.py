import re

def swapLetter(stringList,letterA,letterB):
    for i,element in enumerate(stringList):
        if element == letterA:
            stringList[i]=letterB
        if element == letterB:
            stringList[i]=letterA
    return stringList
    
            
def swapPos(stringList,source,dest):
    stringList[source],stringList[dest]=stringList[dest],stringList[source]
    return stringList

def rotateLeft(stringList,steps):
    
    return   stringList[steps:] +stringList[:steps] 

def rotateRight(stringList,steps):
    return  stringList[-steps:] +stringList[:-steps]

def reverse(stringList,start, end):
    tmplist = list(reversed(stringList[start:end+1]))
    #print(stringList[5::-1])
    return  stringList[:start] + tmplist + stringList[end+1:]

def move(stringList,src, dst):
    stringList.insert(dst,stringList.pop(src))
    return stringList

start = 'abcdefgh'
stringList = list(start)
with open('input21.dat') as file:
    for line in file:
        line = line.rstrip()
        numbers = list(map(int,re.findall('\d+', line))) 
        tonkens = line.split(' ')
        if line.startswith('swap position'):
            stringList =swapPos(stringList,numbers[0],numbers[1])
        if line.startswith('swap letter'):  
            stringList =swapLetter(stringList,tonkens[2],tonkens[-1])
        if line.startswith('reverse'):     
            stringList = reverse(stringList,numbers[0],numbers[1])
        if line.startswith('rotate left'):  
            stringList = rotateLeft(stringList,numbers[0])
        if line.startswith('rotate right'):  
            stringList = rotateRight(stringList,numbers[0])   
        if line.startswith('move position'):  
            stringList = move(stringList,numbers[0],numbers[1])       
        if line.startswith('rotate based '):  
            steps = stringList.index(tonkens[-1])
            steps+=1
            if steps > 4:
                steps+=1
            steps = steps % len(stringList)
            stringList = rotateRight(stringList,steps)       
               
            
            
        #print(stringList)
print(''.join(stringList))