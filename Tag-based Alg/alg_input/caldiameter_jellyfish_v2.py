#!/usr/bin/env python

import sys
import os
from igraph import *
from yen_alg import *

if len(sys.argv) < 6:
    print "genroute_jellyfish_v2.py topo_file switch_num switch_degree switch_degree_to_switch perpair_path_num"
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


netdiameter = 0
for server1 in range(ServerNum):
    #temptopo = deepcopy(topo)
    dist, pred = dijkstra(topo, str(server1+N))
    path = []
    for server2 in range(ServerNum):
        if str(server2+N) in pred:
            path = predecessor_to_path(pred, str(server1+N), str(server2+N))
            if (len(path)-1) > netdiameter:
                netdiameter = len(path)-1      
            
sys.stdout.write("netdiameter=" + str(netdiameter)+" ")
