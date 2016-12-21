'''
Created on 20.12.2016

@author: weichslgartner
'''

from heapq import heappush, heappop
from collections import namedtuple
import time

Range = namedtuple('Range',['begin', 'end'])



def findNonBlockedIps(ipList):
    currentIP = 0
    lowestIp = MAXIP
    allowed = 0  
    while ipList:
        element =  heappop(ipList)
        begin = element.begin
        end =element.end
        if begin >currentIP+1:
            if currentIP <  lowestIp:
                lowestIp =currentIP+1
            allowed+= (begin -currentIP -1)
        if end > currentIP:
            currentIP = end
        if debugPrint:
            print(begin, end ="\t")
            print(end, end ="\t")
            print(currentIP, end ="\t")
            print(allowed, end ="\t")
            print(lowestIp, )
    if currentIP < MAXIP:
        allowed+= (MAXIP -currentIP )
    return lowestIp,allowed

    

debugPrint = False
MAXIP=4294967295
ipList =  []
start = time.time()
with open('input20.dat') as file:
    for line in file:
        line.strip()
        tokens = line.split("-")
        heappush(ipList, Range(int(tokens[0]),int(tokens[1])))

lowest, allowed =findNonBlockedIps(ipList)
end = time.time()
print(end - start)

print("Lowest IP: {0} \nNumber of allowed IPs: {1}".format(lowest, allowed))