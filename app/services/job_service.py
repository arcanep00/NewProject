from app.models.job import Job
from sqlalchemy.orm import Session

def create_job(db: Session, filename: str):
    job = Job(filename=filename, status="pending")

    db.add(job)

    db.commit()

    db.refresh(job)

    return job