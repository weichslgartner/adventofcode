'''
Created on 02.12.2016

@author: weichslgartner
'''
import re

from enum import Enum
class Dir(Enum):
    no = -1
    east =0
    south = 1
    west =2
    north =3
    
def isvisited(x,y,visited):    
    if((x,y) in visited):
        print("Crossing Point x:{0} y:{1} Manhattan Distance {2}" .format(x,y,abs(x)+abs(y)))   
    else:
        visited.add((x,y))  
  #      print( visited)
    
def putToSet(x_src,y_src,x_dest,y_dest,visited):
    x_cur = x_src
    y_cur= y_src
 #   print("{0} {1} {2} {3}" .format(x_src,y_src,x_dest,y_dest))
    while x_cur != x_dest or y_cur != y_dest:
        if x_cur < x_dest:
            x_cur += 1
        elif x_cur > x_dest:
            x_cur -= 1
        elif y_cur < y_dest:
            y_cur += 1
        elif y_cur > y_dest:
            y_cur -= 1    
        isvisited(x_cur,y_cur,visited)
    
x=0
y=0
visited = {}
visited = set()
currentDir = Dir.no
with open('input1.dat') as file:
    visited.add((0,0))
    for line in file:
        tokens = line.split()
        for token in tokens:
            turn = token[0] 
            steps = re.findall(r'\d+',token)
            dist = int(steps[0])
            if currentDir == Dir.no:
                if turn == 'L':
                    putToSet(x,y,x-dist,y,visited)
                    x=x-dist
                    currentDir = Dir.west
                else:
                    putToSet(x,y,x+dist,y,visited)
                    x=x+dist
   
                    currentDir = Dir.east 
            elif currentDir == Dir.east:
                if turn == 'L':
                    putToSet(x,y,x,y+dist,visited)
                    y=y+dist
                    currentDir = Dir.north
                else:
                    putToSet(x,y,x,y-dist,visited)
                    y=y-dist   
                    currentDir = Dir.south
            elif currentDir == Dir.south:
                if turn == 'L':
                    putToSet(x,y,x+dist,y,visited)
                    x=x+dist
                    currentDir = Dir.east
                else:
                    putToSet(x,y,x-dist,y,visited)
                    x=x-dist   
                    currentDir = Dir.west   
            elif currentDir == Dir.west:
                if turn == 'L':
                    putToSet(x,y,x,y-dist,visited)
                    y=y-dist
                    currentDir = Dir.south
                else:
                    putToSet(x,y,x,y+dist,visited)
                    y=y+dist   
                    currentDir = Dir.north   
            elif currentDir == Dir.north:
                if turn == 'L':
                    putToSet(x,y,x-dist,y,visited)
                    x=x-dist
                    currentDir = Dir.west
                else:
                    putToSet(x,y,x+dist,y,visited)
                    x=x+dist   
                    currentDir = Dir.east
         #   print(visited)        
 
    print("Final destination: x:{0} y:{1} Manhattan Distance {2}" .format(x,y,abs(x)+abs(y)))   