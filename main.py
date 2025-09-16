import logging
import os
import pandas as pd


# vérifier si le fichier sites existe ou pas
if not os.path.exists("data/sites.csv"):
    logging.error("There is no data")

#lecture du fichier csv
sites_df = pd.read_csv("data/sites.csv")

#Convertir les latitudes
def lat_degmin_to_decimal(coord: str) -> float:
    """
    """
    try:
        deg_part, rest = coord.split("°")
        min_part, direction = rest.split("'")
    except ValueError:
        raise ValueError("Format attendu: ex '48°51.40'N' ou '34°36.22'S'")

    degrees = float(deg_part)
    minutes = float(min_part)

    decimal = degrees + minutes / 60

    # Latitude Sud doit être négative
    if direction.strip().upper() == "S":
        decimal = -decimal

    return decimal


#Convertir les longitudes
def lon_degmin_to_decimal(coord: str) -> float:
    """
    """
    try:
        deg_part, rest = coord.split("°")
        min_part, direction = rest.split("'")
    except ValueError:
        raise ValueError("Format attendu: ex '2°21.13'E' ou '58°22.90'W'")

    degrees = float(deg_part)
    minutes = float(min_part)

    decimal = degrees + minutes / 60

    # Longitude Ouest doit être négative
    if direction.strip().upper() == "W":
        decimal = -decimal

    return decimal


for lat in sites_df["latitude"]:
    if "°" not in str(lat):
        if (lat >= 41.3) & (lat <= 51.1):
            lat_degmin_to_decimal(str(lat))
        else:
            print("Latitude pas en France")

for lon in sites_df["longitude"]:
    if "°" not in str(lon):
        if (lon >= -5.1) & (lon <= 9.6):
            lon_degmin_to_decimal(str(lon))
        else:
            print("Longitude pas en France")




