'''
Created on 02.12.2016

@author: weichslgartner
'''

keypad = [['0','0','1','0','0'],
          ['0','2','3','4','0'],
          ['5','6','7','8','9'],
          ['0','A','B','C','0'],
          ['0','0','D','0','0']]


    

with open('input2.dat') as file:
    x=0
    y=2
    for line in file:
       
        for char in line:
            if char == 'U':
                if y > 0 and keypad[y-1][x] != '0' :
                    y-=1
            elif char == 'L':
                if x > 0 and keypad[y][x-1] != '0':
                    x-=1
            elif char == 'R':
                if x < 4 and keypad[y][x+1] != '0':
                    x+=1
            elif char == 'D':          
                if y < 4 and keypad[y+1][x] != '0':
                    y+=1  
      
        print ("{2}".format(x,y,keypad[y][x]), end ="")