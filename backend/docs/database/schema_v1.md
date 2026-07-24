# SQAnalytics Database Schema (Current)

**Current Stable Release:** Backend v1.2.0

This document describes the current production database schema used by SQAnalytics.

---

# Table: qr_codes

Stores every registered QR code and its associated redirect information.

| Column | Data Type | Description |
|----------|-----------|-------------|
| qr_id | UUID | Primary Key |
| short_code | VARCHAR(20) | Unique redirect identifier |
| display_slug | VARCHAR(255) | Human-friendly URL slug (optional) |
| title | VARCHAR(255) | QR title |
| destination_url | TEXT | Redirect destination URL |
| status | VARCHAR(20) | active / inactive |
| created_at | TIMESTAMP | Automatically generated creation timestamp |
| updated_at | TIMESTAMP | Automatically managed update timestamp |

---

## Example URLs

Legacy URL

```text
https://love-bar.kndb.stream/r/19fba1ff
```

Human-Friendly URL

```text
https://love-bar.kndb.stream/r/19fba1ff-where-words-meet-music
```

Both URLs remain fully supported.

---

# Table: scan_events

Stores every QR scan together with analytics collected during the redirect process.

| Column | Data Type | Description |
|----------|-----------|-------------|
| event_id | UUID | Primary Key |
| qr_id | UUID | Related QR Code |
| scan_timestamp | TIMESTAMP | Time the QR was scanned |
| user_agent | TEXT | Raw User-Agent |
| browser | VARCHAR(100) | Browser name |
| operating_system | VARCHAR(100) | Operating System |
| device_type | VARCHAR(50) | Device category |
| device_brand | VARCHAR(100) | Device manufacturer |
| referrer | TEXT | HTTP Referrer |
| country | VARCHAR(100) | Country |
| country_code | VARCHAR(10) | ISO Country Code |
| region | VARCHAR(100) | State / Province |
| city | VARCHAR(100) | City |
| timezone | VARCHAR(100) | Visitor timezone |
| ip_hash | VARCHAR(255) | Hashed IP address |
| language | VARCHAR(50) | Browser language |
| session_id | UUID | Visitor session identifier |
| visitor_id | UUID | Returning visitor identifier |
| first_visit | BOOLEAN | First visit flag |
| returning_visitor | BOOLEAN | Returning visitor flag |
| visit_number | INTEGER | Visit count |
| destination_url | TEXT | Redirect destination |
| redirect_timestamp | TIMESTAMP | Redirect execution time |
| redirect_success | BOOLEAN | Redirect completed successfully |
| response_time_ms | INTEGER | Redirect response time |
| time_on_page | INTEGER | Reserved for future frontend analytics |
| bounce | BOOLEAN | Reserved for future frontend analytics |
| clicked_cta | BOOLEAN | Reserved for future frontend analytics |
| engagement_score | INTEGER | Reserved for future frontend analytics |
| created_at | TIMESTAMP | Record creation timestamp |

---

# Relationships

```text
qr_codes
    │
    │ 1
    │
    └───────────────∞
                    │
             scan_events
```

One QR code may generate many scan events.

---

# Schema Evolution

| Version | Major Changes |
|----------|---------------|
| v1.0 | QR Registry |
| v1.1 | Analytics Expansion |
| v1.2 | Human-Friendly URLs + Display Slug + Automatic Database Timestamps |

---

# Current Status

Production Ready

**SQAnalytics Backend v1.2.0**