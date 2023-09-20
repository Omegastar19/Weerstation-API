import requests
import datetime
import csv
import os

def plaatsnamen(csv_file):
    # zet het plaatsnamen-bestand om in een lijst
    place_names = []
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            place_names.extend(row)
    # zet plaatsnamen om tot kleine letters
    place_names = [name.lower() for name in place_names]
    return place_names

def weer_api(api_key, location):
    # haalt weergegevens op via de api van weerlive.nl

    api_bron = "https://weerlive.nl/api/json-data-10min.php"
    parameters = {
        "key": api_key,
        "locatie": location
    }

    response = requests.get(api_bron, params=parameters)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Er is iets fout gegaan. Status code: {response.status_code}")
        return None

    # De specifieke weergegevens die opgehaald kunnen worden:

def gevoelstemperatuur(weather_data):
    return weather_data['liveweer'][0].get('gtemp', 'n/a')

def windsnelheid(weather_data):
    return weather_data['liveweer'][0].get('windkmh', 'n/a')

def luchtdruk(weather_data):
    return weather_data['liveweer'][0].get('luchtd', 'n/a')

def luchtvochtigheid(weather_data):
    return weather_data['liveweer'][0].get('lv', 'n/a')

def weergesteldheid(weather_data):
    return weather_data['liveweer'][0].get('samenv', 'n/a')

def create_document(location, weather_data):
    # Maakt een document waarin alle weergegevens worden gestopt
    # Document wordt in sub-folder geplaatst
    sub_directory = 'weerberichten'
    # Document bevat ook datum en tijd waarop de gegevens opgehaald zijn
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{location.capitalize()}_{current_datetime}.txt"
    file_path = os.path.join(sub_directory, filename)

    # inhoud van het document
    inhoud_weergegevens = (
        f"Weather in {location}:\n"
        f"Temperatuur: {weather_data['liveweer'][0].get('temp', 'n/a')}°C\n"
        f"Gevoelstemperatuur: {gevoelstemperatuur(weather_data)}°C\n"
        f"Windsnelheid: {windsnelheid(weather_data)} km/h\n"
        f"Luchtdruk: {luchtdruk(weather_data)} hectopascal\n"
        f"Luchtvochtigheid: {luchtvochtigheid(weather_data)} procent\n"
        f"Weergesteldheid: {weergesteldheid(weather_data)}"
    )

    # Document opslaan
    with open(file_path, "w") as f:
        f.write(inhoud_weergegevens)
        print(f"Weergegevens opgeslagen in {filename}")

def main():
    # variabelen
    api_key = "4d2b635f23"
    csv_file = 'Plaatsnamen.csv'
    place_names = plaatsnamen(csv_file)

    # input
    location = input("Voor welke plaats in Nederland zoek je weergegevens?: ").lower()

    # Kijk of de ingevoerde plaatsnaam op de lijst staat
    if location not in place_names:
        print(f"Error: '{location}' is niet een geldige Nederlandse plaatsnaam.")
        return

    # Main loop
    weather_data = weer_api(api_key, location)

    # Print de weergegevens en maakt een document waarin de weergegevens opgeslagen worden
    if weather_data:
        print(f"Weer in {location.capitalize()}:")
        print(f"Temperatuur: {weather_data['liveweer'][0]['temp']}°C")
        print(f"Gevoelstemperatuur: {gevoelstemperatuur(weather_data)}°C")
        print(f"Windsnelheid: {windsnelheid(weather_data)} km/h")
        print(f"Luchtdruk: {luchtdruk(weather_data)} hectopascal")
        print(f"Luchtvochtigheid: {luchtvochtigheid(weather_data)} procent")
        print(f"Weergesteldheid: {weergesteldheid(weather_data)}")

        create_document(location, weather_data)

while True:
    # Programma herhalen of niet

    main()

    nogmaals = input("Type [Enter] om door te gaan, of type [0] om te stoppen.\n")
    if nogmaals == "0":
        break