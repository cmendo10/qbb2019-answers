#!/usr/bin/env python3

# Count total alignments 

count = open("/Users/cmdb/qbb2019-answers/day1-homework/SRR072893.SAM")
hits = 0
for line in count:
    fields = line.rstrip("\n").split("\t")
    for field1 in fields:
        if field1 == "NH:i:1":
            hits += 1
print(hits)