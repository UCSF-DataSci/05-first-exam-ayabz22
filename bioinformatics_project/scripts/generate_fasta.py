import random 

def generate_random_dna(length):
    dna = [] #we have our empty list 
    for _ in range(length):
        bases = random.choice('ACGT') #chooses a letter randomly
        dna.append(bases) #add it to our empty list
    return ''.join(dna) #then add " " so that theres no space so instead of A C G T it would be ACGT


