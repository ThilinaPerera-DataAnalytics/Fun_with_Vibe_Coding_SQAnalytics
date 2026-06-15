from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="SQAnalytics API",
    description="Smart QR Analytics Platform Backend",
    version="0.1.0"
)


# -----------------------------
# Data Model
# -----------------------------

class QRCreateRequest(BaseModel):
    destination_url: str


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "SQAnalytics API is running"
    }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# -----------------------------
# Version
# -----------------------------

@app.get("/version")
def version():
    return {
        "project": "SQAnalytics",
        "version": "0.1.0"
    }


# -----------------------------
# Create QR (Mock)
# -----------------------------

@app.post("/qr")
def create_qr(payload: QRCreateRequest):

    return {
        "message": "QR record created successfully",
        "destination_url": payload.destination_url
    }