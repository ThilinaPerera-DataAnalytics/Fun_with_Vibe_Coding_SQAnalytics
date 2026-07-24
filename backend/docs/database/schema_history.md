# SQAnalytics Database History

---

## Database Version 1.0.0

### 000_create_qr_codes.sql

Creates

- qr_codes

---

### 001_create_scan_events.sql

Creates

- scan_events

---

### 002_enrich_scan_events.sql

Adds

- browser
- operating_system
- device_type
- referrer

---

Status

✅ Production

Release

SQAnalytics Backend v1.0.0

---

## Database Version 1.1.0

### 003_advanced_analytics.sql

- device_brand
- country
- country_code
- region
- city
- timezone
- ip_hash
- language
- session_id
- visitor_id
- first_visit
- returning_visitor
- visit_number
- destination_url
- redirect_timestamp
- redirect_success
- response_time_ms
- time_on_page
- bounce
- clicked_cta
- engagement_score

Status

✅ Production

Release

SQAnalytics Backend v1.1.0

---

## Database Version 1.2.0

### 004_add_display_slug.sql

Adds

- display_slug

Purpose

- Enables human-friendly QR URLs.
- Allows descriptive URLs while preserving backward compatibility with existing QR codes.

Example

Old URL

```
https://[Sub-domain].kndb.stream/r/19fba1ff
```

New URL

```
https://[Sub-domain].kndb.stream/r/19fba1ff-where-words-meet-music
```

---

### 005_fix_timestamps.sql

Adds

- created_at default timestamp
- updated_at default timestamp

Purpose

- PostgreSQL now automatically populates timestamps.
- Removes dependency on application-generated timestamps.
- Ensures consistent audit information across all database writes.

---

Status

✅ Production

Release

SQAnalytics Backend v1.2.0