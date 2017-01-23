import sys
from random import randint

f = open(sys.argv[1])
lines = f.readlines()
f.close()

topo = {}
for eachLine in lines:
    words = eachLine.split()
    topo[words[0]] = words[1:]

N = int(sys.argv[2])
k = int(sys.argv[3])
r = int(sys.argv[4])
serverperswitch = k-r
ServerNum = N*serverperswitch
NodeNum = ServerNum + N
random_pathnum = int(sys.argv[5])

for i in range(random_pathnum):
    hoplimit = randint(1,20)
    currenthop = str(randint(N, NodeNum-1))
    sys.stdout.write(currenthop)
    while hoplimit > 0 :
        neighbornum = len(topo[currenthop]) 
        nexthop = topo[currenthop][randint(0,neighbornum-1)]
        sys.stdout.write(" " + nexthop)
        currenthop = nexthop
        hoplimit -= 1
    print

