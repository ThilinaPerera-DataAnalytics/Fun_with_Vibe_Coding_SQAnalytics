# SQAnalytics System Architecture

**Current Stable Release:** Backend v1.2.0

---

# Overview

SQAnalytics is a full-stack analytics platform designed to bridge physical QR codes with digital engagement analytics.

Every QR code acts as a permanent gateway that records scan analytics before redirecting the visitor to its destination.

---

# High-Level Architecture

```text
                 Reader / Mobile Device
                          │
                          │
                    Scan QR Code
                          │
                          ▼
      https://love-bar.kndb.stream/r/{short_code}-{display_slug}
                          │
                          ▼
               Cloudflare DNS & SSL
                          │
                          ▼
               FastAPI Backend (Render)
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
  QR Registry Lookup             Scan Analytics Engine
          │                               │
          └───────────────┬───────────────┘
                          │
                          ▼
               PostgreSQL (Supabase)
                          │
                          ▼
            Redirect to Destination URL
                          │
                          ▼
         YouTube / Website / Digital Content
```

---

# Request Flow

```text
User
 │
 ▼
Scans QR Code
 │
 ▼
Cloudflare
 │
 ▼
Render (FastAPI)
 │
 ▼
Locate QR Record
 │
 ▼
Capture Analytics
 │
 ▼
Store Analytics
 │
 ▼
HTTP Redirect
 │
 ▼
Destination Content
```

---

# Backend Components

## API Layer

Responsible for:

- QR Management
- Redirect Engine
- Analytics API
- Health Monitoring

Technology

- FastAPI
- Uvicorn

---

## QR Generation Engine

Responsible for:

- QR generation
- Human-friendly QR URLs
- Logo embedding
- PNG generation

Libraries

- qrcode
- Pillow

---

## Redirect Engine

Responsibilities

- Locate QR record
- Validate status
- Record analytics
- Redirect visitor

Supported URL formats

Legacy

```text
/r/19fba1ff
```

Human-Friendly

```text
/r/19fba1ff-where-words-meet-music
```

Both remain fully supported.

---

## Analytics Engine

Current analytics collected

- Scan Timestamp
- Browser
- Operating System
- Device Type
- Device Brand
- Language
- Referrer
- Redirect Destination
- Redirect Success
- Response Time

Future analytics

- Country
- Region
- City
- Timezone
- Visitor Sessions
- Returning Visitors
- Engagement Metrics

---

## Database Layer

Platform

PostgreSQL 17.6

Hosted on

Supabase

Tables

```text
qr_codes
scan_events
```

---

# Deployment Architecture

```text
GitHub
   │
   ▼
Render
   │
   ▼
FastAPI Backend
   │
   ▼
Supabase PostgreSQL
```

QR Redirect Domain

```text
https://love-bar.kndb.stream
```

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Backend API | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Cloud Database | Supabase |
| QR Generation | qrcode + Pillow |
| User-Agent Parsing | user-agents |
| Hosting | Render |
| DNS / SSL | Cloudflare |
| Source Control | Git + GitHub |

---

# Future Architecture

```text
                   Next.js Frontend
                           │
                           ▼
                    Authentication
                           │
                           ▼
                     FastAPI Backend
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
    QR Management                   Analytics API
          │                                 │
          └────────────────┬────────────────┘
                           ▼
                PostgreSQL (Supabase)
```

---

# Current Status

Current Stable Release

**SQAnalytics Backend v1.2.0**

Current Production Components

- FastAPI Backend
- QR Generation Engine
- Human-Friendly QR URLs
- Redirect Engine
- Analytics Engine
- PostgreSQL Database
- Supabase Cloud Database
- Render Deployment
- Cloudflare Custom Domain