# Take age input
age = int(input())

# Check age category
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")
