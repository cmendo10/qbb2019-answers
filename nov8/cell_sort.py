#!/usr/bin/env python3

"""
Usage: ./cell_sort.py <ctab>

Heat map
"""
import sys
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import numpy as np

# fig, ax = plt.subplots()
# ax.set_title("AKSM V142A")
# ax.scatter([0,75], [0,15])
# ax.plot([0,75], [0,15]) # , color="red")

df1 = pd.read_csv(sys.argv[1],sep = "\t", names = ["gene_name_", "cfu","poly","unk","int","mys","mid"], index_col = "gene_name_")
genedf = df1.iloc[1:,:] 
gene_list = df1.index.tolist()
# print(gene_list)
T_genedf = genedf.transpose() 
celltype_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
# print(genedf)
# print(T_genedf)
Z1 = linkage(genedf, 'average')
Z2 = linkage(T_genedf, 'average')
# print(Z2)
k1 = leaves_list(Z1)
k2 = leaves_list(Z2)
# print(k1)
# print(k2)

gened_f1 = genedf.iloc[k1,:]
gened_f2 = gened_f1.iloc[:,k2]
# print(gened_f2)

FPKM_matrix = gened_f2.values.astype(float)
fig, ax = plt.subplots()
im = ax.imshow(FPKM_matrix, aspect = "auto")
ax.set_xlabel("Cell Type")
ax.set_ylabel("Gene")
ax.set_title("Heatmap of Cell Types")
fig.colorbar(im, ax = ax)
# plt.colorbar()
# plt.show()
plt.savefig("Heat_Map")