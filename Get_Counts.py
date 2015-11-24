# -*- coding: utf-8 -*-
#"""
#Created on Wed Nov 18 14:35:33 2015

#@author: simmonsma3


import os
os.chdir('/Users/simmonsma3/Documents/Alzheimers_and_AMD')
#AMDcur = open('AMD_curated_genes_f.csv','r')
#ADcur = open('AD_genes.csv')
#ADmut = open('AD_SNPS.csv')
#AMDmut = open('AMD_SNPS.csv')

import pandas as pd

df = pd.read_csv('AMD_SNPS.csv')
df1 = df['Gene Name']

def GetCounts(data_frame, csv_name):
    unique = []
    
    for i in data_frame:
        if i not in unique:
            unique.append(i)
    
    final = {}
    
    for i in unique:
        count = 0 
        for j in data_frame:
            if i == j:
                count += 1
        final[i] = count
    
    df2 = pd.DataFrame.from_dict(final, orient = 'index')
    
    df2.to_csv(csv_name)
    
    print (df2)
