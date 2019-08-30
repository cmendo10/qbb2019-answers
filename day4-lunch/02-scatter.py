#!/usr/bin/env python3

"""
Usage: ./02-scatter.py <ctab1> <ctab2>

Plot 2 sets of FPKM in Scatter
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly ###
import scipy.stats as stats
plt.style.use('ggplot')
from sklearn import datasets

fpkms = []
fpkms2 = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    fpkms.append(float(fields[-1])+1)

for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    fpkms2.append(float(fields[-1])+ 1)


print(len(fpkms))

my_data = np.log2(fpkms)
my_data2 = np.log2(fpkms2)



# mu = float(sys.argv[2])
# sigma = float(sys.argv[3])
# x = np.linspace(-15, 15, 100)

#print(y)
#print(type(y))

#fig = entire image, ax = a panel such as (fig, (ax, ax2...))

"""
Graphing the normal distribution
"""
# y = stats.norm.pdf(x, mu, sigma )

# fig, ax = plt.subplots()
# ax.hist(my_data, bins=100, density=True)
# ax.plot(x, y)
# fig.savefig("norm_fpkms.png")
# plt.close(fig)

"""
Graphing the SKEW normal distribution
"""
# a = float(sys.argv[4])
# y2 = stats.skewnorm.pdf(x, a, mu, sigma)

coefs = np.polyfit(my_data, my_data2, 1) ###
my_data_new = np.linspace(0, 12, 100) ###
f = np.poly1d(coefs)
# print(f)
y = f(my_data_new)
print(y)

fig, ax = plt.subplots()
ax.scatter(my_data, my_data2, c="blue", alpha=0.1)
ax.plot(my_data_new,y)
fig.suptitle("Scatter of SRR07893 and SRR07894")
ax.set_xlabel("SRR07893")
ax.set_ylabel("SRR07894")
fig.savefig("scatter.png")
plt.close(fig)



# ffit = poly.polyval(coefs, my_data_new) ###
# plt.plot(my_data_new, ffit) ###

### Numpy Fit Line from Class Answers Review
# log_ctab = np.log2(ctab)
# log_ctab2 = np.log2(ctab2)
# coef = np.polyfit(log_ctab, log_ctab2)

# Simpler terms: p = np.polyfit(fpkm1, fpkm2, 1)
#                 print(p)
#             or  d = no.poly1d(p)
#                 print(d)

##### Exercise 3 #####



# print(y)
# print(type(y))

# ax.plot(x, y2)
# ax.plot(x, y, color="black") #normal distribution

# plt.text(-10, 0.2, "Mu="+str(mu),
#          fontsize=20)
# plt.text(-10, 0.15, "Sigma="+str(sigma),
#          fontsize=20)
# plt.text(-10, 0.10, "a="+str(a),
#          fontsize=20)
# ax.legend(labels=["Skewnorm", "Norm"], loc="upper right")
# fig.savefig("skewnorm_fpkms.png")
# plt.close(fig)

