# Input string
s = input()

# Check palindrome
if s == s[::-1]:
    print("Yes")
else:
    print("No")
