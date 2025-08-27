Lukulista=[]
while True:
    try:
        luku = int(input("Enter a number (or press Enter to quit): "))
        Lukulista.append(luku)
    except ValueError:
        break
print(f"Smallest number: {min(Lukulista)}")
print(f"Largerst number: {max(Lukulista)}")
