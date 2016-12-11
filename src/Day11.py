'''
Created on 11.12.2016

@author: andreas
'''
import copy
simulatorArray = [['.',  '.' ,  '.',  '.',   '.'],
                  ['.',   '.' ,  '.',  'LG' ,  '.'],
                  ['.' ,  'HG' ,  '.' , '.' ,  '.'],
                  ['E' ,  '.'  , 'HM',  '.',   'LM']
                  ]

def isValid(line):
    valid = True
    if 'HM' in line and 'LG' in line and not 'HG' in line:
        valid = False
    elif 'LM' in line and 'HG' in line and not 'LG' in line:
        valid = False
    return valid

def indexElevator(simulatorArray):
    for i in range(len(simulatorArray)):
        print(simulatorArray[i][0])
        if simulatorArray[i][0]== 'E':
            return i
    return 0


def possibleMoves(simulatorArray):
    elevatorindex = indexElevator(simulatorArray)
    nextIndex =[]
    if elevatorindex -1 > 0:
        nextIndex.append(elevatorindex -1)
    if elevatorindex+1 < len(simulatorArray):
        nextIndex.append(elevatorindex +1)    
        
    
    for i in range(1,len(simulatorArray[0])):
        for index in nextIndex:
            if 'HG' in simulatorArray[elevatorindex] and 'HM' in simulatorArray[elevatorindex]:
                newline = copy.deepcopy(simulatorArray[index])
                newline[1]= 'HG'
                newline[2]= 'HM'
                print (newline)
                print(isValid(newline))
            if 'LG' in simulatorArray[elevatorindex] and 'LM' in simulatorArray[elevatorindex]:
                newline[3]= 'LG'
                newline[4]= 'LM'
                print (newline)
                print(isValid(newline))
            if simulatorArray[elevatorindex][i] != '.':
                newline = copy.deepcopy(simulatorArray[index])
                newline[i] = simulatorArray[elevatorindex][i]
                print (newline)
                print(isValid(newline))
                
possibleMoves(simulatorArray)