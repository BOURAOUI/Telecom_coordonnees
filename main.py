import logging
import os
import pandas as pd
import duckdb
import folium
import simplekml


# vérifier si le fichier sites existe ou pas
if not os.path.exists("data/sites.csv"):
    logging.error("There is no data")

# lecture du fichier csv
sites_df = pd.read_csv("data/sites.csv")


# Fonction de nettoyage simple pour coordonnées ---
def to_decimal(coord):
    """
    Convertit une coordonnée:
    - Si c'est déjà un nombre -> float
    - Si c'est un string style "48°51.40'N" -> convertit en décimal
    """
    try:
        # Cas déjà en décimal
        return float(coord)
    except:
        # Cas degrés/minutes (format: 48°51.40'N)
        deg, rest = coord.split("°")
        minutes, direction = rest.split("'")
        decimal = float(deg) + float(minutes) / 60
        if direction in ["S", "W"]:
            decimal = -decimal
        return decimal


# Appliquer aux colonnes latitude/longitude ---
sites_df["latitude"] = sites_df["latitude"].apply(to_decimal)
sites_df["longitude"] = sites_df["longitude"].apply(to_decimal)

# Sauvegarder dans DuckDB ---
con = duckdb.connect("data/sites.duckdb")
con.execute("CREATE OR REPLACE TABLE sites AS SELECT * FROM sites_df")
con.close()


# Créer une carte centrée sur le centre de la France
m = folium.Map(location=[46.6, 2.5], zoom_start=6)

# Ajouter des marqueurs
for lat, long, site in zip(
    sites_df["latitude"], sites_df["longitude"], sites_df["site_id"]
):
    folium.Marker(
        [lat, long], popup=f"Site ID : {site}", tooltip=f"Site {site}"
    ).add_to(m)

# Sauvegarde
m.save("output/sites_map.html")


# Créer un objet KML
kml = simplekml.Kml()

# Ajouter un point (latitude, longitude)
for lat, long, site in zip(
    sites_df["latitude"], sites_df["longitude"], sites_df["site_id"]
):
    kml.newpoint(name=f"Site {site}", coords=[(lat, long)])

# Sauvegarder dans un fichier .kml
kml.save("output/sites.kml")