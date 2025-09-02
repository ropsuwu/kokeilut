gal = float(input("Enter a volume in American gallons (negative value to quit): "))


def gallons_to_liters(gal):
    bensa = gal * 3.785
    return bensa


while True:
    if gal >= 0:
        gallons_to_liters(gal)
        print(f"{gal} American gallons is {gallons_to_liters(gal):.2f} liters.")
        gal = float(input("Enter a volume in American gallons (negative value to quit): "))
    else:
        print("Program finished.")
        break

