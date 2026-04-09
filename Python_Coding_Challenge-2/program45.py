# Input list
lst = list(map(int, input().split()))

# Create frequency dictionary
d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
