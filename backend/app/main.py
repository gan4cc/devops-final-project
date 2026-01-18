from fastapi import FastAPI
from app.health import router as health_router

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
