from uuid import uuid4

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import QRCode
from app.models import ScanEvent
from app.qr_generator import generate_qr_image


def create_qr(
    db: Session,
    title: str,
    destination_url: str
):

    short_code = str(uuid4())[:8]

    qr = QRCode(
        qr_id=uuid4(),
        short_code=short_code,
        title=title,
        destination_url=destination_url,
        status="active"
    )

    db.add(qr)
    db.commit()
    db.refresh(qr)

    qr_file = generate_qr_image(short_code)

    return {
        "qr": qr,
        "qr_file": qr_file
    }


def get_all_qrs(
    db: Session
):

    return db.query(QRCode).all()


def get_qr_by_short_code(
    db: Session,
    short_code: str
):

    return (
        db.query(QRCode)
        .filter(QRCode.short_code == short_code)
        .first()
    )


def create_scan_event(
    db: Session,
    qr_id,
    user_agent,
    browser,
    operating_system,
    device_type,
    referrer
):

    event = ScanEvent(
        qr_id=qr_id,
        user_agent=user_agent,
        browser=browser,
        operating_system=operating_system,
        device_type=device_type,
        referrer=referrer
    )

    db.add(event)
    db.commit()

    return event


def get_total_scans(
    db: Session
):

    return db.query(
        func.count(ScanEvent.event_id)
    ).scalar()


def get_browser_distribution(
    db: Session
):

    return (
        db.query(
            ScanEvent.browser,
            func.count(ScanEvent.event_id)
        )
        .group_by(
            ScanEvent.browser
        )
        .all()
    )


def get_device_distribution(
    db: Session
):

    return (
        db.query(
            ScanEvent.device_type,
            func.count(ScanEvent.event_id)
        )
        .group_by(
            ScanEvent.device_type
        )
        .all()
    )