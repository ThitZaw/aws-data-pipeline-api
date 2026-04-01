from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_file

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = await save_file(file)
    return {
        "filename": file.filename, "save_to": file_path
    }
    
    
@router.get("/data")
def get_data():
    return {
        "message": "simple data endpoint"
    }