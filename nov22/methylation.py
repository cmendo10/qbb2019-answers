#!/usr/bin/env python3

import sys

#SRR1035452_1_bismark_bt2_pe.bedGraph
#SRR1035454_1_bismark_bt2_pe.bedGraph

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])

inputs = []
overlap = []

fileuniq1 = []
fileuniq2 = []

for i, line in enumerate(file1):
    if i == 0:
        continue
    inputs.append(line)
    

counter = 0
for i, line in enumerate(file2):
    if i == 0:
        continue
    if line not in inputs:
        fileuniq2.append(line)
    else:
        overlap.append(line)
    counter += 1
for item in inputs:
    if item not in overlap:
        fileuniq1.append(item)
        
print(fileuniq2)
