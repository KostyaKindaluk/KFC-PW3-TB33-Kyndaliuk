import numpy as np
import pandas as pd
from datetime import timedelta, date

from config.settings import MODEL_PATH, TRAINING_DATA_PATH
from machine_learning.model import load_model
from machine_learning.preprocess import load_and_clean_weather_data


def prepare_input_features(date: date, df: pd.DataFrame) -> np.ndarray:
	df = df.sort_values("date")
	last_rows = df.tail(4)

	if len(last_rows) < 4:
		raise ValueError("Недостатньо даних для формування лагів (потрібно хоча б 4 попередні дні).")

	lag_1 = last_rows.iloc[-1]['temp']
	lag_2 = last_rows.iloc[-2]['temp']
	lag_3 = last_rows.iloc[-3]['temp']
	lag_4 = last_rows.iloc[-4]['temp']

	day_of_year = date.timetuple().tm_yday
	sin_doy = np.sin(2 * np.pi * day_of_year / 365)
	cos_doy = np.cos(2 * np.pi * day_of_year / 365)

	features = np.array([[sin_doy, cos_doy, lag_1, lag_2, lag_3, lag_4]])
	return features

def predict_temperature_for_date(date_str: str) -> float:
	model = load_model(MODEL_PATH)
	df = load_and_clean_weather_data(TRAINING_DATA_PATH)

	if isinstance(date_str, str):
		date = date.strptime(date_str, "%Y-%m-%d").date()
	else:
		date = date_str

	features = prepare_input_features(date, df)
	predicted_temp = model.predict(features)[0]

	return predicted_temp

def predict_temperatures(model, start_date: date, lag_1: float, lag_2: float, lag_3: float, lag_4: float, num_days: int = 365):
	predictions = []

	current_date = start_date
	for _ in range(num_days):
		day_of_year = current_date.timetuple().tm_yday
		sin_doy = np.sin(2 * np.pi * day_of_year / 365)
		cos_doy = np.cos(2 * np.pi * day_of_year / 365)

		features = np.array([[sin_doy, cos_doy, lag_1, lag_2, lag_3, lag_4]])
		predicted_temp = model.predict(features)[0]

		predictions.append({
			"date": current_date,
			"temp": predicted_temp
		})

		lag_4 = lag_3
		lag_3 = lag_2
		lag_2 = lag_1
		lag_1 = predicted_temp

		current_date += timedelta(days=1)

	return predictions