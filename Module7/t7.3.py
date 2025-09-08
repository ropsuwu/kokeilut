airports = {}
print("")
quer = int(input("Airport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): "))
while quer != "":
    if quer == 1:
        icao = input("Enter the ICAO code: ")
        airname = input("Enter the airport name: ")
        airports[icao] = airname
        print(f"Airport {airname} with ICAO code {icao} has been added.\n")
        quer = int(input("Airport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): "))
    elif quer == 2:
        icaosearch = input("Enter the ICAO code: ")
        if icaosearch in airports:
            print(f"The airport with ICAO code {icaosearch} is", airports[icaosearch] +".")
            print("")
        else:
            print(f"No airport found with ICAO code {icaosearch}.")
            print("")
        quer = int(input("Airport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): "))
    else:
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break
