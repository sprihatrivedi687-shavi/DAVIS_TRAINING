# Input list
lst = list(map(int, input().split()))

# Remove duplicates
lst = list(set(lst))

# Sort list
lst.sort()

# Print second largest
print(lst[-2])
