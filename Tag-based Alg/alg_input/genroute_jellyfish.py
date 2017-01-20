#!/usr/bin/env python

import sys
import os
from igraph import *
from yen_alg import yen_ksp

if len(sys.argv) < 6:
    print "gentopo_jellyfish.py topo_file switch_num switch_degree switch_degree_to_switch perpair_path_num"
    sys.exit(1)

topo = {}
f = open(sys.argv[1])
lines = f.readlines()
f.close()

for eachLine in lines:
    words = eachLine.split()
    tempdic = {}
    for i in range(len(words[1:])):
        tempdic[words[i+1]] = 1
    topo[words[0]] = tempdic

N = int(sys.argv[2])
k = int(sys.argv[3])
r = int(sys.argv[4])
m = int(sys.argv[5])
serverperswitch = k-r
ServerNum = N*serverperswitch

for server1 in range(ServerNum):
    for server2 in range(ServerNum):
        if server1 != server2:
            #print "src dst = ", str(server1+N), str(server2+N)
            temptopo = deepcopy(topo)
            paths = yen_ksp(temptopo, str(server1+N), str(server2+N), m)
            for path in paths:
                for node in path[0]:
                    sys.stdout.write(" " + node)
                print

