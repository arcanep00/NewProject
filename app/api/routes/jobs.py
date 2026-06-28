from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException
from app.services.file_service import save_uploaded_file
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.job_service import create_job

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.post("/upload")
async def upload_file(
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    uploaded_file = save_uploaded_file(file)

    job = create_job(
        db=db,
        filename=uploaded_file["stored_filename"]
    )

    return {
        "job_id": job.id,
        "status": job.status,
        "filename": job.filename
    }