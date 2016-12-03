'''
Created on 02.12.2016

@author: weichslgartner



'''


import re

def isTriangle(x, y, z,count):
    if x + y > z and x + z > y and y + z > x:
        count += 1
    return count    

with open('input3.dat') as file:
    count =0
    i = 0
    x=[0]*3
    y=[0]*3
    z=[0]*3
    for line in file:
        tokens = re.findall("\d+", line)
        x[i] = int(tokens[0])
        y[i] = int(tokens[1])
        z[i] = int(tokens[2])
        i+=1
        if i % 3 ==0:
            count = isTriangle(x[0], x[1], x[2],count)
            count = isTriangle(y[0], y[1], y[2],count)
            count = isTriangle(z[0], z[1], z[2],count)
            i = 0
            

    
    print(count)