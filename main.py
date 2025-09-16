import logging
import os
import pandas as pd

import duckdb

# vérifier si le fichier sites existe ou pas
if "/data/sites.csv" not in os.listdir("data"):
    logging.error("There is no data")

#lecture du fichier csv
sites_df = pd.read_csv("/data/sites.csv")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#   print_hi('PyCharm')

