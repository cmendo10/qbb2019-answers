#!/usr/bin/env python3

# Count total alignments 

count = open("/Users/cmdb/qbb2019-answers/day1-homework/SRR072893.SAM")
match = 0
for line in count:
    fields = line.split("\t")
    for field1 in fields:
        if field1 == "NM:i:0":
           match += 1
print(match)