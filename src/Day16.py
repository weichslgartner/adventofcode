'''
Created on 16.12.2016

@author: weichslgartner
'''


def dragonFractal(inputString):
    b = list(inputString[::-1])
    for i,char in enumerate(b):
        if char == '1':
            b[i]= '0'
        elif char == '0':
            b[i]= '1'
        else:
            print("Wrong Input string")
    return inputString+'0'+''.join(b)

def generateCheckSum(word):
    resultList = []
    for i in range(0,len(word)-1,2):
        if word[i:i+2] == '11' or word[i:i+2] == '00':
            resultList.append('1')
        else:
            resultList.append('0')
    resultString = ''.join(resultList)
    if len(resultList) % 2 == 0:
        resultString = generateCheckSum(resultString)
    return resultString

puzzleInput = '10010000000110000'
desiredLength = 35651584

while len(puzzleInput) < desiredLength:
    puzzleInput = dragonFractal(puzzleInput)
    
    

print(generateCheckSum(puzzleInput[0:desiredLength]))