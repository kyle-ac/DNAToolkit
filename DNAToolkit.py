# DNA Toolkit file 
from collections import Counter
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

def translate_seq(seq, init_pos = 0):
    """Tranlsates a DNA sequence into its Amino acid sequence"""
    return [DNA_Codons [seq[pos:pos + 3]] for pos in range (init_pos, len(seq) - 2, 3)] 

def codon_usage (seq, AminoAcid):
    """Provides the frequency of each codon encoding a given amino acid in a DNA sequence"""
    tmpList= []
    for i in range (0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]] == AminoAcid: 
            tmpList.append(seq[i:i+3])

    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round (freqDict[seq]/totalWeight, 2)
    return freqDict

def gen_reading_frames(seq):
    """Generate the six reading frames of a DNA sequences, including the reverse complement"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames. append(translate_seq(reverse_complement(seq), 0))
    frames. append(translate_seq(reverse_complement(seq), 1))
    frames. append(translate_seq(reverse_complement(seq), 2))

    return frames 

def proteins_from_rf (aa_seq):
    """Compute all possible proteins in an amino acid seq and return a list of possible proteins"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            #STOP adding AA if stop codon is read 
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else: 
            # Start adding AA if M - Start Codon is read 
            if aa == "M":
                current_prot.append("")
            for i in range (len(current_prot)):
                current_prot[i] += aa
    return proteins
        
def all_proteins_from_orfs (seq, startReadPos=0, endReadPos = 0, ordered = False):
    """Compute all possible proteins from all open reading frames """
    """Protein search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2  """
    """API can be used to pull protein info """
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startRead: endRead])
    else:
        rfs = gen_reading_frames(seq)

    res =[]    
    for rf in rfs: 
        prots = proteins_from_rf(rf)
        for p in prots:
            res.append(p)

    if ordered: 
        return sorted(res, key=len, reverse = True )
    return res 