from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.jobs import router as jobs_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(jobs_router)

@app.get("/")
def root():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

