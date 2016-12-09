'''
Created on 02.12.2016

@author: weichslgartner



'''


import hashlib, sys


doorcode = "reyedfim" 
solution1 =''
solution1Count = 0
solution = ['x']*8
foundpositions = []
foundValidhashes = 0
for i in range(0,sys.maxsize):
    word = doorcode+ str(i)
    m = hashlib.md5(word.encode('ascii'))
    hashValue = m.hexdigest()
    if str(hashValue).startswith("00000"):
        print(hashValue + " " + word)
        if(solution1Count < 8):
            solution1 += hashValue[5]
            solution1Count+=1
        if(int(hashValue[5],16) <8 and int(hashValue[5]) not in foundpositions):
            solution[int(hashValue[5])] = hashValue[6]
            foundValidhashes +=1
            foundpositions.append(int(hashValue[5]))
    if(foundValidhashes >= 8):
        print("Solution1: "+solution1)
        print("Solution2: " +"".join(solution))
        break
        