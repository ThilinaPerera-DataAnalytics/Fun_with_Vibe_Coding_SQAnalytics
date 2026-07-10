# SQAnalytics

**Smart QR Analytics Platform**

![SQAnalytics Project Logo](./main_logo.png)

SQAnalytics is a full-stack analytics platform designed to transform printed QR-code interactions into measurable digital engagement.

The platform enables QR codes to redirect users to dynamic digital content while capturing scan analytics such as browser, operating system, device type, referrer, and scan timestamp.

---

## Vision

SQAnalytics bridges physical media and digital analytics.

```text
Printed QR Code
        ↓
Permanent Redirect URL
        ↓
Scan Event Captured
        ↓
Analytics Stored
        ↓
User Redirected to Digital Content
        ↓
Analytics Dashboard
````

The initial real-world use case is enabling printed publications to link readers to digital content while providing measurable engagement analytics.

---

## Core Capabilities

* Create and manage QR-code records
* Generate downloadable QR-code images
* Redirect QR scans to dynamic destination URLs
* Record every scan event in PostgreSQL
* Capture browser, operating system, device type, referrer, and timestamp
* Provide analytics through REST API endpoints
* Support cloud-hosted redirects independent of a local machine
* Prepare permanent QR infrastructure through a custom domain

---

## Current Architecture

```text
Reader / Mobile Device
          ↓
     QR Code Scan
          ↓
   [Subdomain].kndb.stream
          ↓
     FastAPI API
       (Render)
          ↓
   ┌──────┴──────┐
   ↓             ↓
Scan Event    QR Registry
   ↓             ↓
PostgreSQL / Supabase
          ↓
Destination Redirect
          ↓
YouTube / Website / Digital Content
```

> `[Subdomain].kndb.stream` is the planned permanent QR redirect domain and is currently being connected to the production backend.

---

## Tech Stack

| Layer              | Technology               |
| ------------------ | ------------------------ |
| Backend API        | FastAPI                  |
| API Server         | Uvicorn                  |
| ORM                | SQLAlchemy               |
| Database           | PostgreSQL               |
| Cloud Database     | Supabase                 |
| PostgreSQL Driver  | psycopg2                 |
| QR Generation      | Python `qrcode` + Pillow |
| User-Agent Parsing | `user-agents`            |
| Backend Hosting    | Render                   |
| DNS & Domain       | Cloudflare               |
| Source Control     | Git                      |
| Repository Hosting | GitHub                   |
| Planned Frontend   | Next.js                  |

---

## Current Backend Features

### QR Management

* Create QR records through `POST /qr`
* Automatically generate unique short codes
* Automatically generate PNG QR images
* Retrieve QR records through the API

### Redirect Engine

A QR scan reaches a redirect endpoint:

```text
/r/{short_code}
```

The backend:

1. Finds the corresponding QR record.
2. Captures the scan event.
3. Stores analytics in PostgreSQL.
4. Redirects the user to the configured destination URL.

### Scan Analytics

Each scan can capture:

* Scan timestamp
* Browser
* Operating system
* Device type
* User-agent string
* Referrer

### Analytics API

The backend currently provides analytics including:

* Total scan count
* Browser distribution
* Device distribution

---

## API Endpoints

Current major endpoints include:

```text
GET  /
GET  /health
GET  /version
GET  /db-test

POST /qr
GET  /qr

GET  /r/{short_code}

GET  /analytics/summary

GET  /qr/{short_code}/generate
```

Interactive API documentation is available through FastAPI Swagger UI at:

```text
/docs
```

---

## Production Deployment

The SQAnalytics backend is deployed on Render and connected to a cloud-hosted PostgreSQL database on Supabase.

Current production backend:

```text
https://sqanalytics-api.onrender.com
```

Planned permanent QR redirect domain:

```text
https://[Subdomain].kndb.stream
```

The custom domain allows printed QR codes to remain permanent even if the underlying hosting provider changes in the future.

---

## Project Status

### Completed

* [x] Git and GitHub foundation
* [x] FastAPI backend setup
* [x] REST API endpoints
* [x] PostgreSQL schema design
* [x] Supabase cloud database integration
* [x] SQLAlchemy ORM integration
* [x] Persistent QR registry
* [x] QR redirect engine
* [x] Scan event logging
* [x] Browser, OS, and device detection
* [x] Analytics summary API
* [x] QR PNG generation
* [x] Automatic QR generation after QR creation
* [x] Public development testing through ngrok
* [x] Production backend deployment to Render
* [x] Production database connection verified

### In Progress

* [ ] Connect `[Subdomain].kndb.stream` to production backend
* [ ] Configure and verify production HTTPS
* [ ] Test permanent QR scan → analytics → redirect flow

### Planned

* [ ] QR download endpoint
* [ ] Simple admin interface
* [ ] Analytics dashboard
* [ ] Next.js frontend
* [ ] Authentication and user management
* [ ] Advanced QR management
* [ ] Production monitoring
* [ ] Automated testing and CI/CD

---

## Current Development Stage

**Backend MVP operational and deployed.**

The immediate objective is to establish the permanent production redirect flow:

```text
Printed QR
    ↓
[Subdomain].kndb.stream
    ↓
FastAPI on Render
    ↓
Scan Recorded in Supabase
    ↓
Destination Redirect
```

Once this flow is verified, SQAnalytics will have a functional end-to-end production QR analytics pipeline.

---

## Project Purpose

SQAnalytics is both:

1. A real-world product designed for measurable QR engagement in printed publications and physical media.
2. An end-to-end full-stack analytics engineering project demonstrating API development, cloud databases, event tracking, deployment, and analytics architecture.

---

## Author

**Thilina Perera**

Data Analytics | Business Intelligence | Data Engineering | Full-Stack Analytics Projects
