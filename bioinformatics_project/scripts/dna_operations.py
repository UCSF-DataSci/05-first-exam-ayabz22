import sys 
import argparse 

#first one is to the complement A to T and C to G 
def complement(sequence):
    dictionary = {'A':'T', 'C':'G', 'T':'A', 'G':'C'} #this is our dictionary of our bases
    complements = [] #our empty list 
    for base in sequence:
        uppercase_base = base.upper() #convert the base to uppercase
        complement_base = dictionary[uppercase_base] #take the uppercase and find it in the dictionary
        complements.append(complement_base) #add it to the complements list 
    return ''.join(complements)

def reverse(sequence):
    return sequence[:: -1] #learned in this class all u have to do is this to reverse 

def reverse_complement(sequence):
    return reverse(complement(sequence))

parser = argparse.ArgumentParser() #from lecture import argparse 
parser.add_argument('sequence', type=str, help='Input sequence')
args = parser.parse_args()
input_seq = args.sequence
print(f"Original sequence: {input_seq}")
print(f"Complement: {complement(input_seq)}")
print(f"Reverse: {reverse(input_seq)}")
print(f"Reverse complement: {reverse_complement(input_seq)}")