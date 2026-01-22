from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from app.health import router as health_router
from google.cloud import storage
from typing import Optional
import os


# =========================
# Google Cloud Storage init
# =========================

client = storage.Client()  # Uses ADC (Workload Identity / gcloud)
bucket_name = os.getenv("GCS_BUCKET")

if not bucket_name:
    raise RuntimeError("GCS_BUCKET environment variable is not set")

bucket = client.bucket(bucket_name)


# =========================
# FastAPI app
# =========================

app = FastAPI(
    title="DevOps Final Project API",
    version="0.1.0",
)

# Health check
app.include_router(health_router)


# =========================
# Root endpoint
# =========================

@app.get("/")
def root():
    return {"message": "Backend is running"}


# =========================
# List files and folders
# =========================

@app.get("/files")
def list_files(prefix: str = ""):
    """
    Returns a list of files and folders in the bucket
    """
    try:
        blobs = bucket.list_blobs(prefix=prefix)

        folders = set()
        files = []

        for blob in blobs:
            name = blob.name

            if "/" in name:
                folders.add(name.split("/")[0] + "/")

            if not name.endswith("/"):
                files.append(name)

        return {
            "prefix": prefix,
            "folders": sorted(folders),
            "files": sorted(files),
        }

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# =========================
# Upload file
# =========================

UPLOAD_FOLDER = "uploads"


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    folder: Optional[str] = None,
):
    """
    Uploads a file to the specified folder or to uploads/ by default
    """
    try:
        contents = await file.read()

        if folder:
            folder = folder.rstrip("/")
            path = f"{folder}/{file.filename}"
        else:
            path = f"{UPLOAD_FOLDER}/{file.filename}"

        blob = bucket.blob(path)
        blob.upload_from_string(
            contents,
            content_type=file.content_type,
        )

        return {
            "filename": file.filename,
            "path": path,
            "bucket": bucket.name,
            "status": "uploaded",
        }

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# =========================
# Create folder
# =========================

@app.post("/folders")
def create_folder(folder: str = Body(..., embed=True)):
    """
    Creates a logical folder (placeholder object)
    """
    try:
        if not folder.endswith("/"):
            folder += "/"

        blob = bucket.blob(folder)
        blob.upload_from_string("")

        return {
            "folder": folder,
            "status": "created",
        }

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# =========================
# Delete file
# =========================

@app.delete("/files")
def delete_file(path: str):
    """
    Deletes a file by its full path
    """
    try:
        blob = bucket.blob(path)

        if not blob.exists():
            raise HTTPException(status_code=404, detail="File not found")

        blob.delete()

        return {
            "file": path,
            "status": "deleted",
        }

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# =========================
# Delete folder
# =========================

@app.delete("/folders")
def delete_folder(folder: str):
    """
    Deletes a folder and all objects with the given prefix
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
            "deleted_files": deleted,
        }

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# =========================
# Move file
# =========================

@app.post("/files/move")
def move_file(
    source: str = Body(..., embed=True),
    destination: str = Body(..., embed=True),
):
    """
    Moves a file (copy + delete)
    """
    try:
        source_blob = bucket.blob(source)

        if not source_blob.exists():
            raise HTTPException(
                status_code=404,
                detail="Source file not found",
            )

        bucket.copy_blob(
            source_blob,
            bucket,
            destination,
        )

        source_blob.delete()

        return {
            "from": source,
            "to": destination,
            "status": "moved",
        }

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
