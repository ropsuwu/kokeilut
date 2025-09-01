numlist = []
while True:
    try:
        luku = float(input("Enter a number: "))
        numlist.append(luku)
    except ValueError:
        break
numlist.sort(reverse=True)
print("The greatest numbers in descending order: ")
for i in range(0, len(numlist[0:5])):
    print(numlist[i])