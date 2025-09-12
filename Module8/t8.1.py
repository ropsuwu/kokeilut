import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='roope',
    password='nakki',
    autocommit=True
)


def hae_lentokentat(koodi):
    kursori = yhteys.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    if tulos:
        print(f"Airport name: {tulos[0]}")
        print(f"Location: {tulos[1]}")
    else:
        print("No airport found with that ICAO code.")


koodi = input("Enter the ICAO code of an airport: ")
hae_lentokentat(koodi)
