from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import TIMESTAMP
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import text

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


# =====================================================
# QR Codes
# =====================================================

class QRCode(Base):

    __tablename__ = "qr_codes"

    qr_id = Column(
        UUID(as_uuid=True),
        primary_key=True
    )

    short_code = Column(
        String(50),
        unique=True,
        nullable=False
    )

    display_slug = Column(
        String(255),
        nullable=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    destination_url = Column(
        Text,
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

# =====================================================
# Scan Events
# =====================================================

class ScanEvent(Base):

    __tablename__ = "scan_events"

    # -----------------------------
    # Primary Information
    # -----------------------------

    event_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    qr_id = Column(
        UUID(as_uuid=True),
        nullable=False
    )

    scan_timestamp = Column(
        TIMESTAMP,
        server_default=text("NOW()")
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("NOW()")
    )

    # -----------------------------
    # Device Information
    # -----------------------------

    user_agent = Column(Text)

    browser = Column(String(100))

    operating_system = Column(String(100))

    device_type = Column(String(100))

    device_brand = Column(String(100))

    referrer = Column(Text)

    # -----------------------------
    # Geography
    # -----------------------------

    country = Column(String(100))

    country_code = Column(String(10))

    region = Column(String(100))

    city = Column(String(100))

    timezone = Column(String(100))

    # -----------------------------
    # Network
    # -----------------------------

    ip_hash = Column(String(255))

    language = Column(String(50))

    # -----------------------------
    # Session
    # -----------------------------

    session_id = Column(UUID(as_uuid=True))

    visitor_id = Column(UUID(as_uuid=True))

    first_visit = Column(
        Boolean,
        server_default=text("TRUE")
    )

    returning_visitor = Column(
        Boolean,
        server_default=text("FALSE")
    )

    visit_number = Column(
        Integer,
        server_default=text("1")
    )

    # -----------------------------
    # Redirect
    # -----------------------------

    destination_url = Column(Text)

    redirect_timestamp = Column(TIMESTAMP)

    redirect_success = Column(
        Boolean,
        server_default=text("FALSE")
    )

    response_time_ms = Column(Integer)

    # -----------------------------
    # Engagement
    # -----------------------------

    time_on_page = Column(Integer)

    bounce = Column(Boolean)

    clicked_cta = Column(
        Boolean,
        server_default=text("FALSE")
    )

    engagement_score = Column(Integer)