# Input string
s = input()

# Initialize result string
res = ""

# Replace vowels
for i in s:
    if i.lower() in "aeiou":
        res += "*"
    else:
        res += i

print(res)
