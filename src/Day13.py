'''
Created on 13.12.2016

@author: weichslgartner
'''

import queue
from collections import namedtuple
import copy

class Node:
    def __init__(self,pred,cost):
        self.pred = pred
        self.cost = cost
        
    
designerNumber = 10
WALL = '#'
NOWALL = '.'
Point = namedtuple('Point', ['x', 'y'])
initPoint = Point(-1,-1)

def isWall(x,y,designerNumber):
    sumW = x*x+3*x+2*x*y+y+y*y
    sumW+=designerNumber
    ones = bin(sumW).count('1')
    if ones % 2 == 0:
        return NOWALL
    else:
        return WALL


def createMaze(height, width,dNumber):
    array = [[0]*width for i in range(height)]
    for y in range(height):
        for x in range (width):
            array[y][x] = isWall(x,y,dNumber)
            
    return array

def createDistantMatrix(height, width,defaultNode):
    array = [[copy.deepcopy(defaultNode) for x in range(width)] for i in range(height)]            
    return array            

def printDistanceMatrix(array):
    for line in array:
        for element in line:
            print(element.cost, end = "\t")
        print()

def printMaze(array):
    for line in array:
        for char in line:
            print(char, end = "")
        print()

def shortestPath(start,destination,maze,distanceMatrix):
    visited = []
    openSet = queue.PriorityQueue()
    openSet.put((0,start))
    distanceMatrix[start.y][start.x].cost = 0
    while not openSet.empty():
        #printDistanceMatrix(distanceMatrix)
        prio, current = openSet.get(0) 
        if current == destination:
            return distanceMatrix[destination.y][destination.x].cost
        visited.append(current)
        expandNode(current,openSet,destination,visited,maze,distanceMatrix)
    #printDistanceMatrix(distanceMatrix)

def expandNode(current,openSet,destination,visited,maze,distanceMatrix):
    for succ in getFreeSuccessors(current,maze):
        if succ in visited:
            continue
        costN = distanceMatrix[current.y][current.x].cost + 1
        if succ in openSet.queue and costN >= distanceMatrix[succ.y][succ.x].cost:
            continue
        distanceMatrix[succ.y][succ.x].pred = current
        distanceMatrix[succ.y][succ.x].cost = costN
        estimate = costN + manhattanDistance(succ,destination)
        openSet.put((estimate,succ))
        
        
def manhattanDistance(current,dest):
    return abs(dest.x - current.x) + abs(dest.y - current.y)


def getFreeSuccessors(current,maze):
    freeSucc = []
    for succ in getSuccessors(current,maze):
        if maze[succ.y][succ.x] == '.':
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
    width = 100
    height = 100
    maze = createMaze(height, width, 1362)
    printMaze(maze)
   
    defaultNode = Node((-1,-1),100000)
    start = Point(1,1)
    dest = Point(31,39)
    #node = Node(start,3)
    distanceMatrix = createDistantMatrix(height,width,defaultNode) 
    sp = shortestPath(start, dest, maze, distanceMatrix)
    print("Part 1: " +str(sp))
    dest = Point(50,50)
    distanceMatrix = createDistantMatrix(height,width,defaultNode) 
    shortestPath(start, dest, maze, distanceMatrix)
    distinctPlaces = pointsWithinRange(distanceMatrix,50)
    print("Part 1: " +str(distinctPlaces))
    