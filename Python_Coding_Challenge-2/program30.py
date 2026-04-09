# Input string
s = input()

# Use set to store duplicates
dup = set()

# Find duplicates
for i in s:
    if s.count(i) > 1:
        dup.add(i)

# Print duplicates
print(" ".join(dup))
