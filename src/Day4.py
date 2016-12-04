'''
Created on 02.12.2016

@author: weichslgartner



'''


import re


#97-122
def decrypt(word,rotate):
    plain =''
    for char in word:
        if '-' == char :
            plain = plain+ " "
        else:
            number =  ord(char) - ord('a') 
            number += int(rotate)
            number %= ord('z')- ord('a') +1
            number += ord('a') 
            plain +=chr(number)  
    # print(plain)
    return plain
    
    
    
def generateChecksum(word):
    word = re.sub('-','',word)
    charMap = {}
    for char in word:
        if char in charMap: 
            charMap[char] = charMap[char]+1
        else:
            charMap[char] = 1
    charMap =sorted(charMap.items(),key = lambda x: x[0])
    valueSort = sorted(charMap,key = lambda x: x[1],reverse=True)
    checksum = ''
    for i in range(0,5):
        checksum += valueSort[i][0]
    return checksum

with open('input4.dat') as file:
    idsum = 0
    found=0
    for line in file:
        sectorID = re.findall("\d+", line)
        roomName = re.findall("[a-z-]+", line)
        checksum = re.findall("\[[a-z]+\]",line)
        checksum[0] = re.sub(r'\[|\]','',checksum[0])
        #print(sectorID[0])
        #print(roomName[0])
        #print(checksum[0])
        if generateChecksum(roomName[0]) ==  checksum[0]:
            idsum += int(sectorID[0])
        plain = decrypt( roomName[0], sectorID[0])
        if re.search("north", plain) != None:
            print(plain+sectorID[0] )
            found = int(sectorID[0]) 
    print('Part 1: {0}'.format(idsum))
    print('Part 2: {0}'.format(found))