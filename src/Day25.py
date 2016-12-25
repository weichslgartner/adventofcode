from collections import defaultdict
import copy
import sys


regdict = defaultdict(lambda : 0)



def interpretProgram(lines,regdict):
    pc = 0
    outlist =[]
    eternal = 100
    while pc < len(lines):
        #print (lines[pc] )
        line = lines[pc]
        tokens = line.split(" ")
        if line.startswith("cpy"):
            target= 0
            if tokens[1].isdigit() or tokens[1][0]=='-':
                target = int(tokens[1])
            else:
                target =regdict[tokens[1]]
            
            if tokens[2].isdigit():
                continue
            regdict[tokens[2]] = target
            pc+=1
        elif  line.startswith("out"):  
            value=regdict[tokens[1]]
            if value < 0 or value > 1:
                return False
            outlist.append(value)
            if len(outlist) >=  2 and outlist[-1] == outlist[-2]:
                return False
            if len(outlist) > eternal:
                print(outlist)
                return True
            pc+=1
        elif line.startswith("mult"):
            regdict[tokens[3]] += regdict[tokens[2]]*regdict[tokens[1]]
            pc+=1
        elif line.startswith("inc"):
            regdict[tokens[1]] = regdict[tokens[1]]+1
            pc+=1
        elif line.startswith("dec"):
            regdict[tokens[1]] = regdict[tokens[1]]-1
            pc+=1
        elif line.startswith("jnz"):
            target= 0
            increment = 0
            if tokens[1].isdigit():
                target = int(tokens[1])
            else:
                target =regdict[tokens[1]]
            if not tokens[2].isdigit() and tokens[2][0]!='-':
                increment=regdict[tokens[2]]
            else:
                increment = int(tokens[2])
            if increment ==0:
                increment =1
            if  target != 0:
                pc+=increment
            else:
                pc+=1
        elif line.startswith("tgl"):
            target = regdict[tokens[1]]
            if pc+target >= len (lines) or pc+target <0:
                pc+=1
                continue
            toToggle = lines[pc+target]
            toggletokens = toToggle.split(" ")
            if len(toggletokens) == 2:
                if toggletokens[0]== 'inc':
                    toggletokens[0] = 'dec'
                else:
                    toggletokens[0] = 'inc'
            else:
                if toggletokens[0]== 'jnz':
                    toggletokens[0] = 'cpy'
                else:
                    toggletokens[0] = 'jnz'       
            lines[pc+target] = ' '.join(toggletokens)    
            pc+=1 
    return False
#part 2
#regdict['c']=0
file = open("input25.dat")
lines = [line.rstrip('\n') for line in file]
print(lines)
file.close()
found = False

for i in range(sys.maxsize):
    regdict.clear()
    regdict['a']=i
    found = interpretProgram(copy.deepcopy(lines), regdict)
    if found:
        print(i)
        break
