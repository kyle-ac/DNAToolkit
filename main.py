# DNA Toolset/ testing file 

from bio_seq import bio_seq

test_DNA = bio_seq("ATCGGTTTG", "DNA", "Test Label")

print(test_DNA.get_seq_info())
print(test_DNA.get_seq_biotype())

test_DNA.generate_rnd_seq()
print(test_DNA.get_seq_info())

