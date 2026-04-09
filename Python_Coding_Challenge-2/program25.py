# Input string
s = input()

# Convert manually
res = ""
for i in s:
    res += chr(ord(i) - 32)  # ASCII conversion

print(res)
