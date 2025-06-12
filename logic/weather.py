from pathlib import Path
from datetime import timedelta
import pandas as pd

from database.connection import get_db
from database.crud import save_forecast, get_all_forecasts, clear_forecasts
from machine_learning.model import load_model
from machine_learning.predict import predict_temperatures
from machine_learning.preprocess import load_and_clean_weather_data
from config.settings import TRAINING_DATA_PATH


def create_forecasts_for_year():
	df = load_and_clean_weather_data(TRAINING_DATA_PATH)

	last_four = df.tail(4)
	if len(last_four) < 4:
		raise ValueError("Потрібно щонайменше 4 дні в історичних даних.")

	lag_1 = last_four.iloc[-1]['temp']
	lag_2 = last_four.iloc[-2]['temp']
	lag_3 = last_four.iloc[-3]['temp']
	lag_4 = last_four.iloc[-4]['temp']
	start_date = last_four.iloc[-1]['date'] + timedelta(days=1)

	model = load_model()
	predictions = predict_temperatures(model, start_date, lag_1, lag_2, lag_3, lag_4, num_days=365)

	with next(get_db()) as db:
		save_forecast(db, predictions)

	return predictions

def get_forecasts():
	with next(get_db()) as db:
		return get_all_forecasts(db)

def clear_all_forecasts():
	with next(get_db()) as db:
		clear_forecasts(db)