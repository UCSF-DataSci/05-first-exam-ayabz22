import random 

def generate_random_dna(length):
    dna = [] #we have our empty list 
    for _ in range(length):
        bases = random.choice('ACGT') #chooses a letter randomly
        dna.append(bases) #add it to our empty list
    return ''.join(dna) #then add " " so that theres no space so instead of A C G T it would be ACGT


def save_fasta(filename, chain):
    with open(filename, 'w') as file:
        for i in range(0, len(chain), 80):
            file.write(chain[i:i+80] + '\n') #use file.write to the write to a file, since we need to do slicing use the [:] 

#now use the functions we made to finish the assignment 
random_dna = generate_random_dna(1000000)
save_fasta("bioinformatics_project/data/random_sequence.fasta", random_dna)
print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")


