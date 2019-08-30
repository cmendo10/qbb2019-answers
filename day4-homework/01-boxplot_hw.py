#!/usr/bin/env python3

"""
Usage: ./01-boxplot.py <gene_name> <FPKMS.csv>

Boxplot all transcipts for a given gene"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name")

goi = df.loc[:,"gene_name"] == gene_name #Defined a list of true and falses. We got 25(rows)
# print(goi)
fpkms = df.drop(columns="gene_name") #Drops the column "gene_name" from output

male = fpkms.iloc[:,:8]


female = fpkms.iloc[8:,:]
# print(df.shape)
# print(fpkms.shape)
# print(fpkms.loc[goi,:])

fig, ax = plt.subplots(2)
ax[0].boxplot(male.loc[goi,:].T)
ax[1].boxplot(female.loc[goi,:].T)
ax[0].set_title("Male")
ax[1].set_title("Female")
# ax.boxplot(fpkms.loc[goi,:].T) #Transpose aka invert
fig.savefig("boxplot.png")
plt.close(fig)