from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from app.health import router as health_router
from google.cloud import storage
import os

# =========================
# Google Cloud Storage init
# =========================

client = storage.Client()  # Использует ADC (Workload Identity / gcloud)
bucket_name = os.getenv("GCS_BUCKET")

if not bucket_name:
    raise RuntimeError("GCS_BUCKET env variable is not set")

bucket = client.bucket(bucket_name)

# =========================
# FastAPI app
# =========================

app = FastAPI(
    title="DevOps Final Project API",
    version="0.1.0"
)

# Health check
app.include_router(health_router)

# =========================
# Root
# =========================

@app.get("/")
def root():
    return {
        "message": "Backend is running"
    }

# =========================
# Upload file
# =========================

UPLOAD_FOLDER = "uploads"

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        blob_path = f"{UPLOAD_FOLDER}/{file.filename}"
        blob = bucket.blob(blob_path)

        blob.upload_from_string(
            contents,
            content_type=file.content_type
        )

        return {
            "filename": file.filename,
            "path": blob_path,
            "bucket": bucket.name,
            "status": "uploaded"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# =========================
# Create folder
# =========================

@app.post("/folders")
def create_folder(folder: str = Body(..., embed=True)):
    """
    Создаёт логическую папку в GCS
    """
    try:
        if not folder.endswith("/"):
            folder += "/"

        blob = bucket.blob(folder)
        blob.upload_from_string("")

        return {
            "folder": folder,
            "status": "created"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# =========================
# Delete file
# =========================

@app.delete("/files")
def delete_file(path: str):
    """
    Удаляет файл по полному пути
    """
    try:
        blob = bucket.blob(path)

        if not blob.exists():
            raise HTTPException(status_code=404, detail="File not found")

        blob.delete()

        return {
            "file": path,
            "status": "deleted"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# =========================
# Delete folder
# =========================

@app.delete("/folders")
def delete_folder(folder: str):
    """
    Удаляет папку (все файлы с этим префиксом)
    """
    try:
        if not folder.endswith("/"):
            folder += "/"

        blobs = bucket.list_blobs(prefix=folder)
        deleted = 0

        for blob in blobs:
            blob.delete()
            deleted += 1

        return {
            "folder": folder,
            "deleted_files": deleted
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
