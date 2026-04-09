# Given dictionary
d = {"A":80, "B":95, "C":78}

# Find key with max value
max_student = max(d, key=d.get)

print(max_student)
