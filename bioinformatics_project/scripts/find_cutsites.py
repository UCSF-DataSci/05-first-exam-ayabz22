import re
import argparse

#read the FASTA file and save the DNA sequence to a variable omitting whitespace
def read_fasta(file):
    with open(file, 'r') as f:
        sequence = []
        for line in f: 
            if not line.startswith(">"):
                sequence += line.replace('\n', '')
    return ''.join(sequence)

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

#accepts two arguments, the FASTA file and a cut site sequence
if __name__ == "__main__":
     parser = argparse.ArgumentParser()
     parser.add_argument("fasta_file", type=str, help="Path to the FASTA file")
     parser.add_argument("cut_site_sequence", type=str, help="Cut site sequence")
     args = parser.parse_args()

     dna_sequence = read_fasta(args.fasta_file)

     cut_site_positions = cut_sites(dna_sequence, args.cut_site_sequence)

     cutsite_pairs = find_cutsite_pairs(cut_site_positions)
     
     print(f'Analyzing cut site: {args.cut_site_sequence}')
     print(f'Total cut sites found: {len(cut_site_positions)}')
     print(f'Cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}')
     print('First 5 pairs:')
     for i in range(min(5, len(cutsite_pairs))):
        start, end = cutsite_pairs[i]
        print(f'{i + 1}. {start} - {end}')
     output_path = '../results/cutsite_summary.txt'
     with open(output_path, 'w') as file:
        file.write(f"Analyzing cut site: {args.cut_site_sequence}\n")
        file.write(f"Total cut sites found: {len(cut_site_positions)}\n")
        file.write(f"Cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}\n")
        file.write(f"First 5 pairs:\n")
        for i in range(min(5, len(cutsite_pairs))):
            start, end = cutsite_pairs[i]
            file.write(f"{i + 1}. {start} - {end}\n")
     print(f"Results saved to {output_path}")


        