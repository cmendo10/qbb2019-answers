#!/usr/bin/env python3

# Count total alignments 

count = open("/Users/cmdb/qbb2019-answers/day1-homework/SRR072893.SAM")
counter = 0
for line in count:
    fields = line.split("\t")
    if fields[5] == "*":
        continue
    else:
        counter += 1
            
print(counter)