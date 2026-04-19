# Rosalind Problem: Counting DNA Nucleotides
# Learning: I learned how to use the .count() method in Python to find the frequency of specific characters.
# I also practiced using the input() function to make the script interactive for any DNA sequence.
dna = input("Enter DNA sequence: ")
a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')
print(f"{a} {c} {g} {t}")
