from collections import defaultdict


regdict = defaultdict(lambda : 0)
#part 1
regdict['c']=0
#part 2
regdict['c']=1
file = open("input12.dat")
lines = [line.rstrip('\n') for line in file]
print(lines)
file.close()
pc = 0
while pc < len(lines):
    line = lines[pc]
    tokens = line.split(" ")
    if line.startswith("cpy"):
        target= 0
        if tokens[1].isdigit():
            target = int(tokens[1])
        else:
            target =regdict[tokens[1]]

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
        if tokens[1].isdigit():
            target = int(tokens[1])
        else:
            target =regdict[tokens[1]]
        if  target != 0:
            pc+=int(tokens[2])
        else:
            pc+=1
print(regdict['a'])