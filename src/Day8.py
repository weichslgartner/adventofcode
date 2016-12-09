'''
Created on 02.12.2016

@author: weichslgartner



'''
import re
import copy



def printPadLetters(array):
    for y in range(len(array)):
        for x in range(len(array[0])):
            if x% 5 ==0:
                print(" ",end="")
            if    array[y][x] == 1:
                print("x",end="")
            else:   
                print(" ",end="") 
        print("")   

def printPad(array):
    for y in range(len(array)):
        for x in range(len(array[0])):
            print(array[y][x],end="")
        print("")   
        
        
def doRect(array,width,height): 
    for y in range (min(height,len(array))):
        for x in range (min(width,len(array[0]))):
            array[y][x] = 1
            #print ("y:{0} x:{1}".format(y,x))
 
def rotateColumn(array,column,value): 
    oldarray = copy.deepcopy(array)
    for y in range(len(array)):
        array[y][column] = oldarray[(y-value) % (len(array))][column]

def rotateRow(array,row,value): 
    oldrow = copy.deepcopy(array[row])
    for x in range(len(array[row])):
        array[row][x] = oldrow[(x-value) % (len(array[0]))]    
        
def countOnes(array):     
    sum=0
    for y in range(len(array)):
        for x in range(len(array[0])):
            sum += array[y][x]
    return sum       
        
WDITH = 50
HEIGTH =6              
padArray = [[0 for x in range(WDITH)] for y in range(HEIGTH)]

 


#printPad(padArray)

#print(padArray[1][1])
with open('input8.dat') as file:
    for line in file:

        numbers = list(map(int,re.findall('\d+', line)))       
        if line.startswith("rect") :
            doRect(padArray,numbers[0],numbers[1])

        elif line.startswith("rotate column") :
            rotateColumn(padArray,numbers[0],numbers[1])

        elif line.startswith("rotate row") :
            rotateRow(padArray,numbers[0],numbers[1])
print("Number Pixels: " +str(countOnes(padArray)))       
printPadLetters(padArray)