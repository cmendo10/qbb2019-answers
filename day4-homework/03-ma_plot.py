#!/usr/bin/env python3

"""
Usage: ./03-ma_plot.py <sample1> <sample2>

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

# fpkm = {"sample1" : [1, 2, 3],
#         "sample2" : [4, 5, 6]}
fpkm = {name1: ctab1.loc[:,"FPKM"],
        name2: ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm)
df+=1

r=df.loc[:,name2]
g=df.loc[:,name1]
y=np.log2(r/g)
x=0.5*np.log2(r*g)

fig, ax = plt.subplots()
ax.scatter(x,y, s=3, alpha=0.5)

# ax.scatter(my_data, my_data2, c="blue", alpha=0.1)
fig.suptitle("Male and Female FPKMS")
ax.set_xlabel("logFPKM")
ax.set_ylabel("Frequency")

fig.savefig("ma_plot.png")
plt.close(fig)