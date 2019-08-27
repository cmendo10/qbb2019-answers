#!/usr/bin/env python3

"""
Parsing file to include flybase gene ids and uniprotect gene ids

usage: ./01-fly.py <gene name file>
"""

import sys

f = open(sys.argv[1])

for i, line in enumerate(f):
    if "DROME" not in line:
        continue
    field = line.split()
    if "FBgn" not in field[-1]:
        continue
    column_1 = field[-1]
    column_2 = field[-2]
    print(column_1, "\t", column_2)