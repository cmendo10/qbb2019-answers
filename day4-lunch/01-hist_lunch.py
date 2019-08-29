#!/usr/bin/env python3

"""
Usage: ./01-hist.py <ctab> <mu value> <sigma value> <skew value>

Plot FPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append(float(fields[-1]))

print(len(fpkms))

my_data = np.log2(fpkms)
mu = float(sys.argv[2])
sigma = float(sys.argv[3])
x = np.linspace(-15, 15, 100)

#print(y)
#print(type(y))

#fig = entire image, ax = a panel such as (fig, (ax, ax2...))

"""
Graphing the normal distribution
"""
y = stats.norm.pdf(x, mu, sigma )

fig, ax = plt.subplots()
ax.hist(my_data, bins=100, density=True)
ax.plot(x, y)
fig.savefig("norm_fpkms.png")
plt.close(fig)

"""
Graphing the SKEW normal distribution
"""
a = float(sys.argv[4])
y2 = stats.skewnorm.pdf(x, a, mu, sigma)

fig, ax = plt.subplots()
ax.hist(my_data, bins=100, density=True)
ax.plot(x, y2)
ax.plot(x, y, color="black") #normal distribution
fig.suptitle("Norm and Skewnorm of SRR07893")
ax.set_xlabel("log(FPKM)")
ax.set_ylabel("Frequency")
plt.text(-10, 0.2, "Mu="+str(mu),
         fontsize=20)
plt.text(-10, 0.15, "Sigma="+str(sigma),
         fontsize=20)
plt.text(-10, 0.10, "a="+str(a),
         fontsize=20)
ax.legend(labels=["Skewnorm", "Norm"], loc="upper right")
fig.savefig("skewnorm_fpkms.png")
plt.close(fig)

