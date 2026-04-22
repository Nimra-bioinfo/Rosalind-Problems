# Rosalind Problem: Transcribing DNA into RNA
# Learning: I learned how to use the .replace() method in Python to perform 
# string substitution, converting Thymine (T) to Uracil (U).

dna = input("Enter DNA sequence: ")

# Transcription: replace all 'T' nucleotides with 'U'
rna = dna.replace('T', 'U')

print(rna)
