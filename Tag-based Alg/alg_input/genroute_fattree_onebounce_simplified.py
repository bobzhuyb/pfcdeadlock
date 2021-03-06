

import sys
import os

if len(sys.argv) < 2:
    print "genroute_fattree.py k"
    sys.exit(1)

k= int(sys.argv[1])
TorNum = k*k/2
LeafNum = k*k/2
SpineNum = k*k/4
ServerPerTor = k/2
SwitchNum = TorNum + LeafNum + SpineNum
ServerNum = ServerPerTor*TorNum
LinkNum = ServerNum + LeafNum*k

#f_path = "D:\\simulation_code\\tagging_algorithm_input\\route_fattree.txt"
#out = open(f_path, "w")


						
for pod1 in range(k):
	for pod2 in range(k):
		if pod1 != pod2:	
			firsttor1 = pod1*k/2
			lasttor1 = firsttor1 + k/2
			firstleaf1 = TorNum + pod1*k/2
			lastleaf1 = firstleaf1 + k/2
		
			firsttor2 = pod2*k/2
			lasttor2 = firsttor2 + k/2
			firstleaf2 = TorNum + pod2*k/2
			lastleaf2 = firstleaf2 + k/2

			
			for tor1 in range(firsttor1, lasttor1):
				for tor2 in range(firsttor2, lasttor2):
					server1 = tor1*k/2 + SwitchNum
					server2 = tor2*k/2 + SwitchNum 
					for leaf1 in range(firstleaf1, lastleaf1):
						firstspine = TorNum+LeafNum + (leaf1-firstleaf1)*k/2
						lastspine = firstspine + k/2
						for spine in range(firstspine, lastspine):
							leaf2 = firstleaf2 + leaf1 - firstleaf1

							#print src_pod bounce paths
							for srcbounceleaf in range(firstleaf1, lastleaf1):
								if srcbounceleaf != leaf1:
									for srcbouncetor in range(firsttor1, lasttor1):
										if srcbouncetor != tor1: 
											sys.stdout.write(str(server1) + " " + str(tor1) + " " + str(srcbounceleaf) + " " + str(srcbouncetor) + " " + str(leaf1) + " " + str(spine) + " " + str(leaf2) + " " + str(tor2) + " " + str(server2))
											sys.stdout.write("\n")
	

							#print dst_pod bounce paths
							for dstbounceleaf in range(firstleaf2, lastleaf2):
								if dstbounceleaf != leaf2:
									for dstbouncetor in range(firsttor2, lasttor2):
										if dstbouncetor != tor2: 
											sys.stdout.write(str(server1) + " " + str(tor1) + " " + str(leaf1) + " " + str(spine) + " " + str(leaf2) + " " + str(dstbouncetor) + " " + str(dstbounceleaf) + " " + str(tor2) + " " + str(server2))
											sys.stdout.write("\n")
