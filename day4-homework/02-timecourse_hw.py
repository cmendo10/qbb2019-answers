#!/usr/bin/env python3

"""
Usage: ./02-timecourse.py <t_name> <samples.csv> <FPKMs> <sex>
Create a time course of a given transcript for a sex
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

def get_fpkms(sample_file,sex_,ctab_dir):
   fpkms = []
   for i, line in enumerate(sample_file):
       if i==0:
           continue
       fields = line.rstrip("\n").split(",")
       sample = fields[0]
       sex = fields[1]
       stage = fields[2]
       if sex != sex_:
           continue
       ctab = os.path.join(ctab_dir,sample,"t_data.ctab")
       df = pd.read_csv(ctab,sep='\t', index_col="t_name")
       fpkms.append(df.loc["FBtr0331261","FPKM"])
   return fpkms

#Specify transcript of interest

    #Load metadata
def pick_sex(ax, fpkms, sex, transcript, color):
    ax.plot(range(8), fpkms.loc[transcript,:], label=sex, color=color)

t_name = sys.argv[1]   
samples = pd.read_csv(sys.argv[2])

    # soi = samples.loc[:,"sex"] == "x"
    # stages = samples.loc[soi,"stage"]

    # print(srr_ids)

    #Load FPKMs
fpkms = pd.read_csv(sys.argv[3], index_col="t_name")
fpkms = fpkms.drop(columns="gene_name")
male = fpkms.iloc[:,:8]
female = fpkms.iloc[:,8:]

male_rep = get_fpkms(open(sys.argv[4]),"male",sys.argv[5])
female_rep = get_fpkms(open(sys.argv[4]),"female",sys.argv[5])

column_names=[0,10,11,12,13, "14A", "14B", "14C", "14D"]

sex_label = ["male", "female"]
fig, ax = plt.subplots()
ax.set_xticklabels(column_names, rotation=90)
pick_sex(ax, male, "male", t_name, "blue")
pick_sex(ax, female, "female", t_name, "red")


ax.plot(range(4,8),male_rep,'x',label="male rep",color='blue')
ax.plot(range(4,8),female_rep,'x',label="female rep",color='red')



    #Extract data
    # my_data = []
 #    for stage in stages:
 #        # print(srr_id)
 #        my_data.append(fpkms.loc[t_name,"x_"+stage])

    # print(my_data)
plt.legend(loc = "center left", bbox_to_anchor=(1,.5))
plt.tight_layout()

plt.title("Sxl")
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mRNA abundance (RPKM)")
fig.savefig("re_timecourse1.png")
plt.close(fig)

    

    
    
    
    
    
    
    
    