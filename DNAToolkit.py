# DNA Toolkit file 
import collections
from Sequences import  *

# Check the Sequence to make sure  it is a DNA String 
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq: 
        if nuc not in Nucleotides:
            return False 
    return tmpseq

# Count the frequnecy of each nucleotide in a string 
def countNucFrequency (seq):
    tmpFreqDict = {"A": 0, "C": 0, "T": 0, "G": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict 
    # return dict(collections.Counter(seq))


def transcription(seq):
    """Take the coding strand and change it to mRNA """
    """DNA -> RNA Transcription -> Replacing thymine with uracil """
    return seq.replace( "T", "U")  


def reverse_complement(seq):
    """Swapping Bases using Watson-Crick Base Pairing"""
    # Not very pythonic, a very generic approach we can use 
    # regardless of language 
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::1]
    # Pythonic approach: a faster, more elegant solution 
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def gc_content (seq): 
    
    """Calculating the GC content in a DNA/RNA sequence as a percentage """
    return round ((seq.count('C') + seq.count('G'))/len(seq)* 100)

def gc_content_subsec(seq, k=20):
    """GC content in a DNA/RNA sub-sequences with length k, k=20 by deafault"""
    res = []
    for i in range (0, len(seq)-k + 1, k ):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res