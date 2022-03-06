#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as n


def remove_newlines(lines):
    lines_proc = []
    indices_chrom = []
    for i, l in enumerate(lines):
        if not l.startswith('>'):
            lines_proc.append(l[:-1])
        else:
            lines_proc.append(l)
            indices_chrom.append(i)
            
    return lines_proc, indices_chrom


def get_chrom_files(lines, indices_chrom, num):
    start_index = indices_chrom[num]+1
    if num != 21:
        end_index = indices_chrom[num+1]
    else:
        end_index = len(lines)
        
    genome = lines[start_index:end_index]
    chrom = lines[indices_chrom[num]]
    
    return chrom, genome


def process_fasta_file(file_path):
    
    print('Reading the FASTA file...')
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    print('Preprocessing the file...')
    newlines, indices = remove_newlines(lines)
    whole_genome = ''
    print('Combining the whole genome...')
    for i in range(0, 22):
        chrom, genome_list = get_chrom_files(newlines, indices, i)
        #print(chrom)
        g = ''.join(genome_list)
        whole_genome = whole_genome + g
    print('DONE.')
    
    return whole_genome.upper()

