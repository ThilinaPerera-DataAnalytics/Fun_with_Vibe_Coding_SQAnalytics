from datetime import datetime

from pydantic import BaseModel


# =====================================================
# QR Schemas
# =====================================================

class QRCreate(BaseModel):
    """Request model for creating a new QR code."""
    title: str
    destination_url: str
    display_slug: str | None = None

class QRUpdate(BaseModel):
    """ Schema for updating an existing QR code destination URL."""

    destination_url: str

class QRResponse(BaseModel):
    """Response model returned after QR creation or retrieval."""
    qr_id: str
    short_code: str
    display_slug: str | None = None
    title: str
    destination_url: str
    status: str

    class Config:
        from_attributes = True


# =====================================================
# Scan Event Schemas
# =====================================================

class ScanEventCreate(BaseModel):
    """Schema used to record a QR scan event."""

    qr_id: str

    # Client Information
    user_agent: str | None = None
    browser: str | None = None
    operating_system: str | None = None
    device_type: str | None = None
    device_brand: str | None = None

    referrer: str | None = None

    # Geographic Information
    country: str | None = None
    country_code: str | None = None
    region: str | None = None
    city: str | None = None
    timezone: str | None = None

    ip_hash: str | None = None
    language: str | None = None

    # Visitor Information
    session_id: str | None = None
    visitor_id: str | None = None
    first_visit: bool | None = True
    returning_visitor: bool | None = False
    visit_number: int | None = 1

    # Redirect Information
    destination_url: str | None = None
    redirect_timestamp: datetime | None = None
    redirect_success: bool | None = False
    response_time_ms: int | None = None

    # Engagement Metrics
    time_on_page: int | None = None
    bounce: bool | None = None
    clicked_cta: bool | None = False
    engagement_score: int | None = None


class ScanEventResponse(ScanEventCreate):
    """Response model for a stored scan event."""

    event_id: str
    scan_timestamp: datetime
    created_at: datetime

    class Config:
        from_attributes = True