# eda-madagaskar

Overview

This project analyzes 40 years (1984–2024) of climate data in Madagascar to assess thermodynamic and hydrological trends in the tropical rainforest. It focuses on temperature changes, hydroclimatic variability, cyclone-season winds, and vegetation response.

Features

Analysis of temperature trends and asymmetry between day and night.

Evaluation of hydroclimatic indicators: precipitation, evaporation, and consecutive dry days.

Investigation of cyclone-season wind patterns and their correlation with climate variables.

Assessment of vegetation response using Leaf Area Index (LAI).

Identification of potential machine learning targets for predicting ecological and climatic changes.

Data

Source: ERA5 reanalysis dataset
 (1940–present)

Variables include:

2 m air temperature, skin temperature

10 m wind components

Precipitation, evaporation, soil moisture and temperature

Surface solar radiation, cloud cover

Leaf Area Index (LAI) for high and low vegetation

Methodology

Daily data at 00:00 and 12:00 UTC extracted for Madagascar rainforest.

Spatial aggregation performed to obtain a central representative point (-15.75°S, 50.0°E).

Statistical analysis includes trend detection, correlation analysis, and visualization of seasonal and interannual variability.

Potential ML Targets

High-canopy LAI for vegetation health

2 m air temperature and skin temperature trends

Hydroclimatic indicators: precipitation totals, rainfall-to-evaporation ratio, consecutive dry days

Extreme event classification (e.g., high wind speeds during cyclone season)

References

Madagascar Climate Overview

Hydrological Study – Madagascar

Wikipedia – Madagascar Climate
