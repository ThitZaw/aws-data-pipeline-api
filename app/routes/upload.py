from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_file
from app.db import SessionLocal
from app.models import FileRecord
from app.services.s3_service import upload_file_to_s3

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = await save_file(file)
    s3_key = f"raw/{file.filename}"
    s3_path = upload_file_to_s3(file_path, s3_key)
    
    db = SessionLocal()
    record = FileRecord(filename=file.filename, path=file_path, s3_path=s3_path)
    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()
    
    return {
        "filename": file.filename, "id": record.id
    }
    
    
@router.get("/data")
def get_data():
    db = SessionLocal()
    records = db.query(FileRecord).all()
    db.close()
    
    return records