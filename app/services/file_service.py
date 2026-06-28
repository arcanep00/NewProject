import shutil
import uuid
from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    exist_ok=True
)

def save_uploaded_file(file: UploadFile):
    file_extension = Path(file.filename).suffix

    unique_filename = (f"{uuid.uuid4()}{file_extension}")

    file_path = (UPLOAD_DIR / unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "original_filename": file.filename,
        "stored_filename": unique_filename,
        "file_path": str(file_path)
    }

