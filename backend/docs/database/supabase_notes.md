# SQAnalytics Supabase Configuration

This document records the Supabase project configuration used during SQAnalytics backend development.

---

# Project Information

| Item | Value |
|------|-------|
| Project Name | SQAnalytics-dev |
| Organization | Thilina Perera - Data Analytics |
| Region | Asia-Pacific |
| Database Engine | PostgreSQL 17.6 |
| Cloud Provider | Supabase |

---

# Current Database

## Production Tables

### qr_codes

Stores all registered QR codes.

Current columns include:

- qr_id
- short_code
- display_slug
- title
- destination_url
- status
- created_at
- updated_at

---

### scan_events

Stores every QR scan together with analytics.

Current analytics include:

- Scan timestamp
- Browser
- Operating System
- Device Type
- Device Brand
- Referrer
- Country
- Country Code
- Region
- City
- Timezone
- Language
- Session ID
- Visitor ID
- Returning Visitor
- Redirect Destination
- Redirect Timestamp
- Redirect Success
- Response Time
- Engagement placeholders

---

# Database Migrations

| Migration | Purpose | Status |
|-----------|---------|--------|
| 000_create_qr_codes.sql | Initial QR Registry | ✅ |
| 001_create_scan_events.sql | Scan Event Table | ✅ |
| 002_enrich_scan_events.sql | Browser / Device Analytics | ✅ |
| 003_advanced_analytics.sql | Advanced Analytics Columns | ✅ |
| 004_add_display_slug.sql | Human-Friendly QR URLs | ✅ |
| 005_fix_timestamps.sql | Automatic PostgreSQL Timestamps | ✅ |

---

# Production Environment

## Backend

FastAPI

Hosted on:

Render

---

## Database

Supabase PostgreSQL

---

## Permanent QR Domain

```text
https://love-bar.kndb.stream
```

---

# Current Backend Release

**SQAnalytics Backend v1.2.0**

---

# Notes

- PostgreSQL automatically manages record timestamps.
- QR redirects remain permanently accessible through the custom Cloudflare domain.
- Human-friendly URLs remain fully backward compatible with legacy QR codes.
- Database schema evolution is documented separately in:

```text
backend/docs/database/schema_history.md
```