# Input list
lst = list(map(int, input().split()))

# Calculate expected sum
n = len(lst) + 1
total = n * (n + 1) // 2

# Find missing number
print(total - sum(lst))
