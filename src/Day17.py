import hashlib, sys
from collections import namedtuple

sys.setrecursionlimit(10000) 
Pos = namedtuple('Point', ['x', 'y'])
DIMY = 3
DIMX = 3
solutions = []
posToDir = {(-1,0):'L',(1,0):'R',(0,1):'D',(0,-1):'U' }
globalDir = {}
minSolutionLength = sys.maxsize
maxSolutionLength = 0
posStepDict = {}

def sequenceToPos(sequence):
    x =0
    y =0
    if sequence == '0':
        return Pos(0,0)
    for s in sequence:
        if s == 'L':
            x-=1
        elif s == 'R':
            x+=1
        elif s == 'U':
            y-=1
        elif s == 'D':
            y+=1
    return Pos(x,y)

def getValidMoves(word, currentPos):
    validMovesPos = []
    for i, charI in enumerate(word[0:4]):
        #open
        if ord(charI) > ord('a'):
            if i == 0 and currentPos.y > 0:
                validMovesPos.append(Pos(0,-1))
            elif i == 1 and currentPos.y < DIMY:
                validMovesPos.append(Pos(0,1))
            elif i == 2 and currentPos.x > 0:
                validMovesPos.append(Pos(-1,0))    
            elif i == 3 and currentPos.x < DIMX:
                validMovesPos.append(Pos(1,0))    
    return validMovesPos


def searchLongestPath(word):
    queue  = []
    queue.append('')
    while len(queue) > 0:
        sequence =  queue[0]
        del  queue[0]
        
        
        if sequence in globalDir:
            continue
        globalDir[sequence] = len(sequence)
        global maxSolutionLength
        currentPos = sequenceToPos(sequence)
        if currentPos.x==3 and currentPos.y == 3:
        #print ('reached')
            if len(sequence) >  maxSolutionLength:    
                solutions.append(sequence)
                maxSolutionLength = len(sequence)
                #print(maxSolutionLength) 
            continue
        if currentPos in posStepDict:
            if posStepDict[currentPos] >  len(sequence):
                continue
            else:
                posStepDict[currentPos] = len(sequence)
        else:
            posStepDict[currentPos] = len(sequence)
        
        
        
        tmpword = word + sequence
        m = hashlib.md5(tmpword.encode('ascii'))
        #print(word)
        hashWord = m.hexdigest()
        moves =  getValidMoves(hashWord, currentPos)
        for move in moves:
            queue.append(sequence + posToDir[move])

def searchShortestPath(word,sequence,currentPos):
    global minSolutionLength
    if currentPos.x==3 and currentPos.y == 3:
        #print ('reached')
        if len(sequence)<  minSolutionLength:    
            solutions.append(sequence)
            minSolutionLength = len(sequence)
        return 
    if len(sequence) > minSolutionLength:
        return
    if word+sequence in globalDir:
        return
    globalDir[word+sequence] = len(sequence)
    tmpword = word + sequence
    m = hashlib.md5(tmpword.encode('ascii'))
    #print(word)
    hashWord = m.hexdigest()
    moves =  getValidMoves(hashWord, currentPos)
    if len(moves) == 0:
        return
    for move in moves:
        tmpSequence = sequence + posToDir[move]
        searchShortestPath(word,tmpSequence,Pos(currentPos.x+move.x,currentPos.y+move.y))
    
word ='qtetzkpl'
sequence = ''
currentPos = Pos(x=0,y=0)
searchShortestPath(word,sequence,currentPos)
print("Part1: "+solutions[-1])
searchLongestPath(word)
print("Part1: "+str(maxSolutionLength))
#print(solutions[-1])