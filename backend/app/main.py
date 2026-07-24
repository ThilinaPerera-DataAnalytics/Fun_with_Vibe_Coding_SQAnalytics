import time
from datetime import datetime, UTC

from fastapi import Depends
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse

from sqlalchemy import text
from sqlalchemy.orm import Session

from pathlib import Path

from app.database import engine
from app.database import get_db

from app.schemas import QRCreate

from app.crud import create_qr
from app.crud import get_all_qrs
from app.crud import get_qr_by_short_code
from app.crud import create_scan_event
from app.crud import get_total_scans
from app.crud import get_browser_distribution
from app.crud import get_device_distribution

from user_agents import parse

from app.qr_generator import generate_qr_image
from app.qr_generator import BASE_URL

app = FastAPI(
    title="SQAnalytics API",
    description="Smart QR Analytics Platform Backend",
    version="1.2.0"
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
        "version": "1.2.0"
    }

@app.get("/db-test")
def db_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT version();")
            )
            version = result.scalar()
            return {
                "status": "connected",
                "database": version
            }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }

@app.post("/qr")
def create_new_qr(
    qr: QRCreate,
    db: Session = Depends(get_db)
):
    result = create_qr(
    db=db,
    title=qr.title,
    destination_url=qr.destination_url,
    display_slug=qr.display_slug
    )

    created_qr = result["qr"]
    qr_file = result["qr_file"]

    redirect_url = (
        f"{BASE_URL}/r/{created_qr.short_code}"
    )

    if created_qr.display_slug:
        redirect_url = (
            f"{BASE_URL}/r/"
            f"{created_qr.short_code}-{created_qr.display_slug}"
        )

    return {
        "qr_id": str(created_qr.qr_id),
        "short_code": created_qr.short_code,
        "display_slug": created_qr.display_slug,
        "redirect_url": redirect_url,
        "title": created_qr.title,
        "destination_url": created_qr.destination_url,
        "status": created_qr.status,
        "qr_file": qr_file
    }

@app.get("/qr")
def get_qr_endpoint(
    db: Session = Depends(get_db)
):
    qrs = get_all_qrs(db)
    results = []

    for qr in qrs:
        results.append(
            {
                "qr_id": str(qr.qr_id),
                "short_code": qr.short_code,
                "title": qr.title,
                "destination_url": qr.destination_url,
                "status": qr.status
            }
        )
    return results

@app.get("/r/{qr_identifier}")
def redirect_qr(
    qr_identifier: str,
    request: Request,
    db: Session = Depends(get_db)
):

    # ---------------------------------
    # Extract short code from URL
    # ---------------------------------

    short_code = qr_identifier.split("-", 1)[0]

    qr = get_qr_by_short_code(
        db=db,
        short_code=short_code
    )

    if not qr:

        return {
            "error": "QR code not found"
        }

    # ---------------------------------
    # Start response time measurement
    # ---------------------------------

    start_time = time.perf_counter()

    # ---------------------------------
    # Request Information
    # ---------------------------------

    user_agent_string = request.headers.get(
        "user-agent",
        ""
    )

    language = request.headers.get(
        "accept-language",
        ""
    )

    ua = parse(user_agent_string)

    browser = ua.browser.family

    operating_system = ua.os.family

    if ua.is_mobile:
        device_type = "Mobile"

    elif ua.is_tablet:
        device_type = "Tablet"

    elif ua.is_pc:
        device_type = "Desktop"

    else:
        device_type = "Other"

    # ---------------------------------
    # Analytics
    # ---------------------------------

    response_time_ms = int(
        (time.perf_counter() - start_time) * 1000
    )

    redirect_timestamp = datetime.now(UTC)

    create_scan_event(
        db=db,
        qr_id=qr.qr_id,
        user_agent=user_agent_string,
        browser=browser,
        operating_system=operating_system,
        device_type=device_type,
        referrer=request.headers.get("referer"),
        language=language,
        destination_url=qr.destination_url,
        redirect_timestamp=redirect_timestamp,
        redirect_success=True,
        response_time_ms=response_time_ms
    )

    return RedirectResponse(
        url=qr.destination_url,
        status_code=302
    )

@app.get("/analytics/summary")
def analytics_summary(
    db: Session = Depends(get_db)
):

    total_scans = get_total_scans(db)

    browsers = get_browser_distribution(db)

    devices = get_device_distribution(db)

    browser_results = []

    for browser in browsers:

        browser_results.append(
            {
                "browser": browser[0],
                "count": browser[1]
            }
        )

    device_results = []

    for device in devices:

        device_results.append(
            {
                "device_type": device[0],
                "count": device[1]
            }
        )

    return {
        "total_scans": total_scans,
        "browser_distribution": browser_results,
        "device_distribution": device_results
    }

@app.get("/qr/{short_code}/generate")
def generate_qr(
    short_code: str,
    db: Session = Depends(get_db)
):

    qr = get_qr_by_short_code(
        db=db,
        short_code=short_code
    )

    if not qr:

        return {
            "error": "QR code not found"
        }

    file_path = generate_qr_image(
        short_code=qr.short_code,
        display_slug=qr.display_slug
    )

    return {
        "message": "QR generated",
        "file": file_path
    }

@app.get("/qr/{short_code}/download")
def download_qr(
    short_code: str,
    db: Session = Depends(get_db)
):
    """
    Download a generated QR code as a PNG file.
    """

    qr = get_qr_by_short_code(
        db=db,
        short_code=short_code
    )

    if not qr:
        return {
            "error": "QR code not found"
        }

    file_path = Path("generated_qr") / f"{short_code}.png"

    if not file_path.exists():

        generate_qr_image(
            short_code=qr.short_code,
            display_slug=qr.display_slug
    )

    return FileResponse(
        path=file_path,
        media_type="image/png",
        filename=f"{short_code}.png"
    )