import pytest
from sklearn.metrics import mean_squared_error, r2_score

from machine_learning.preprocess import load_and_clean_weather_data, add_training_features
from machine_learning.model import load_model
from config.settings import TRAINING_DATA_PATH


@pytest.fixture(scope="module")
def model():
	return load_model()

@pytest.fixture(scope="module")
def test_data():
	df = load_and_clean_weather_data(TRAINING_DATA_PATH)
	X_test, y_test = add_training_features(df)
	return X_test, y_test

def test_model_predictions(model, test_data):
	X_test, y_test = test_data

	preds = model.predict(X_test)

	mse = mean_squared_error(y_test, preds)
	r2 = r2_score(y_test, preds)

	print(f"Test MSE: {mse:.4f}, R2: {r2:.4f}")

	assert mse < 5.0, "Середньоквадратична помилка занадто висока"
	assert r2 > 0.5, "Модель погано пояснює дисперсію"