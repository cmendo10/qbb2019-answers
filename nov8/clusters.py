#!/usr/bin/env python3

"""
Usage: ./clusters.py <ctab>

Clusters
"""
import sys
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


hema_data = open(sys.argv[1])
df1 = pd.read_csv(hema_data, sep = "\t", names = ["gene_name_", "cfu","poly","unk","int","mys","mid"], index_col = "gene_name_", skiprows=[0])
print(df1)
x = df1["cfu"].values
#print(x)
y = df1["poly"].values
#print(y)
df41 = DataFrame({"cfu": x, "poly": y})
print(df41)
kmeans = KMeans(n_clusters=5).fit(df41)
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(df41['cfu'], df41['poly'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
# plt.show()
plt.savefig('K_Means_Clusters')


