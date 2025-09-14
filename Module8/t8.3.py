import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='roope',
    password='nakki',
    autocommit=True
)

def get_airport_coordinates(icao_code):
    kursori = yhteys.cursor()
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao_code,))
    return kursori.fetchone()

def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ").upper()
    icao2 = input("Enter the ICAO code of the second airport: ").upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 and coords2:
        dist = distance.distance(coords1, coords2).kilometers
        print(f"Distance between {icao1} and {icao2}: {dist:.2f} kilometers")
    else:
        print("")

run_airport_distance()
