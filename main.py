# DNA Toolset/Code testing file 
from DNAToolkit import *
from Utilities import coloured
import random


# Creating a random DNA sequence for testing
rndDNAStr =  ''.join([random.choice(Nucleotides)
                        for nuc in range (50)]) 

DNAStr = validateSeq(rndDNAStr)

print(f'\n Sequence: {coloured(DNAStr)}\n')
print(f'[1] Sequence Length: {len(DNAStr)}\n')
print(coloured(f'[2] Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

print(f'[3] DNA/RNA Transcription: {transcription(DNAStr)}\n')

# Printing DNA Pattern 5'->3' with reverse complement
print(f"[4] DNA String + Complement + Reverse Complement:\n5'{coloured(DNAStr)} 3'")
print (f"   {''.join(['|' for c in range (len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")