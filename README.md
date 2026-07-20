# SQAnalytics

**Smart QR Analytics Platform**

![SQAnalytics Project Logo](./main_logo.png)

SQAnalytics is a full-stack analytics platform designed to transform printed/ digital QR-code interactions into measurable digital engagement.

The platform enables QR codes to redirect users to dynamic digital content while capturing scan analytics such as scan timestamp, browser, operating system, device type and country. 

This is an end-to-end full-stack analytics engineering project demonstrating API development, cloud databases, event tracking, deployment, and analytics architecture.

---

## 1. Vision Diagrm

SQAnalytics bridges physical media and digital analytics.

```text
Printed QR Code
        ↓
https://[Sub-domain].kndb.stream/r/{short_code}
        ↓
FastAPI Backend (Render)
        ↓
Analytics Logged (Supabase)
        ↓
Redirect to Destination
        ↓
Analytics API
        ↓
Future Dashboard (Next.js)
````

The initial real-world use case is enabling printed publications to link readers to digital content while providing measurable engagement analytics.

---

## Core Capabilities

* Create and manage QR records
* Automatically generate branded QR codes
* Download QR codes as PNG images
* Redirect QR scans through permanent URLs
* Record every scan event in PostgreSQL
* Capture browser, operating system, device type, country, and timestamp
* Generate analytics summaries through REST APIs
* Support cloud-hosted redirects using a custom domain
* Production-ready backend deployed on Render

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

> `[Sub-domain].kndb.stream` is the current permanent QR redirect domain.

---

## 2. Tech Stack

| Layer              | Technology               |
| ------------------ | ------------------------ |
| Backend API        | FastAPI                  |
| API Server         | Uvicorn                  |
| ORM                | SQLAlchemy               |
| Database           | PostgreSQL  17              |
| Cloud Database     | Supabase                 |
| PostgreSQL Driver  | psycopg2                 |
| QR Generation      | Python `qrcode` + Pillow |
| User-Agent Parsing | `user-agents`            |
| Backend Hosting    | Render                   |
| DNS / SSL          | Cloudflare               |
| Source Control     | Git                      |
| Repository Hosting | GitHub                   |
| Planned Frontend   | Next.js                  |

---

## 3. Current Backend Features

### QR Management

* Create QR records through `POST /qr`
* Automatically generate unique short codes
* Automatically generate branded QR images
* Retrieve QR records through the API

<div align="center">
  <img src="branded_qr.png" width="250" />
</div>


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

Current scan analytics include:

* Scan timestamp
* Browser
* Operating system
* Device type
* User-Agent string
* Scan creation timestamp

### Analytics API

The backend currently provides analytics including:

* Total scan count
* Browser distribution
* Device distribution

---

## 4. API Endpoints

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

GET  /qr/{short_code}/download
```

Interactive API documentation is available through FastAPI Swagger UI at:

```text
/docs
```

---

## 5. Production Deployment

The SQAnalytics backend is deployed on Render and connected to a cloud-hosted PostgreSQL database hosted on Supabase.


Production API:

```text
https://sqanalytics-api.onrender.com
```

Production QR Redirect Domain:

```text
https://[Subdomain].kndb.stream
```

The custom domain allows printed QR codes to remain permanent even if the underlying hosting provider changes in the future.

---

# 6. Project Status
```
✅ Completed

* [x] Git and GitHub foundation
* [x] FastAPI backend
* [x] REST API development
* [x] PostgreSQL database
* [x] Supabase integration
* [x] SQLAlchemy ORM
* [x] QR registry
* [x] Automatic QR generation
* [x] Branded QR generation
* [x] QR download endpoint
* [x] QR redirect engine
* [x] Scan analytics logging
* [x] Browser detection
* [x] Operating system detection
* [x] Device detection
* [x] Analytics summary API
* [x] Render deployment
* [x] Cloudflare custom domain
* [x] HTTPS enabled
* [x] Production QR redirect verification

🚧 Next Milestone (Backend v1.1)

* [ ] Visitor session tracking
* [ ] Visitor identification
* [ ] Geo-location analytics
* [ ] Language detection
* [ ] Landing-page engagement analytics
* [ ] Next.js frontend
* [ ] Authentication
* [ ] Analytics dashboard
```
---

## 7. Current Development Stage

**SQAnalytics Backend v1.0 is complete and running in production.**

Current production flow

```text
Printed QR
      ↓
[Sub-domain].kndb.stream
      ↓
FastAPI (Render)
      ↓
Analytics stored in Supabase
      ↓
Redirect to destination
```
---

## 8. Roadmap
```md
Backend v1.0 ✅

- REST API
- QR Registry
- Automatic QR Generation
- Branded QR Codes
- QR Download
- Analytics Logging
- Production Deployment
- Custom Domain
- HTTPS

Backend v1.1 🚧

- Visitor Sessions
- Visitor Identification
- GeoIP Analytics
- Country / Region / City
- Language Detection
- Returning Visitors
- Advanced Analytics API

Frontend v2.0

- Next.js Web Application
- QR Management Portal
- Analytics Dashboard
- Authentication
- User Management
```
---

## Author

**Thilina Perera | Data with TP**
```
📌 Data Science/ Data Analytics D-Technosavant
📌 Machine Learning/ Deep Learning, LLM/LMM, NLP, and Data Engineering Inquisitive
``` 
