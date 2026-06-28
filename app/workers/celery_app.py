from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "transaction_processor",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

@celery_app.task
def test_task():
    return {
        "message": "Celery is working"
    }