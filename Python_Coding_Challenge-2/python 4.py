# Take username and password
user = input()
pwd = input()

# Verify credentials
if user == "admin" and pwd == "1234":
    print("Login Successful")
else:
    print("Invalid")
