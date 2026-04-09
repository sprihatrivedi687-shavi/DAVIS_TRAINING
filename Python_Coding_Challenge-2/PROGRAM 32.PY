# Input two lists
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# Find intersection
print(list(a & b))
