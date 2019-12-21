#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# import plotly.graph_objects as go

y_values = []
x_values = []


arg1 = open((sys.argv[1]))

for line in arg1:
   if line.startswith("#"):
       continue
   column = line.rstrip("\n").split("\t")
   x_values.append(int(column[8]))
   y_values.append(int(column[5]) - int(column[4]))
   

fig, ax = plt.subplots()
plt.title("Contigs vs references")
ax.scatter(x_values, y_values)
ax.set_xlabel("Total length of contigs")
ax.set_ylabel("Length of reference")
ax.scatter(x_values, y_values)
fig.savefig("reference2__contig.png")
plt.close(fig)