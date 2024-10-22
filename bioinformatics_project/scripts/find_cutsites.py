import re

#read the FASTA file and save the DNA sequence to a variable omitting whitespace
def read_fasta(file):
    with open(file, 'r') as f:
        sequence = []
        for line in f: 
            if not line.startswith(">"):
                sequence += line.replace('\n', '')
    return sequence 

#Find all occurrences of the cut site (specified below) in the DNA sequence.
def cut_sites(dna_sequence, cut_site):
    clean_cutsite = cut_site.replace('|', '')
    cutsite_positions = []
    for match in re.finditer(re.escape(clean_cutsite), dna_sequence):
        cutsite_positions.append(match.start())
    return cutsite_positions

#Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
def find_cutsite_pairs(positions):
    pairs = []
    upper_base = 120000
    lower_base = 80000
    for i in range(len(positions)):
        for a in range(i + 1, len(positions)):
            distance = positions[a] - positions[i]
            if lower_base <= distance <= upper_base:
                pairs.append((positions[i], positions[a]))
    return pairs 


        