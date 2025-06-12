from sqlalchemy.orm import Session
from typing import List

from database.models import Weather


def save_forecast(db: Session, forecasts: List[dict]) -> None:
	weather_entries = [Weather(date=entry['date'], temp=entry['temp']) for entry in forecasts]
	
	db.bulk_save_objects(weather_entries)
	db.commit()

def get_all_forecasts(db: Session) -> List[Weather]:
	return db.query(Weather).order_by(Weather.date).all()

def clear_forecasts(db: Session) -> None:
	db.query(Weather).delete()
	db.commit()