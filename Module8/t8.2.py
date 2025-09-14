import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='roope',
    password='nakki',
    autocommit=True
)


def get_airports_by_country(country_code):
    kursori = yhteys.cursor()
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s group by type order by type";
    kursori.execute (sql, (country_code,))
    tulos = kursori.fetchall()
    return tulos


def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    tulos = get_airports_by_country(country_code)
    if tulos:
        print("")
        print("")
        print(f"Airports in {country_code}:")
        for tyyppi, maara in tulos:
            print(f"{maara} {tyyppi} airports")
    else:
        print(f"No airports found for country code '{country_code}' or database connection failed.")

run_country_program()
