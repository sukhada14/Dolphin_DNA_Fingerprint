#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
import numpy as np
import re

def remove_newlines(lines):
    lines_proc = []
    indices_scaffold = []
    for i, l in enumerate(lines):
        if not l.startswith('>'):
            lines_proc.append(l[:-1])
        else:
            lines_proc.append(l)
            indices_scaffold.append(i)
            
    return lines_proc, indices_scaffold


def get_scaffold_files(lines):
    
    g = ''.join(lines)
    start = [_.start() for _ in re.finditer('>Q', g)] 
    end = [_.start() for _ in re.finditer('\n', g)] 
    scaffolds = [g[a: b] for a, b in zip(start, end)]
    
    sequences = []
    for i in range(0, len(start)):
        if i <480:
            s = g[end[i]+1 : start[i+1]].upper()
        elif i == 480:
            s = g[end[i]+1:].upper()
        sequences.append(s)
        
    scaffold_sequence_dict = {i:s for i, s in zip(scaffolds, sequences)}
    return scaffold_sequence_dict
    

def process_fasta_file(file_path):
    print('Reading the FASTA file...')
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    print('Preprocessing the file...')
    newlines, indices = remove_newlines(lines)
    
    print('Collecting scaffold genomes')
    scaffold_sequence_dict = get_scaffold_files(newlines)
        
    print('DONE.')

    return scaffold_sequence_dict


# In[53]:


with open('../Data/Donor1/GCA_003314715.1_Tur_tru_Illumina_hap_v1_genomic.fna', 'r') as f:
    lines = f.readlines()


# In[ ]:




