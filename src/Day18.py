TRAP = '^'
SAFE ='.'


def printTrapList(trapList):
    for row in trapList:
        for element in row:
            print(element, end="")
        print()
def countSafeTiles(trapList):
    safeCount =0
    for row in trapList:
        for element in row:
            if element == SAFE:
                safeCount +=1
    return safeCount

def generateNextLine(trapList,numbRows):
    safecount = 0
    for i in range(1,numbRows):
        currentLine =[]
        for j,element in enumerate(trapList[i-1]):
            center = element
            left = SAFE
            right = SAFE
            if j>0:
                left = trapList[i-1][j-1]
            if j < len(trapList[i-1])-1:
                right = trapList[i-1][j+1]
#             if left==TRAP and center==TRAP and  right == SAFE:
#                 currentLine.append(TRAP)
#             elif left==SAFE and center==TRAP and  right == TRAP:
#                 currentLine.append(TRAP)

            if left==TRAP and  right == SAFE:
                currentLine.append(TRAP)
            elif left==SAFE and  right == TRAP:
                currentLine.append(TRAP)
            else: 
                currentLine.append(SAFE)
                safecount+=1
        trapList.append(currentLine)
    return safecount
        
start = '.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'
trapList = []
trapList.append(list(start))
generateNextLine(trapList,40)
print(countSafeTiles(trapList))
del trapList[1:len(trapList)]
safeCount = generateNextLine(trapList,400000)
print(safeCount)
#print(countSafeTiles(trapList))