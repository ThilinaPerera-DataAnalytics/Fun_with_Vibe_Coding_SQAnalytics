from uuid import uuid4

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import QRCode
from app.models import ScanEvent
from app.qr_generator import generate_qr_image

import re
import unicodedata

def create_qr(
    db: Session,
    title: str,
    destination_url: str,
    display_slug: str | None = None
):

    short_code = str(uuid4())[:8]

    # Create a URL-friendly slug

    # -----------------------------------------
# Generate URL-safe display slug
# -----------------------------------------

    if display_slug:

        # Remove accents and normalize Unicode
        display_slug = unicodedata.normalize(
            "NFKD",
            display_slug
        ).encode(
            "ascii",
            "ignore"
        ).decode(
            "ascii"
        )

        # Lowercase
        display_slug = display_slug.lower()

        # Replace non-alphanumeric characters
        display_slug = re.sub(
            r"[^a-z0-9]+",
            "-",
            display_slug
        )

        # Collapse repeated hyphens
        display_slug = re.sub(
            r"-+",
            "-",
            display_slug
        )

        # Remove leading/trailing hyphens
        display_slug = display_slug.strip("-")

        # Limit maximum length
        display_slug = display_slug[:100]

        # Fallback if slug becomes empty
        if not display_slug:
            display_slug = None

    qr = QRCode(
        qr_id=uuid4(),
        short_code=short_code,
        display_slug=display_slug,
        title=title,
        destination_url=destination_url,
        status="active"
    )

    db.add(qr)
    db.commit()
    db.refresh(qr)

    qr_file = generate_qr_image(
    short_code=short_code,
    display_slug=display_slug
)

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
    **event_data
):

    """
        Creates a scan event using keyword arguments.

        Accepts any ScanEvent model field as a keyword argument,
        allowing future analytics fields to be added without
        modifying this function.
    """

    event = ScanEvent(
        **event_data
    )

    db.add(event)
    db.commit()
    db.refresh(event)

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