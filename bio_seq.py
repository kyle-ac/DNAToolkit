from bio_structs import *
import random

class bio_seq:
    """DNA sequence class. Default value: ATCG, DNA, No Label"""

    def __init__ (self, seq = "ATCG", seq_type= "DNA", label = "No Label"):
        """Sequence Initialization, validation"""
        self.seq = seq.upper()
        self.label = label 
        self.seq_type =seq_type
        self.is_valid = self.__validateSeq()
        assert self.is_valid,(f"provded data does not seem to be correct {self.seq_type} sequence")

    # DNA Toolkit Fucntions: 
    def __validateSeq(self):
        """ Check the Sequence to make sure  it is a DNA String """
        return set (DNA_Nucleotides).issuperset(self.seq)
    
    
    def get_seq_biotype (self): 
        """Returns sequence type"""
        return self.seq_type
    
    def get_seq_info(self):
        """Returns 4 strings. Full sequence information"""
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"
    
    def generate_rnd_seq (self, length = 10, seq_type ="DNA"):
        """Generate a random DNA sequence with given legnth for testing"""
        seq = ''.join([random.choice(DNA_Nucleotides)
                       for x in range (length)])
        self.__init__(seq, seq_type, "Randomly Generated Sequence")