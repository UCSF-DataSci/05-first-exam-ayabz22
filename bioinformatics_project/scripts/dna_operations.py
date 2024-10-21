import sys 

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
    return [:: -1] #learned in this class all u have to do is this to reverse 
