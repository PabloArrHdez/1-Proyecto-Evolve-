import requests 
import pandas as pd
from datetime import datetime
import os


def extraccion_API(cities_of_interest):
    url = "https://api.citybik.es/v2/networks"
    response = requests.get(url)
    cities_of_interest = [
    "Madrid", "Barcelona", "Paris", "Berlin", "Amsterdam", 
    "Bruxelles", "Lisbon", "Vienna", "Warsaw", 
    "Budapest", "Stockholm", "Helsinki", "Oslo", "London", "Prague", "Dublin", "Zurich", 
    "Munich"
]
    if response.status_code == 200:
        networks = response.json().get("networks", [])
        bike_data = []
        extraction_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        for network in networks:
            city = network.get("location", {}).get("city")
            if city in cities_of_interest:
                stations_url = f"https://api.citybik.es/v2/networks/{network['id']}"
                stations_response = requests.get(stations_url)
                if stations_response.status_code == 200:
                    stations = stations_response.json().get("network", {}).get("stations", [])
                    for station in stations:
                        bike_data.append([
                            network["name"], network["id"], city, network["location"]["country"],
                            station.get("free_bikes", 0), station.get("empty_slots", 0), 
                            station.get("latitude"), station.get("longitude"), extraction_date 
                        ])
    df = pd.DataFrame(bike_data, columns=["name", "id", "city", "country", "free_bikes", "empty_slots", "latitude", "longitude", "extraction_date"])
    df.to_csv("Datos/bici_publicas_oficial_sucio.csv", mode="a", header=not os.path.isfile("bici_publicas_oficial_sucio.csv"), index=False)