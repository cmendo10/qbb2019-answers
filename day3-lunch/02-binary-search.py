#!/usr/bin/env python3

"""
Binary Search

usage: ./02-binary-search.py <gene name file>
"""

import sys

f = open(sys.argv[1])
gene_list = []
search_pos = 21378950

for i, line in enumerate(f):
    if line.startswith("#"):
        continue
    column = line.rstrip("\n").split()
    chrom = column[0]
    types = column[2]
    gene_start = int(column[3])
    gene_stop = int(column[4])
    gene_name = column[13]
    if types == "gene" and chrom == "3R":
        if 'gene_biotype "protein_coding";' in line:
            gene_list.append(gene_stop)
            gene_list.append(gene_start)

gene_list = sorted(gene_list)

count = len(gene_list)
iterations = 0
while count != 1:
    iterations += 1
    if search_pos < int(gene_list[int(count/2)]):
        gene_list = gene_list[:int(count/2)]
    
    elif search_pos > int(gene_list[int(count/2)]):
        gene_list = gene_list[int(count/2):]
    count = int(count/2)
    
location = gene_list[count]

print(location)    

for i, line in enumerate(open(sys.argv[1])):
   column = line.rstrip("\n").split()
   if line.startswith("#"):
       continue
   chrom = column[0]
   types = column[2]
   gene_start = int(column[3])
   gene_stop = int(column[4])
   gene_name = column[13]
   if types == "gene" and chrom == "3R" and "protein_coding" in line:
           if str(location) in line:
               gene_id = str(column[13])
               print(gene_id)
               
                    
print(abs(location - search_pos))
print(iterations)
print(gene_id)