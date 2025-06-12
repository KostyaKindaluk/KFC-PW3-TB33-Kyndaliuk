import pickle
from sklearn.ensemble import RandomForestRegressor

from config.settings import MODEL_PATH, TRAINING_DATA_PATH
from machine_learning.preprocess import load_and_clean_weather_data, add_training_features


def train_model() -> RandomForestRegressor:
	df = load_and_clean_weather_data(TRAINING_DATA_PATH)
	X, y = add_training_features(df)

	model = RandomForestRegressor(n_estimators=100, random_state=42)
	model.fit(X, y)

	with open(MODEL_PATH, "wb") as f:
		pickle.dump(model, f)

	return model

def load_model() -> RandomForestRegressor:
	if not MODEL_PATH.exists():
		raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
	
	with open(MODEL_PATH, "rb") as f:
		model = pickle.load(f)
	
	return model


if __name__ == "__main__":
	train_model()