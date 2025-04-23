from contextlib import asynccontextmanager

from api.routers import user
from database import engine
from fastapi import FastAPI
from loging import LogLevels, configure_logging
from sqlmodel import SQLModel
from utils.config import Settings

configure_logging(LogLevels.info)

settings = Settings()

""" db start """


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⏳ creating Tables ...")
    SQLModel.metadata.create_all(engine)
    print("✅ Tables created.")
    yield
    print("👋 Turning off app...")


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)


""" Health check"""


@app.get("/healthy")
def healthy_check():
    return {"status": "healthy"}


app.include_router(user.router)
