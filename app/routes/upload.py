from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_file
from app.db import SessionLocal
from app.models import FileRecord

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = await save_file(file)
    
    db = SessionLocal()
    record = FileRecord(filename=file.filename, path=file_path)
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