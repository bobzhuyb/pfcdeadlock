import os
import sys



f=open(sys.argv[1])
lines = f.readlines()
f.close()

for eachLine in lines:
    words = eachLine.split()

    #print "python alg_input/gentopo_jellyfish.py " + words[0] + " " + words[1] + " " + words[2] + " " + "> alg_input/topo_jellyfish_" + words[0] + "_" + words[1] + "_" + words[2]
    os.system("python alg_input/gentopo_fattree.py " + words[0] + " > alg_input/topo_fattree_" + words[0])

    #print "python alg_input/genroute_jellyfish.py " + " alg_input/topo_jellyfish_" + words[0] + "_" + words[1] + "_" + words[2] + " " + words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " > alg_input/route_jellyfish_" + words[0] + "_" + words[1] + "_" + words[2] + "_" + words[3]
    os.system("python alg_input/genroute_fattree_simplified.py" + " " + words[0] + " > alg_input/route_fattree_simplified_" + words[0])
    os.system("python alg_input/genroute_fattree_onebounce_simplified.py" + " " + words[0] + " >> alg_input/route_fattree_simplified_" + words[0])

    #print "python tag_based_alg.py " + " alg_input/topo_jellyfish_" + words[0] + "_" + words[1] + "_" + words[2] + " alg_input/route_jellyfish_" + words[0] + "_" + words[1] + "_" + words[2] + "_" + words[3]
    sys.stdout.write(words[0] + " ")
    sys.stdout.flush() 
    os.system("python tag_based_alg.py " + " alg_input/topo_fattree_" + words[0] + " alg_input/route_fattree_simplified_" + words[0])
