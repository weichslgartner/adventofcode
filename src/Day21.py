import re
import itertools
from itertools import permutations

def scramble(stringList, lines,descramble):
    for line in lines:
        line = line.rstrip()
        numbers = list(map(int, re.findall('\d+', line)))
        tonkens = line.split(' ')
        if line.startswith('swap position'):
            if descramble:
                stringList = swapPos(stringList, numbers[1], numbers[0])
            else:
                stringList = swapPos(stringList, numbers[0], numbers[1])
        if line.startswith('swap letter'):
            if descramble:
                stringList = swapLetter(stringList, tonkens[-1], tonkens[2])
            else:
                stringList = swapLetter(stringList, tonkens[2], tonkens[-1])
        if line.startswith('reverse'):
            if descramble:
                stringList = reverse(stringList, numbers[1], numbers[0])
            else:
                stringList = reverse(stringList, numbers[0], numbers[1])
        if line.startswith('rotate left'):
            if descramble:
                stringList = rotateRight(stringList, numbers[0])
            else:
                stringList = rotateLeft(stringList, numbers[0])
        if line.startswith('rotate right'):
            if descramble:
                stringList = rotateLeft(stringList, numbers[0])

            else:
                stringList = rotateRight(stringList, numbers[0])
        if line.startswith('move position'):
            if descramble:
                stringList = move(stringList, numbers[1], numbers[0])

            else:
                stringList = move(stringList, numbers[0], numbers[1])
        if line.startswith('rotate based '):
            steps = stringList.index(tonkens[-1])
            steps += 1
            if steps > 4:
                steps += 1
            steps = steps % len(stringList)
            if descramble:
                stringList = rotateLeft(stringList, steps)
            else:
                stringList = rotateRight(stringList, steps)
        #print(stringList)
    return stringList

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
    lines = file.read().splitlines()
    
stringList = scramble(stringList, lines, False)       
print(''.join(stringList))



start = 'fbgdceah'
stringList= list(start)
for permutation in permutations(stringList):
    permuated = scramble(list(permutation), lines, False)  
    if ''.join(permuated) == start:
        print("Found:"+''.join(permutation))
         
print(''.join(stringList))