names = set()

while True:
    name = input("Give name (or press Enter to stop): ")
    if not name:
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("All names:")
for n in names:
    print(n)
