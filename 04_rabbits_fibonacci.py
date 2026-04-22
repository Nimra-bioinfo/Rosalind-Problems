# Rosalind Problem: Rabbits and Recurrence Relations (FIB)
# Goal: Calculate the total number of rabbit pairs after n months with k offspring per litter.
# Concept: This is a variation of the Fibonacci sequence using Dynamic Programming

n = 34
k = 4

# Initializing first two months
mature_rabbits = 1 
total_rabbits = 1   

# Loop starts from month 3 to n
for _ in range(n - 2):
    # Calculate new babies from mature pairs
    new_babies = mature_rabbits * k
    
    # Calculate total for the current month
    next_month_total = total_rabbits + new_babies
    
    # Update for the next iteration
    mature_rabbits = total_rabbits
    total_rabbits = next_month_total

print(total_rabbits)
