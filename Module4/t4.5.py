ru = "python"
rp = "rules"

u = input("Enter username: ")
pw = input("Enter password: ")
arvaukset = 0

while u != ru and pw != rp:
    arvaukset = arvaukset + 1
    print("Incorrect username or password. Please try again.")
    u = input("Enter username: ")
    pw = input("Enter password: ")
    if arvaukset == 4:
        print("Access denied")
        break
else:
    print("Welcome")