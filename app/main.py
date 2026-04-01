from fastapi import FastAPI
from app.routes import upload
from app.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AWS Data Pipeline API")
app.include_router(upload.router)

@app.get("/")
async def root():
    return {"message": "API is running"}


