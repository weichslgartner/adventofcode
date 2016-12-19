'''
Created on 19.12.2016

@author: weichslgartner
'''


import copy, sys

class Elf:
    def __init__(self,id,gifts):
        self.id = id
        self.gifts=gifts
    def __del__(self):
        pass
NUMBERELVES=3018458

elves = []
for i in range(1,NUMBERELVES+1,1):
    elves.append(Elf(i,1))
# for i in range(1,int(NUMBERELVES)+1):
#     elves.append(Elf(i,2))


found = False
i=0
while len(elves)>1:

#     if len(elves) %2 ==0:
#         length = int(len(elves)/2)
#     else:
#         length =int(len(elves)/2)+1
    length = len(elves)
    if (length%10000 ==0):
        sys.stdout.write("%d  %d \r" % (i,length) )
        sys.stdout.flush()

    nextElf = (int(len(elves)/2) + i) % length
    elves[i].gifts +=elves[nextElf].gifts
    elves[nextElf].gifts =0
        #deletelist.append(elves[next])
    #print (str(elves[i].id) + " steals from " + str(elves[nextElf].id))
    del elves[nextElf]
    if nextElf > i:
        i= (i+1)
    i= i % len(elves)
        
    
if len(elves) == 1:
    print("FOUND:" +str(elves[i].id)+ " "+str(elves[i].gifts))
    
    
    #for element in deletelist:
     #   elves.remove(element)