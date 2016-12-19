'''
Created on 19.12.2016

@author: weichslgartner
'''


import copy 

class Elf:
    def __init__(self,id,gifts):
        self.id = id
        self.gifts=gifts
    def __del__(self):
        pass
NUMBERELVES=3018458

elves = []
if NUMBERELVES % 2 == 0:
    for i in range(1,NUMBERELVES+1,2):
        elves.append(Elf(i,2))
else:
    for i in range(1,NUMBERELVES+1,1):
        elves.append(Elf(i,1))
# for i in range(1,int(NUMBERELVES)+1):
#     elves.append(Elf(i,2))


found = False
while not found:
    #deletelist = []
    newList = []
    print(len(elves))
    for i,elf in enumerate(elves):
        #if (i%100 ==0):
        #    print("\r {0}/{1}"  .format(i, len(elves)))
        next = (i+1) % len(elves)
        if elf.gifts > 0 and elves[next].gifts >0:
            elves[i].gifts +=elves[next].gifts
            elves[next].gifts =0
            #deletelist.append(elves[next])
            newList.append(elf)
            
            if next ==0:
                del newList[0]
            
        if elves[i].gifts == NUMBERELVES:
            print("FOUND:" +str(elves[i].id)+ " "+str(elves[i].gifts))
            found = True
            break
    elves = newList
    if (len(elves)==1):
        print(elves[0].gifts)
    if (len(elves)==0):
        break
    #for element in deletelist:
     #   elves.remove(element)