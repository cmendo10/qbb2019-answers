#!/usr/bin/env python3

"""
# Usage: ./00-scatter.py <ctab>
#
# Compare num_exons vs length
"""
import sys
import matplotlib.pyplot as plt

component1 = []
component2 = []

for i, line in enumerate(open(sys.argv[1])):
    fields = line.rstrip("\n").split("\t")
    component1.append(float(fields[2]))
    component2.append(float(fields[3]))
    
fig, ax = plt.subplots()
ax.scatter(component1, component2)
plt.title("PCA_genetic_relatedness")
ax.set_xlabel("PCA component 1")
ax.set_ylabel("PCA component 2")
fig.savefig("gen_relatedness")
plt.close(fig)