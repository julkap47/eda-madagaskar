import cfgrib
import xarray as xr
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def load_era5_gribs(file_paths):
    """
    Loads and organizes ERA5 GRIB files into a unified structure.
    
    Args:
        file_paths (list): List of strings containing paths to .grib files.
        
    Returns:
        pd.DataFrame: A unified, time-sorted DataFrame with all variables.
        
    """
    all_year_frames = []

    for file in file_paths:
        print(f"Reading: {file}")
        datasets = cfgrib.open_datasets(file)
        current_file_frames = []

        for ds in datasets:
            accumulated_vars = ['ssrd', 'e', 'ro', 'tp']
            is_accum_ds = any(var in ds.data_vars for var in accumulated_vars)

            df = ds.to_dataframe().reset_index()
            if is_accum_ds and 'valid_time' in df.columns:
                df['time'] = df['valid_time']

            df = _prepare_coordinate_index(df)
            current_file_frames.append(df)

        file_combined = pd.concat(current_file_frames, axis=1)
        all_year_frames.append(file_combined)

    final_df = pd.concat(all_year_frames, axis=0)
    
    return final_df.sort_index(level='time')

def _prepare_coordinate_index(df):
    """
    Internal helper to clean time, drop metadata, and set the MultiIndex.

    """
    df['time'] = pd.to_datetime(df['time']).dt.round('H')
    
    cols_to_drop = ['number', 'step', 'surface', 'valid_time', 'depthBelowLandLayer']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
    
    df = df.set_index(['time', 'latitude', 'longitude'])
    df = df.sort_index()

    return df[~df.index.duplicated(keep='first')]