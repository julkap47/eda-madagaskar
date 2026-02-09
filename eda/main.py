from src import data_reader as dr
from src import preprocessing as pr
import pandas as pd
import os

files = [

    'dane_madagaskar/data1984-1991.grib',
    'dane_madagaskar/data1992-2002.grib',
    'dane_madagaskar/data2002-2013.grib',
    'dane_madagaskar/data2014-2024.grib'
]

output_path = "output/era5_full_timeseries.csv"

# Only proceed if the file DOES NOT exist
if not os.path.isfile(output_path):
    print(f"File {output_path} not found. Starting data processing...")
    
    data = dr.load_era5_gribs(files)
    data.reset_index().to_csv(output_path, index=False)
    
    print(f"Process complete. Rows: {len(data)}")
else:
    print(f"File {output_path} already exists. Skipping processing.")
    data = pd.read_csv(output_path)


data = pr.mean_and_cleaning(data, "output/era5_clean_timeseries.csv")
