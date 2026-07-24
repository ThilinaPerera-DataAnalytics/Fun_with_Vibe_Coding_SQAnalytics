# SQAnalytics Technology Stack

**Current Stable Release:** Backend v1.2.0

This document summarizes the technologies currently used throughout the SQAnalytics platform.

---

# Source Control

| Technology | Purpose |
|------------|---------|
| Git | Version Control |
| GitHub | Repository Hosting & Releases |

---

# Backend

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API Framework |
| Uvicorn | ASGI Server |
| SQLAlchemy | ORM |
| Pydantic | Request & Response Validation |
| python-dotenv | Environment Variable Management |

---

# Database

| Technology | Purpose |
|------------|---------|
| PostgreSQL 17.6 | Relational Database |
| Supabase | Cloud Database Hosting |
| psycopg2 | PostgreSQL Driver |

---

# QR Generation

| Technology | Purpose |
|------------|---------|
| qrcode | QR Code Generation |
| Pillow | Image Processing |
| PNG | QR Image Output |

Features

- Automatic QR generation
- Logo embedding
- Human-friendly QR URLs
- PNG downloads

---

# Analytics

Current Analytics

- Scan Timestamp
- Browser Detection
- Operating System Detection
- Device Type Detection
- Device Brand
- Language
- Referrer
- Redirect Destination
- Redirect Success
- Response Time

Future Analytics

- Country
- Region
- City
- Timezone
- Visitor Sessions
- Returning Visitors
- Engagement Analytics

---

# Infrastructure

| Technology | Purpose |
|------------|---------|
| Render | Backend Hosting |
| Cloudflare | DNS, SSL & Custom Domain |
| Supabase | Managed PostgreSQL |

Production Domain

```text
https://love-bar.kndb.stream
```

---

# API Documentation

| Technology | Purpose |
|------------|---------|
| OpenAPI 3.1 | API Specification |
| Swagger UI | Interactive Documentation |

---

# Development Tools

| Technology | Purpose |
|------------|---------|
| Visual Studio Code | IDE |
| Python | Programming Language |
| GitHub Desktop / VS Code Source Control | Git Workflow |

---

# Current Project Structure

```text
SQAnalytics
│
├── backend
│   ├── app
│   ├── docs
│   ├── generated_qr
│   ├── icon
│   ├── migrations
│   └── requirements.txt
│
├── docs
│
├── README.md
│
└── .gitignore
```

---

# Planned Technology

## Frontend

- Next.js
- React
- Tailwind CSS

---

## Authentication

- JWT
- OAuth

---

## Analytics Dashboard

- Chart.js
- Recharts

---

## Future Integrations

- GeoIP Services
- Email Notifications
- AI Insights
- Webhooks

---

# Current Backend Version

**SQAnalytics Backend v1.2.0**