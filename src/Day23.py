from collections import defaultdict


regdict = defaultdict(lambda : 0)
#part 1
regdict['a']=12
#part 2
#regdict['c']=0
file = open("input23.dat")
lines = [line.rstrip('\n') for line in file]
print(lines)
file.close()
pc = 0
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
    #print(lines)
    #print(regdict['a'])   
    #print(regdict.items())
    #print(pc)
    #print(lines[pc])
print(regdict['a'])