from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(
    title="SQAnalytics API",
    description="Smart QR Analytics Platform Backend",
    version="0.1.0"
)


# -----------------------------
# Temporary Storage
# -----------------------------

qr_storage = []


# -----------------------------
# Request Model
# -----------------------------

class QRCreateRequest(BaseModel):
    destination_url: str


# -----------------------------
# Root
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "SQAnalytics API is running"
    }


# -----------------------------
# Health
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
# Create QR
# -----------------------------

@app.post("/qr")
def create_qr(payload: QRCreateRequest):

    qr_record = {
        "qr_id": str(uuid4()),
        "destination_url": payload.destination_url
    }

    qr_storage.append(qr_record)

    return qr_record


# -----------------------------
# Get All QRs
# -----------------------------

@app.get("/qr")
def get_all_qrs():
    return qr_storage