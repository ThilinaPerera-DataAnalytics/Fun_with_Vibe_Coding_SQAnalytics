from fastapi import FastAPI

app = FastAPI(
    title="SQAnalytics API",
    description="Smart QR Analytics Platform Backend",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "SQAnalytics API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "project": "SQAnalytics",
        "version": "0.1.0"
    }