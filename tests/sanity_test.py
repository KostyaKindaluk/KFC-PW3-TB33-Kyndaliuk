import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

from database.connection import get_db
from machine_learning.model import load_model
from config.settings import MODEL_PATH


def test_database_connection():
    try:
        with next(get_db()) as db:
            result = db.execute(text("SELECT 1")).scalar()
        assert result == 1
    except SQLAlchemyError as e:
        pytest.fail(f"Database connection failed: {e}")

def test_model_file_exists():
    assert MODEL_PATH.exists(), f"Model file {MODEL_PATH} does not exist"

def test_model_load():
    try:
        model = load_model()
        assert model is not None
    except Exception as e:
        pytest.fail(f"Model loading failed: {e}")