from fastapi import FastAPI
from app.health import router as health_router
from google.cloud import storage
import os
from fastapi import UploadFile, File

client = storage.Client()  # ← ищет ADC автоматически
bucket = client.bucket(os.getenv("GCS_BUCKET"))

app = FastAPI(
    title="DevOps Final Project API",
    version="0.1.0"
)

# Health check
app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Backend is running"
    }
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    blob = bucket.blob(file.filename)
    contents = await file.read()
    blob.upload_from_string(contents, content_type=file.content_type)
    return {
        "filename": file.filename,
        "bucket": bucket.name
    }
