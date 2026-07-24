# SQAnalytics Database Schema Evolution

This document records the evolution of the SQAnalytics database schema throughout backend development.

---

# Version 1.0

## Table: qr_codes

| Column | Type | Description |
|----------|----------|----------|
| qr_id | UUID | Primary Key |
| short_code | VARCHAR(20) | Unique QR identifier |
| title | VARCHAR(255) | QR title |
| destination_url | TEXT | Redirect destination |
| status | VARCHAR(20) | active / inactive |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

---

## Table: scan_events

| Column | Type | Description |
|----------|----------|----------|
| event_id | UUID | Primary Key |
| qr_id | UUID | Related QR Code |
| scan_timestamp | TIMESTAMP | Scan timestamp |
| user_agent | TEXT | Raw User-Agent |
| browser | VARCHAR(100) | Browser name |
| operating_system | VARCHAR(100) | Operating System |
| device_type | VARCHAR(50) | Mobile / Tablet / PC |
| referrer | TEXT | HTTP Referrer |
| created_at | TIMESTAMP | Record creation timestamp |

---

# Version 1.1

The analytics schema was expanded to support richer visitor intelligence.

## Device

- device_brand

---

## Geography

- country
- country_code
- region
- city
- timezone

---

## Network

- ip_hash
- language

---

## Session

- session_id
- visitor_id
- first_visit
- returning_visitor
- visit_number

---

## Redirect

- destination_url
- redirect_timestamp
- redirect_success
- response_time_ms

---

## Engagement

- time_on_page
- bounce
- clicked_cta
- engagement_score

---

# Version 1.2

Backend v1.2 introduced human-friendly QR URLs while preserving complete backward compatibility.

## qr_codes

New Column

- display_slug

Example

Old

```
https://love-bar.kndb.stream/r/19fba1ff
```

New

```
https://love-bar.kndb.stream/r/19fba1ff-where-words-meet-music
```

---

## Timestamp Improvements

PostgreSQL now automatically manages:

- created_at
- updated_at

using database defaults instead of application-generated timestamps.

---

# Current Status

Current Stable Release

**SQAnalytics Backend v1.2.0**