# Input list
lst = list(map(int, input().split()))

# Assume first element is max
m = lst[0]

# Find max manually
for i in lst:
    if i > m:
        m = i

print(m)
