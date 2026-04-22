# Rosalind Problem: Complementing a Strand of DNA
# Learning: I learned how to use string slicing [::-1] to reverse a string 
# and the .replace() method or a translation table to find DNA complements.

dna = input("Enter DNA sequence: ")

# Step 1: Reverse the DNA string
reversed_dna = dna[::-1]

# Step 2: Replace each nucleotide with its complement
mapping = str.maketrans("ATCG", "TAGC")
reverse_complement = reversed_dna.translate(mapping)

print(reverse_complement)
