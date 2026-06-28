from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile
from fastapi import HTTPException

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.post("/upload")
async def upload_file(
        file: UploadFile = File(...)
):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )
    return {
        "filename": file.filename
    }