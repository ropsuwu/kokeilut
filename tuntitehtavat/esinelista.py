esineet = set()

while True:
    esine = input("Anna esine (tyhjä lopettaa): ")
    if not esine:
        break
    if esine in esineet:
        print("Löytyy jo esine")
    else:
        esineet.add(esine)

print(f"Kaikkia esineet: {esineet}")
for n in esineet:
    print(n)