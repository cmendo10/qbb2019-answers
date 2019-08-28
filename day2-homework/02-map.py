#!/usr/bin/env python3

"""
Mapping identifier
usage: ./02-map.py <fly-parsed-file> <mapping-file> <Choose "Default" or "Nothing">
"""

import sys
f = open(sys.argv[1])
f2 = open(sys.argv[2])
gene_dictionary = {}

for i, line in enumerate(f):
    fields = line.rstrip("\n").split("\t")
    gene_id = fields[0]
    uniprot = fields[1]
    gene_dictionary[gene_id] = uniprot


for i, line in enumerate(f2):
    fields = line.rstrip("\n").split("\t")
    flybase = fields[8]
    line = line.rstrip("\n")
    if flybase in gene_dictionary:
        uniprot_name = gene_dictionary[flybase]
        print(line, uniprot_name)
    elif flybase not in gene_dictionary and sys.argv[3] == "Default":
        print(line, "No Match")
    elif flybase not in gene_dictionary and sys.argv[3] == "Nothing":
        continue
    

