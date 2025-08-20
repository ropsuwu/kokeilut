sukupuoli = (input("Anna sukupuolesi: "))
if sukupuoli == "Mies" or sukupuoli == "mies":
    hgm = (int(input("Mikä on hemoglobiiniarvosi? : ")))
    if (hgm >= 134 and hgm <= 195):
           print ("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi ei ole normaali")
elif sukupuoli == "Nainen" or sukupuoli == "nainen":
    hgn = (int(input("Mikä on hemoglobiiniarvosi? : ")))
    if (hgn >= 117 and hgn <= 175):
           print ("Hemoglobiiniarvosi on normaali.")
    else:
        print ("Hemoglobiniarvosi ei ole normaali")
else: print("Väärä input pelle")