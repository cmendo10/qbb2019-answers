#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



ctab_dir = sys.argv[1]


for i, line in enumerate(open(ctab_dir)):
    fields = line.rstrip("\n").split("\t")
    if i == 0:
        continue
    if fields[2] == "+":
        promoter_left = int(fields[3]) - 500
        promoter_right =  int(fields[3]) + 500
        
    if fields[2] == "-":
        promoter_left = int(fields[4]) - 500
        promoter_right =  int(fields[4]) + 500
    if promoter_left <= 0:
        promoter_left = 0
    print(fields[1], promoter_left, promoter_right, fields[5], sep="\t")
        


