#!/usr/bin/env python3

# Count total alignments 

count = open("/Users/cmdb/qbb2019-answers/day1-homework/SRR072893.SAM")
bases = 0
for line in count:
    fields = line.split("\t")
    if fields[2] != "2L":
        continue
    if int(fields[3]) >= 10000 and int(fields[3]) <=20000:
        bases += 1
print(bases)