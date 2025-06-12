import pandas as pd
import numpy as np
from pathlib import Path


def load_and_clean_weather_data(path: Path) -> pd.DataFrame:
	df = pd.read_csv(path)

	df['timestamp'] = pd.to_datetime(df['timestamp'], format="%Y%m%dT%H%M")
	df = df.sort_values("timestamp")

	df = df[['timestamp', 'mean_temp']]
	df.columns = ['date', 'temp']

	return df

def add_training_features(df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
	df = df.copy()

	df['day_of_year'] = df['date'].dt.dayofyear
	df['year'] = df['date'].dt.year

	df['sin_doy'] = np.sin(2 * np.pi * df['day_of_year'] / 365)
	df['cos_doy'] = np.cos(2 * np.pi * df['day_of_year'] / 365)

	df['lag_1'] = df['temp'].shift(1)
	df['lag_2'] = df['temp'].shift(2)
	df['lag_3'] = df['temp'].shift(3)
	df['lag_4'] = df['temp'].shift(4)

	df = df.dropna()

	X = df[['sin_doy', 'cos_doy', 'lag_1', 'lag_2', 'lag_3', 'lag_4']].values
	y = df['temp'].values

	return X, y