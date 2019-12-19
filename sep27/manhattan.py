#!/usr/bin/env python3

"""
Manhattan plots
"""
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
colors = [ '#ffe120', '#469991']


#for files in current working director, technically ls -a
for file_name in os.listdir (os.getcwd()):
    if file_name.endswith('.qassoc'):
        pval_by_chromo = {}
        qassoc_file = open(file_name)
        for i, line in enumerate(qassoc_file):
            if i == 0:
                continue
            fields = line.rstrip("\n").split()
            chromo = fields[0]
            p_val = fields[-1]
            if p_val =='NA':
                continue
            pval_by_chromo.setdefault(chromo,[])
            pval_by_chromo[chromo].append(-1*np.log10(float(p_val)))


fig, ax = plt.subplots()
plt.tick_params(axis= "x", which= "both", bottom=False, top=False, labelbottom=False)
previous_points = 0
for i, chromo in enumerate(pval_by_chromo):
    ax.scatter([x+previous_points for x in range(len(pval_by_chromo[chromo]))], pval_by_chromo[chromo], color = colors[i%2])
    previous_points += len(pval_by_chromo[chromo])
    plt.title("Phenotype Association")
    ax.set_xlabel("Chromosome")
    ax.set_ylabel("-log10(P-Value)")
    fig.savefig("pheno_assoc")
    plt.close(fig)