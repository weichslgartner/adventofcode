import hashlib, sys, re

input ="ngcjuoqr"
#input ="abc"

def checkFiveTimesNextThousands(hash,currettriplet, i,fivelet,onetimepads):
    letter5 = fivelet[0]
    valid = False
    key_list = [k for k, v in currettriplet.items() if v ==letter5 ]
    for key  in  key_list:
        value = letter5
        if key >= i-1000 and key != i:
            onetimepads.append(key)
            globaldict[key] = (hashes[key],i,hash)
            valid = True
           
    
    
    
    return valid

def printglobalDict(globaldict):
    list = sorted(globaldict)
    i=1
    for element in list:
        print(str(i)+ ": " +str(element) + " "+globaldict[element][0]+ " "+str(globaldict[element][1])+ " "+globaldict[element][2])
        i+=1

def stretchHash(word,times):
    for i in range(times+1):
        m = hashlib.md5(word.encode('ascii'))
        word = m.hexdigest()
        #print(word)
    return word


def findValidOneTimePads(part2,onetimepads, currettriplet ):
    for i in range(0,24000):
        word = input + str(i)
        m = hashlib.md5(word.encode('ascii'))
        #print(word)
        hashValue = m.hexdigest()
        if part2:
            hashValue = stretchHash(word,2016)
        matches = re.search('(\w)\\1\\1', hashValue)
        
        if matches != None:
            hashes[i]=hashValue
            print(str(i) + " " +matches.group(0)+" "+hashValue)
            triplet = matches.group(0)
            currettriplet[i]=triplet[0]
        matches = re.search('(\w)\\1\\1\\1\\1', hashValue)
        if matches != None and checkFiveTimesNextThousands(hashValue,currettriplet, i, matches.group(0),onetimepads):   
            if len(globaldict)>=80:
                #print(sorted(onetimepads))
                break
        #print(i)
        
   
onetimepads =[]
currettriplet = {}  
globaldict ={}
hashes={}
part2 = False


findValidOneTimePads(part2,onetimepads, currettriplet )
printglobalDict(globaldict)
print(onetimepads[64])


onetimepads =[]
currettriplet = {}  
globaldict ={}
hashes={}
part2 = False


findValidOneTimePads(part2,onetimepads, currettriplet )
printglobalDict(globaldict)
print(onetimepads[64])
