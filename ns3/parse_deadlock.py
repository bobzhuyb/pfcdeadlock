# 2.001647 /0 1.8>1.7 u 38084 4984 3 

import sys

f = open(sys.argv[1])
lines = f.readlines()
f.close()

out380 = open("trace380.txt", "w")
out381 = open("trace381.txt", "w")
out382 = open("trace382.txt", "w")
out388 = open("trace388.txt", "w")

out540 = open("trace540.txt", "w")
out541 = open("trace541.txt", "w")
out542 = open("trace542.txt", "w")
out544 = open("trace544.txt", "w")

out760 = open("trace760.txt", "w")
out761 = open("trace761.txt", "w")
out762 = open("trace762.txt", "w")
out766 = open("trace766.txt", "w")


for each in lines:
	words = each.split()
	if words[3] == "u":
		if words[2] == "1.8>1.7" and words[1] == "/0":
			print >> out760, words[0], words[5]
		if words[2] == "1.4>1.9" and words[1] == "/0":
			print >> out380, words[0], words[5]
		if words[2] == "1.6>1.5" and words[1] == "/0":
			print >> out540, words[0], words[5]
		if words[2] == "1.8>1.7" and words[1] == "/1":
			print >> out761, words[0], words[5]
		if words[2] == "1.4>1.9" and words[1] == "/1":
			print >> out381, words[0], words[5]
		if words[2] == "1.6>1.5" and words[1] == "/1":
			print >> out541, words[0], words[5]
		if words[2] == "1.8>1.7" and words[1] == "/2":
			print >> out762, words[0], words[5]
		if words[2] == "1.4>1.9" and words[1] == "/2":
			print >> out382, words[0], words[5]
		if words[2] == "1.6>1.5" and words[1] == "/2":
			print >> out542, words[0], words[5]
		if words[2] == "1.8>1.7" and words[1] == "/6":
			print >> out766, words[0], words[5]
		if words[2] == "1.4>1.9" and words[1] == "/8":
			print >> out388, words[0], words[5]
		if words[2] == "1.6>1.5" and words[1] == "/4":
			print >> out544, words[0], words[5]