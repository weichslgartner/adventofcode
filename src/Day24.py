'''
Created on 24.12.2016

'''

from collections import namedtuple
import copy
import sys


from itertools import permutations
import itertools
from heapq import heappush, heappop

WALL = '#'
NOWALL = '.'
Point = namedtuple('Point', ['x', 'y'])
initPoint = Point(-1,-1)

class PrioQu:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count
    
    def add_task(self,task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)
    
    def contains_task(self,task):
        if task in self.entry_finder:
            return True
        return False
    
    def empty(self):
        return len(self.entry_finder) == 0
    
    def remove_task(self,task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED
    
    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

class Node:
    def __init__(self,pred,cost):
        self.pred = pred
        self.cost = cost
        
    


def findShortestRouteAndRoundTrip(destDict, adjacencyMatrix):
    destList = list(destDict.keys())
    destList.remove(0)
    shortestRoute = sys.maxsize
    shortestRoundTrip = sys.maxsize
    for permutation in permutations(destList):
        permutedList = list(permutation)
        permutedList.insert(0, 0) #print(permutedList)
        currShortestRoute = 0
        currShortestRoundTrip = 0
    #permutedList =[0,4,1,2,3]
        for cur, next in zip(permutedList[:-1], permutedList[1:]):
            currShortestRoute += adjacencyMatrix[cur][next]
        
        currShortestRoundTrip = currShortestRoute + adjacencyMatrix[permutedList[-1]][0]
        shortestRoundTrip = min(currShortestRoundTrip, shortestRoundTrip)
        shortestRoute = min(currShortestRoute, shortestRoute)
    
    print('Part1:', end=" ")
    print(shortestRoute)
    print('Part2:', end=" ")
    print(shortestRoundTrip)


def fillAdjacencyMatrix(maze, destDict, width, height, adjacencyMatrix, defaultNode, distanceMatrix):
    for outerKey, outerValue in destDict.items():
        start = outerValue
        distanceMatrix = createDistantMatrix(height, width, defaultNode)
        for innerKey, innerValue in destDict.items(): 
            if innerKey < outerKey:
                continue
            print("from {0} to {1}".format(outerKey, innerKey)) #printDistanceMatrix(distanceMatrix)
            print(destDict)
            dest = innerValue
            sp = shortestPath(start, dest, maze, distanceMatrix)
            adjacencyMatrix[outerKey][innerKey] = sp
            adjacencyMatrix[innerKey][outerKey] = sp#
            
            
def readMaze(filepath):
    array =[]
    y=0
    destDict = {}
    with open(filepath) as file:
        for line in file:
            currentLineList = list(line.rstrip())
            for x,char in enumerate(currentLineList):
                if char.isdigit():
                    destDict[int(char)]= Point(x,y)
            array.append(currentLineList)
            y+=1
    return array, destDict




def createDistantMatrix(height, width,defaultNode):
    array = [[copy.deepcopy(defaultNode) for x in range(width)] for i in range(height)]            
    return array            

def printDistanceMatrix(array):
    for line in array:
        for element in line:
            print(element.cost, end = "\t")
        print()

def printAdjacencyMatrix(array):
    for line in array:
        for char in line:
            print(char, end = "\t")
        print()  

def printMaze(array):
    for line in array:
        for char in line:
            print(char, end = "")
        print()

def shortestPath(start,destination,maze,distanceMatrix):
    visited = []
    
    openSetPrio = PrioQu()
    
    
    openSetPrio.add_task(start, 0)
    distanceMatrix[start.y][start.x].cost = 0
    while not openSetPrio.empty():
        #printDistanceMatrix(distanceMatrix)
        current = openSetPrio.pop_task() 
        if current == destination:
            return distanceMatrix[destination.y][destination.x].cost
        visited.append(current)
        expandNode(current,openSetPrio,destination,visited,maze,distanceMatrix)
    #printDistanceMatrix(distanceMatrix)

def expandNode(current,openSet,destination,visited,maze,distanceMatrix):
    for succ in getFreeSuccessors(current,maze):
        if succ in visited:
            continue
        costN = distanceMatrix[current.y][current.x].cost + 1
        if openSet.contains_task(succ) and costN >= distanceMatrix[succ.y][succ.x].cost:
            continue
        distanceMatrix[succ.y][succ.x].pred = current
        distanceMatrix[succ.y][succ.x].cost = costN
        estimate = costN + manhattanDistance(succ,destination)
        
        openSet.add_task(succ,estimate)
        
        
def manhattanDistance(current,dest):
    return abs(dest.x - current.x) + abs(dest.y - current.y)


def getFreeSuccessors(current,maze):
    freeSucc = []
    for succ in getSuccessors(current,maze):
        if maze[succ.y][succ.x] != WALL:
            freeSucc.append(succ)
    return freeSucc

def pointsWithinRange(distanceMatrix,maxSteps):
    numbPoints = 0
    for line in distanceMatrix:
        for element in line:
            if element.cost <= maxSteps:
                numbPoints +=1
    return numbPoints


def getSuccessors(current,maze):
    succs=[]
    if current.x > 0:
        succs.append(Point(current.x-1,current.y))
    if current.x < len(maze[0])-1:
        succs.append(Point(current.x+1,current.y))
    if current.y > 0:
        succs.append(Point(current.x,current.y-1))
    if current.y < len(maze)-1:
        succs.append(Point(current.x,current.y+1))
    return succs




if __name__ == '__main__':
   
    maze, destDict = readMaze('input24.dat')
    printMaze(maze)
    width = len(maze[0])
    height = len(maze)
    adjacencyMatrix = [[-1]*len(destDict) for i in range (len(destDict))]
    defaultNode = Node((-1,-1),100000)
    distanceMatrix = createDistantMatrix(height,width,defaultNode)

    fillAdjacencyMatrix(maze, destDict, width, height, adjacencyMatrix, defaultNode, distanceMatrix)
    
    printAdjacencyMatrix(adjacencyMatrix)
    findShortestRouteAndRoundTrip(destDict, adjacencyMatrix)
    