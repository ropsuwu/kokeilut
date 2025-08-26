nimi = input("Anna hahmosi nimi: ")
print(f"Hei {nimi} onpa hieno nimi. Haluatko turpaan vai nuolen?")
tulos = input("Turpaan vai nuolen? ")
if tulos.lower() == "turpaan":
    print("Kuolit! Hävisit pelin.")
elif tulos.lower() == "nuolen":
    print("Sait koiran nimeltä Nuoli!")
