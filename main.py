# DNA Toolset/Code testing file 
from DNAToolkit import *
from Utilities import coloured
import random


# Creating a random DNA sequence for testing
rndDNAStr =  ''.join([random.choice(Nucleotides)
                        for nuc in range (50)]) 

DNAStr = validateSeq(rndDNAStr)

# print(f'\n Sequence: {coloured(DNAStr)}\n')
# print(f'[1] Sequence Length: {len(DNAStr)}\n')
# print(f'[2] Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')

# # print(f'[3] DNA/RNA Transcription: {transcription(DNAStr)}\n')

# # # Printing DNA Pattern 5'->3' with reverse complement
# print(f"[4] DNA String + Complement + Reverse Complement:\n5'{coloured(DNAStr)} 3'")
# print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
# print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")

# # # Analysing the Sequence 
# print(f'[5] GC Content: {gc_content(DNAStr)}%\n')
# print(f'[6] GC Content in Subsection k = 5: {gc_content_subsec(DNAStr, k = 5)}\n')
# print(f'[7] Amino Acid Sequence: {translate_seq(DNAStr, 0)}\n')
# print(f'[8] Codon Freqency (L): {codon_usage(DNAStr, "L")}\n')

# # # Finding proteins by reading frames
# print('[9] Reading Frames: ')
# for frame in gen_reading_frames(DNAStr): 
#     print (frame)

# Protein search within reading frames 
print('\n[10] All proteins in 6 ORFs: ')
for prot in all_proteins_from_orfs(NM_000207_3, 0, 0, True ):
    print(f'{prot}')