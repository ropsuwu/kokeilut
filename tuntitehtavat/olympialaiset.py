vuosi = int(input("Anna vuosi: "))
if vuosi == 2020 or vuosi == 1916 or vuosi == 1940 or vuosi == 1944:
    print("Ei ollut olympiavuosi.")
elif vuosi == 2021:
    print("On olympiavuosi.")
elif vuosi % 4 == 0:
    print("On olympiavuosi.")
else:
    print("Ei ollut olympiavuosi.")