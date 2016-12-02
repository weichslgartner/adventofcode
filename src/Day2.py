Created on 02.12.2016

@author: weichslgartner
'''
import re

keypad = [[1,2,3],[4,5,6],[7,8,9]]


    

with open('input2.dat') as file:
    x=1
    y=1
    for line in file:
        print ("{0} {1}".format(x,y))
        for char in line:
            if char == 'U':
                if y > 0:
                    y-=1
            elif char == 'L':
                if x > 0:
                    x-=1
            elif char == 'R':
                if x < 2:
                    x+=1
            elif char == 'D':          
                if y < 2:
                    y+=1  
            print(keypad[x][y], end="")
        print(' ', end="")                
        print(keypad[x][y])    