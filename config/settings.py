import os
from pathlib import Path


DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "superqwerty123!")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "weather_forecast")

DATABASE_URL = (
  f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


MODEL_PATH = Path("data/model.pkl")
TRAINING_DATA_PATH = Path("data/training_data.csv")
TESTING_DATA_PATH = Path("data/testing_data.csv")