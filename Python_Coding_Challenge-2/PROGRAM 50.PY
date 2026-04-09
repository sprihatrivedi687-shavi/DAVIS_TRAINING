# Function to check prime
def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return "Not Prime"
    
    # Check divisibility
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

# Example
print(is_prime(7))
