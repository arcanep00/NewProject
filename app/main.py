from fastapi import FastAPI
from app.core.config import settings
from app.db.init__db import init_db

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

