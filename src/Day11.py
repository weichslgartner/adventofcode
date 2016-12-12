'''
Created on 11.12.2016

@author: andreas
'''
import copy, re    
import itertools as it
#                    E    PrG        PrM    CoG    CoM    CuG    CuM    RuG     RuM    PlG    PlM
simulatorArrayPart1 = [['.',  '.' ,      '.',    '.',    '.',  '.',   '.',  '.',     '.',  '.',   '.'],
                  ['.',   '.' ,     '.',    '.',   'CoM',  '.',   'CuM',  '.',     'RuM',  '.',   'PlM'],
                  ['.' ,  '.' ,     '.' ,   'CoG' , '.', 'CuG',   '.',  'RuG',      '.',  'PlG',   '.'],
                  ['E' ,  'PrG'  ,  'PrM',  '.',   '.',  '.',   '.',  '.',      '.',  '.',   '.']
                  ]



targetArrayPart1   =  [['E',  'PrG' ,  'PrM',  'CoG', 'CoM',  'CuG',   'CuM',  'RuG',     'RuM',  'PlG',   'PlM'],
                  ['.',   '.' ,     '.',    '.',   '.',  '.',   '.',  '.',     '.',  '.',   '.'],
                  ['.' ,  '.' ,     '.' ,   '.' , '.', '.',   '.',  '.',      '.',  '.',   '.'],
                  ['.' ,  '.'  ,  '.',  '.',   '.',  '.',   '.',  '.',      '.',  '.',   '.']
                  ]

#                    E    PrG        PrM    CoG    CoM        CuG    CuM    RuG     RuM    PlG    PlM        ElG    ElM    DiG        DiM
simulatorArray = [['.',  '.' ,      '.',    '.',   '.',       '.',   '.',  '.',     '.',   '.',   '.',      '.',    '.',    '.',    '.'],
                  ['.',   '.' ,     '.',    '.',   'CoM',     '.',   'CuM',  '.',   'RuM',  '.',   'PlM',   '.',    '.',    '.',    '.'],
                  ['.' ,  '.' ,     '.' ,   'CoG' , '.',     'CuG',   '.',  'RuG',   '.',  'PlG',   '.' ,   '.',    '.',    '.',    '.'],
                  ['E' ,  'PrG'  ,  'PrM',  '.',   '.',        '.',   '.',  '.',     '.',  '.',   '.',      'ElG',  'ElM',  'DiG', 'DiM']
                  ]



targetArray   =  [['E',  'PrG' ,  'PrM',  'CoG', 'CoM',  'CuG',   'CuM',  'RuG',     'RuM',  'PlG',   'PlM', 'ElG', 'ElM','DiG', 'DiM'],
                  ['.',   '.' ,     '.',    '.',   '.',  '.',   '.',  '.',     '.',  '.',   '.', '.','.','.','.'],
                  ['.' ,  '.' ,     '.' ,   '.' , '.', '.',   '.',  '.',      '.',  '.',    '.', '.','.','.','.'],
                  ['.' ,  '.'  ,  '.',  '.',   '.',  '.',   '.',  '.',      '.',  '.',   '.', '.','.','.','.']
                  ]

numberFloors = len(simulatorArray)



def hash(array):
    hash = ''
    for y in range(numberFloors):
        hash += ''.join(array[y])
    return hash    

def printArray(array):
    for y in range(numberFloors):
        for x in range(len(array[0])):
            print(array[y][x], end = "\t")
        print('')

def isValid(line):
    valid = True
    generators = []
    microchips = []
    for token in line:
        if 'M' in token:
            microchips.append(token) 
        if 'G' in token:
            generators.append(token) 
    for chip in microchips:
        #check if generator exits
        generator =  re.sub('M','G',chip) 
        if generator in generators:
            continue
        elif len(generators) > 0:
            valid = False
            break
        
#     if 'HM' in line and 'LG' in line and not 'HG' in line:
#         valid = False
#     elif 'LM' in line and 'HG' in line and not 'LG' in line:
#         valid = False
    return valid

def indexElevator(simulatorArray):
    for i in range(len(simulatorArray)):
        #print(simulatorArray[i][0])
        if simulatorArray[i][0]== 'E':
            return i
    return 0


def copyLines(simulatorArray,lines):
    #newArray = [len(simulatorArray)][len(simulatorArray[0])]
    newArray = copy.deepcopy(simulatorArray)
    for y in lines:
        newArray[y][0] = '.'
    return newArray

def getConstantLines(length,*args):
    indices = []
    for i in range(length):
        if i not in args:
            indices.append(i)
    return indices


def entryIndices(line):
    indicies = []
    for i in range(1,len(line)):
        if line[i] != '.':
            indicies.append(i)
    return indicies


def possibleMoves(array,visited):
    elevatorindex = indexElevator(array)
    nextIndex =[]
    possiblemoves = []
    if elevatorindex -1 >= 0:
        nextIndex.append(elevatorindex -1)
    if elevatorindex+1 < len(array):
        nextIndex.append(elevatorindex +1) 
    
    
    for index in nextIndex:
        combs = entryIndices(array[elevatorindex])
        for comb in it.combinations(combs,2):
            newline = copy.deepcopy(array[index])
            newline[0] = 'E'
            
            newline[comb[0]]= targetArray[0][comb[0]]
            newline[comb[1]]= targetArray[0][comb[1]]
            newArray = copyLines(array,getConstantLines(numberFloors,elevatorindex,index))
            newArray[index] = copy.deepcopy(newline)
            newArray[elevatorindex][0] = '.'
            newArray[elevatorindex][comb[0]] = '.'
            newArray[elevatorindex][comb[1]] = '.'
            
            #print (newline)
            if hash(newArray) not in visited and isValid(newline) and isValid(newArray[elevatorindex]):
                #print(isValid(newline))
                
                #printArray(newArray)
                possiblemoves.append(newArray)
        for i in range(1,len(array[0])):
#            
            if array[elevatorindex][i] != '.':
                newline = copy.deepcopy(array[index])
                newline[i] = array[elevatorindex][i]
                newline[0] = 'E'
                newArray = copyLines(array,getConstantLines(numberFloors,elevatorindex,index))
                newArray[index] = newline
                newArray[elevatorindex][0] = '.'
                newArray[elevatorindex][i] = '.'
                #print (newline)
                #print(isValid(newline))
                if hash(newArray) not in visited and isValid(newline) and isValid(newArray[elevatorindex]):
                    
                   
                    #printArray(newArray)
                    possiblemoves.append(newArray)
                    
    return possiblemoves                
                    

def solve(simulatorArray,movesdict,numberMoves):
    queue = []
    queue.append((simulatorArray,numberMoves))
    bestFoud = 10000000
    currentStep = -1
    while len(queue) >0:
        current,numberMoves = queue[0]
        del queue[0]
      
       
        if hash(current) not in movesdict:
            movesdict[hash(current)] =numberMoves
        elif movesdict[hash(current)] <= numberMoves:
            continue
        if numberMoves > currentStep:
            print("Step: {0} size: {1}" .format(numberMoves, len(queue)))
            currentStep+=1
        #printArray(current)
        if hash(targetArray) == hash(current):
            print("Finished: {0}" .format(numberMoves))
            bestFoud = min(numberMoves,bestFoud)
            return
            #continue
        nextMoves = possibleMoves(current,movesdict)
        for move in nextMoves:
            queue.append((move,numberMoves+1))
            
    
    
movesdict={}
numberMoves = 0




#solveNew(simulatorArray,movesdict,numberMoves)
solve(simulatorArray,movesdict,numberMoves)
print(movesdict[hash(targetArray)])