import logging
import os
import pandas as pd
import duckdb


# vérifier si le fichier sites existe ou pas
if not os.path.exists("data/sites.csv"):
    logging.error("There is no data")

#lecture du fichier csv
sites_df = pd.read_csv("data/sites.csv")

# --- 2. Fonction de nettoyage simple pour coordonnées ---
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

# --- 3. Appliquer aux colonnes latitude/longitude ---
sites_df["latitude"] = sites_df["latitude"].apply(to_decimal)
sites_df["longitude"] = sites_df["longitude"].apply(to_decimal)

# --- 4. Sauvegarder dans DuckDB ---
con = duckdb.connect("data/sites.duckdb")
con.execute("CREATE OR REPLACE TABLE sites AS SELECT * FROM sites_df")
con.close()