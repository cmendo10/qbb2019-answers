#!/usr/bin/env python3

"""
Parsing BDGP6 file

usage: ./01-BDGP.py <gene name file>
"""

import sys

f = open(sys.argv[1])
length = 0
pc = []
search_pos = 21378950

for i, line in enumerate(f):
    if "protein_coding" in line:
        field = line.rstrip("\n").split("\t")
        if field[0] == "3R" and field[2] == "gene":
            pc.append(line)
            length += 1
            print(line)
            


print(length)