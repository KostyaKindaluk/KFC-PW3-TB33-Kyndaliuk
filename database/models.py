from sqlalchemy import Column, Integer, Float, Date, UniqueConstraint
from database.connection import Base


class Weather(Base):
	__tablename__ = "weather"

	id = Column(Integer, primary_key=True, autoincrement=True)
	date = Column(Date, nullable=False)
	temp = Column(Float, nullable=False)

	__table_args__ = (
		UniqueConstraint('date', name='uq_weather_date'),
	)

	def __repr__(self):
		return f"<Weather(id={self.id}, date={self.date}, temp={self.temp})>"