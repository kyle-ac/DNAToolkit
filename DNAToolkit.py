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

# Take the coding strand and change it to mRNA 
def transcription(seq):
    """DNA -> RNA Transcription -> Replacing thymine with uracil """
    return seq.replace( "T", "U")  

"""Swapping Bases using Watson-Crick Base Pairing"""
def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::1]
