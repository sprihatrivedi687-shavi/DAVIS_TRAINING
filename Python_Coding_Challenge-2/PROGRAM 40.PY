# Input list
lst = list(map(int, input().split()))

# Rotate right by one
rotated = [lst[-1]] + lst[:-1]

print(rotated)
