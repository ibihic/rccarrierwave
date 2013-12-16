def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1)>len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    occurences = 0
    for char in dna:	
    	if char in nucleotide:
    		occurences = occurences + 1
    return occurences


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.count(str(dna2))>0

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if DNA sequence dna contains no other characters
    other than 'A','T','C' and 'G'.

    >>>is_valid_sequence('ATGCATGC')
    True
    >>>is_valid_sequence('ACCacc')
    False
    >>>is_valid_sequence('ACZ123xx')
    False
    >>>is_valid_sequence('')
    True
    # if want is_valid_sequence('')
    # False
    # return count==0 and len(dna)>0
    '''
    count=0
    for char in dna:	
    	if str(char) not in 'ATCG':
    		count+=1
    return count==0

def insert_sequence(dna1, dna2, index_num):
    ''' (str, str, int) -> str

    Return new DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>>insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>>insert_sequence('CCGG', 'AT', 0)
    ATCCGG
    >>>insert_sequence('', 'AT', 100)
    AT
    >>>insert_sequence('CCGG', 'AT', -100)
    ATCCGG    
    '''
    return str(dna1)[:index_num]+str(dna2)+str(dna1)[index_num:]


def get_complement(nucleotide):
    '''(str) -> str

    Return the nucleotide's complement. The complement of 'A' is 'T' and the
    complement of 'C' is 'G', and vice versa.

    >>>get_complement('A')
    'T'
    >>>get_complement('C')
    "G'
    '''
    
    for char in nucleotide:
        if char=='A':
            return 'T'
        elif char=='T':
            return 'A'
        elif char=='C':
            return 'G'        
        elif char=='G':
            return 'C'
        else:
            return 'Not valid nucleotide'
        

def get_complementary_sequence(dna):
    '''(str) -> str

    Return the DNA sequence that is complement to the given DNA sequence. The
    complement of 'A' is 'T' and the complement of 'C' is 'G', and vice versa.

    >>>get_complementary_sequence('ATATGGCC')
    'TATACCGG'
    >>>get_complementary_sequence('CCGGTT')
    "GGCCAA'
    '''

    new_dna_sequence=''
    for char in dna:
        if char not in 'ATCG':
            return 'Not valid DNA sequence'
        elif char=='A':
            new_dna_sequence += 'T'
        elif char=='T':
            new_dna_sequence += 'A'
        elif char=='C':
            new_dna_sequence += 'G'        
        elif char=='G':
            new_dna_sequence += 'C'
    return new_dna_sequence 
    
    
