"""
Bioinformatics Script: Sequence Comparison (Hamming vs Levenshtein)
Author: Nimra
Description: 
1. Hamming Distance: For equal length sequences (Substitutions only).
2. Levenshtein Distance: For unequal lengths (Substitutions, Insertions, Deletions).
"""

def calculate_hamming_distance(s, t):
    """Calculates point mutations for equal length strings."""
    if len(s) != len(t):
        raise ValueError("Hamming distance requires strings of equal length.")
    return sum(1 for char1, char2 in zip(s, t) if char1 != char2)

def calculate_levenshtein_distance(s, t):
    """
    Calculates the minimum edit distance using Dynamic Programming.
    This accounts for gaps (indels) in DNA sequences.
    """
    if len(s) < len(t):
        return calculate_levenshtein_distance(t, s)
    if len(t) == 0:
        return len(s)

    previous_row = range(len(t) + 1)
    for i, char1 in enumerate(s):
        current_row = [i + 1]
        for j, char2 in enumerate(t):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (char1 != char2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

if __name__ == "__main__":
    # Test Case 1: Equal Length (Rosalind Style)
    seq_a = "GAGCCTACTAACGGGAT"
    seq_b = "CATCGTAATGACGGCCT"
    
    # Test Case 2: Unequal Length (Real-world Scenario)
    seq_c = "GATTACA"
    seq_d = "GATACA" # One 'T' is deleted
    
    print(f"--- Hamming Distance (Equal Length) ---")
    print(f"Distance: {calculate_hamming_distance(seq_a, seq_b)}")
    
    print(f"\n--- Levenshtein Distance (Unequal Length) ---")
    print(f"Comparing '{seq_c}' and '{seq_d}':")
    print(f"Edit Distance: {calculate_levenshtein_distance(seq_c, seq_d)}")
