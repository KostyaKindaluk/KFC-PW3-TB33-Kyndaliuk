from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import DATABASE_URL


engine = create_engine(
	DATABASE_URL,
	pool_pre_ping=True,
	future=True
)
SessionLocal = sessionmaker(
	bind=engine,
	autoflush=False,
	autocommit=False,
	expire_on_commit=False,
	future=True
)
Base = declarative_base()


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()