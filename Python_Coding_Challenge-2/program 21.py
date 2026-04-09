# Input string
s = input()

# Initialize counter
count = 0

# Count vowels
for i in s:
    if i.lower() in "aeiou":
        count += 1

print(count)
