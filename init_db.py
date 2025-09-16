import pandas as pd
import random
import math

# Nombre de sites à générer
N = 10

def decimal_to_degmin(value, is_lat=True):
    """Convertit une coordonnée décimale en degrés minutes (WGS84)."""
    degrees = int(abs(value))
    minutes = (abs(value) - degrees) * 60
    direction = ""
    if is_lat:
        direction = "N" if value >= 0 else "S"
    else:
        direction = "E" if value >= 0 else "W"
    return f"{degrees}°{minutes:.2f}'{direction}"

# Génération de données factices
site_ids = [f"S{i+1}" for i in range(N)]
lats = [round(random.uniform(41.0, 51.0), 6) for _ in range(N)]   # France approx
longs = [round(random.uniform(-5.0, 9.0), 6) for _ in range(N)]  # France approx
villes = [random.choice(["Paris", "Lyon", "Marseille", "Toulouse", "Lille", "Bordeaux", "Nantes", "Strasbourg"]) for _ in range(N)]

latitudes = []
longitudes = []
formats = []

for lat, lon in zip(lats, longs):
    if random.random() < 0.5:  # 50% en décimal
        latitudes.append(lat)
        longitudes.append(lon)
        formats.append("decimal")
    else:  # 50% en degrés minutes
        latitudes.append(decimal_to_degmin(lat, is_lat=True))
        longitudes.append(decimal_to_degmin(lon, is_lat=False))
        formats.append("deg_min")

# Création DataFrame
df = pd.DataFrame({
    "site_id": site_ids,
    "latitude": latitudes,
    "longitude": longitudes,
    "ville": villes,
    "format": formats
})

# Sauvegarde dans un CSV
df.to_csv("./data/sites.csv", index=False)

print("✅ Fichier 'sites.csv' généré avec", N, "sites.")
