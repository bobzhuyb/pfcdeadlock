#!/usr/bin/env python

import sys
from copy import deepcopy
from igraph import *

INIT_TAG = 8

if len(sys.argv) < 3:
    print "tag_based_alg.py topo_file route_file"
    sys.exit(1)

if len(sys.argv) >= 4:
    from tag import ClosTag as TTLTag
else:
    from tag import TTLTag

topo = {}
f = open(sys.argv[1])
lines = f.readlines()
f.close()

for eachLine in lines:
    words = eachLine.split()
    topo[words[0]] = words[1:]

f = open(sys.argv[2])
lines = f.readlines()
f.close()
routes = [0] * len(lines)

for i in range(len(lines)):
    routes[i] = lines[i].split()

switch_map = {}

for switch in topo:
    switch_map[switch] = TTLTag(switch)
    for port in topo[switch]:
        switch_map[switch].add_port(port) 

for route in routes:
    tag = INIT_TAG
    last_hop = ""
    for i in range(len(route)):
        hop = route[i]
        switch_map[hop].register_port_tag(last_hop, tag)
        if i < len(route) - 1:
            tag = switch_map[hop].get_new_tag(tag, last_hop, route[i+1])
        last_hop = hop

# Port Tag Format: ('A', 4, 6)
porttag_id_map = {}
id_porttag_map = {}
count = 0
for switch in switch_map:
     for each in switch_map[switch].get_all_tagged_ports():
         porttag_id_map[each] = count
         id_porttag_map[count] = each
         count += 1

porttag_edges = {}

for i in range(count):
    for j in range(count):
        if i==j:
            continue
        if switch_map[id_porttag_map[i][0]].is_port_dependency(
            id_porttag_map[i][1], id_porttag_map[i][2],
            switch_map[id_porttag_map[j][0]], id_porttag_map[j][1], id_porttag_map[j][2]):
            porttag_edges[(i, j)] = 1

output = []
porttag_priority_map = {}
inter_s_edges = {}
v = deepcopy(porttag_id_map)
t = INIT_TAG

s = {}
output.append(s)
while t>=0:
    left_over = False
    porttag_list = v.keys()
    for porttag in porttag_list:
        if porttag[2] != t:
            continue

        #####################
        # try this port_tag #
        #####################
        s[porttag] = 1
        
        ###############################
        # build port dependency graph #
        ###############################
        pdg_v = {}
        pdg_e = {}
        for pt in s:
            if (pt[0], pt[1]) not in pdg_v:
                pdg_v[(pt[0], pt[1])] = len(pdg_v.keys())
        for pt0 in s:
            for pt1 in s:
                if pdg_v[(pt0[0], pt0[1])] == pdg_v[(pt1[0], pt1[1])]:
                    continue
                if (porttag_id_map[pt0], porttag_id_map[pt1]) in porttag_edges:
                    pdg_e[(pdg_v[(pt0[0], pt0[1])], pdg_v[(pt1[0], pt1[1])])] = 1

        pdg = Graph(pdg_e.keys(), directed=True)

        ###############################
        # check port dependency graph #
        ###############################
        if not pdg.is_dag():
            s.pop(porttag)
            left_over = True
            continue
        
        ######################
        # accept this vertex #
        ######################
        v.pop(porttag)
        porttag_priority_map[porttag] = len(output) - 1

    if left_over:
        #####################
        # add inter_s_edges #
        #####################
        for edge in porttag_edges:
            pt0 = id_porttag_map[edge[0]]
            pt1 = id_porttag_map[edge[1]]
            if (pt0 in s) and (pt1 not in s):
                inter_s_edges[(pt0, pt1)] = 1

        ################
        # create new s #
        ################
        s = {}
        output.append(s)
    else:
        t -= 1

print "Required Traffic Classes"
print "############################"

print "Class 0: lossy"
for i in range(len(output)):
    print "Class %d: lossless" % (i + 1)

print ""
print "ACL Rules"
print "############################"

for priority in range(len(output)):
    for porttag in output[priority]:
        print "On switch %s, port %d, match packets with tag=%d, assign to class %d" % (
            porttag[0], porttag[1], porttag[2], len(output) - priority
        )

print ""
print "Special PFC Configurations"
print "############################"

dedup = {}
for e in inter_s_edges:
    tmp = (e[0][0], e[0][1], len(output) - porttag_priority_map[e[1]], len(output) - porttag_priority_map[e[0]])
    if tmp not in dedup:
        print "On switch %s, port %d, when receive PAUSE of priority %d, pause egress queue %d" % (tmp)
        dedup[tmp] = 1
