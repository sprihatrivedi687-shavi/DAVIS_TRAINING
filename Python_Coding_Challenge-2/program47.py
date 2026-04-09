# Function to return even numbers
def even(lst):
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i)
    return result

# Example
print(even([1,2,3,4]))
