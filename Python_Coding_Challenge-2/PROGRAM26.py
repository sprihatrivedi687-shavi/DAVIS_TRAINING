# Input sentence
s = input().split()

# Assume first word is longest
longest = s[0]

# Find longest word
for word in s:
    if len(word) > len(longest):
        longest = word

print(longest)
