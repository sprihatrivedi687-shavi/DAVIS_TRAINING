# Input number
n = input()

# Check palindrome
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
