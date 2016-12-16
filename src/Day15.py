'''
Created on 15.12.2016

@author: weichslgartner



'''

import re



def parseFile(fileName, numberPositions, startingPosition):
    with open(fileName) as file:
        for line in file:
            numbers = re.findall('\d+', line)
            numberPositions.append(int(numbers[1]))
            startingPosition.append(int(numbers[-1]))


def allZeros(array):
    for element in array:
        if element != 0:
            return False
    return True

def discPositions(time,numberPositions,startingPosition):
    positions = [0]*len(numberPositions)
    time +=1
    for disc, number in enumerate(numberPositions):
        positions[disc]=(startingPosition[disc] + time) % number
        time +=1
    return positions


def findFirstFallThroughPosition(numberPositions,startingPosition):
    for i in range(5000000):
        positions = discPositions(i,numberPositions,startingPosition) 
        if allZeros(positions):
            print("Fall through at {0}".format(i) ) 
            break

numberPositions = []
startingPosition =[]
parseFile('input15.dat',numberPositions, startingPosition)

findFirstFallThroughPosition(numberPositions,startingPosition) 

numberPositions = []
startingPosition =[]
parseFile('input15_part2.dat',numberPositions, startingPosition)

findFirstFallThroughPosition(numberPositions,startingPosition) 