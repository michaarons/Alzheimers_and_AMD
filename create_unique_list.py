# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:56:46 2015

@author: simmonsma3
Takes a directory location and a file_input of a list of entities and returns \
a column in a csv file (output) with the same list with duplicates removed
"""
def uniquelist(directory, file_input, output):
    #find the directory
    import os
    os.chdir(directory)
# '/Users/simmonsma3/Documents/Alzheimers_and_AMD'    
    #Need to set file_out for creating the final file - note the 'w' designation
    file_out = open(output,'w')
    #'AMD_curated_genes_f.csv'
    #pandas is good at writing and reading excel files
    import pandas as pd
    df = pd.read_csv(file_input)
    
    #Alternate notation: gene = AMD['Genes']
    gene = df.Genes
    
    #Create new list
    gene_list = []
    
    #Compare:
    for i in gene:
        if i not in gene_list:
            gene_list.append(i)
    
    for i in gene_list:
        file_out.write(i + '\n')
    
    file_out.close()
    
    return gene_list

print(uniquelist('/Users/simmonsma3/Documents/Alzheimers_and_AMD','AMD_curated_genes.csv', 'AMD_SNP_counts.csv'))