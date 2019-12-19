#!/usr/bin/env python3

"""
# Usage: ./00-scatter.py <ctab>
#
# Compare num_exons vs length
"""
import sys
import matplotlib.pyplot as plt

freq = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split()
    freq.append(float(fields[5]))

#print(len(freq))

fig, ax = plt.subplots()
print(len(freq))
ax.hist(freq, bins=100)
plt.title("Allele_Frequency")
ax.set_xlabel("Allele")
ax.set_ylabel("Number of Variants")
fig.savefig("allele_frequency")
plt.close(fig)