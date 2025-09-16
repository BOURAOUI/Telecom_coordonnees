import logging
import os
import pandas as pd

import duckdb

# vérifier si le fichier sites existe ou pas
if "sites.csv" not in os.listdir("/Users/mohamedabbesbouraoui/PycharmProjects/Telecom_geo/Telecom_coordonnees/data"):
    logging.error("There is no data")

#lecture du fichier csv
sites_df = pd.read_csv("/data/sites.csv")

print(type(sites_df))




