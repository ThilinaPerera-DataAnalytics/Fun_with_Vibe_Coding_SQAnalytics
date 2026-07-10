from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import TIMESTAMP
from sqlalchemy import text

from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


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

    created_at = Column(TIMESTAMP)

    updated_at = Column(TIMESTAMP)


class ScanEvent(Base):

    __tablename__ = "scan_events"

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

    user_agent = Column(Text)

    browser = Column(String(100))

    operating_system = Column(String(100))

    device_type = Column(String(100))

    referrer = Column(Text)

    created_at = Column(
        TIMESTAMP,
        server_default=text("NOW()")
    )