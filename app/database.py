# database.py
from sqlmodel import create_engine
from utils.config import Settings

settings = Settings()

connect_args = (
    {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
)

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)
