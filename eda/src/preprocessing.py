import pandas as pd
import numpy as np

def mean_and_cleaning(df, output_path):

    """
    national average and scientific unit conversions.

    """
    data = df.groupby('time').mean().reset_index()
    # Kelvin to Celsius
    for col in ['t2m', 'skt', 'stl1']:
        if col in df.columns:
            df[col] = df[col] - 273.15

    # Meters to millimeters 
    for col in ['tp', 'e', 'ro']:
        if col in df.columns:
            df[col] = df[col] * 1000

    # Fraction to percentage 
    if 'tcc' in df.columns:
        df['tcc'] = df['tcc']*100
    
    # Calculate wind speed
    if 'u10' in df.columns and 'v10' in df.columns:
        df['ws'] = np.sqrt(df['u10']**2 + df['v10']**2)

    data['time'] = pd.to_datetime(data['time'])
    data.to_csv(output_path, index=False)
    return data

