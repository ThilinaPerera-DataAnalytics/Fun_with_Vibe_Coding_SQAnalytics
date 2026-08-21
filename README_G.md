<p align="center">
  <img src="./main_logo.png" alt="SQAnalytics Banner" width="100%" />
</p>

<h1 align="center">Google Analytics for Printed QR Codes</h1>

<p align="center">
  <b>Smart QR Analytics Platform</b><br>
  <i>Transforming physical QR code scans into actionable real-time digital engagement metrics.</i>
</p>

<p align="center">
  <a href="https://github.com/ThilinaPerera-DataAnalytics/Fun_with_Vibe_Coding_SQAnalytics"><img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-17-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"></a>
  <a href="https://supabase.com/"><img src="https://img.shields.io/badge/Supabase-Cloud-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase"></a>
  <a href="https://render.com/"><img src="https://img.shields.io/badge/Render-Production-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render"></a>
  <a href="https://www.cloudflare.com/"><img src="https://img.shields.io/badge/Cloudflare-DNS%20%26%20SSL-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Cloudflare"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License"></a>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Vision](#-vision)
- [Why SQAnalytics?](#-why-sqanalytics)
- [Real-World Use Cases](#-real-world-use-cases)
- [Core Capabilities](#-core-capabilities)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [API Overview & Endpoints](#-api-overview--endpoints)
- [Production Deployment](#-production-deployment)
- [Quick Start Guide](#-quick-start-guide)
- [Detailed Roadmap & Milestones](#-detailed-roadmap--milestones)
- [Version History](#-version-history)
- [Author & Acknowledgments](#-author--acknowledgments)
- [License](#-license)

---

## 🌟 Overview

**SQAnalytics** is an enterprise-grade full-stack analytics platform engineered to transform static printed and digital QR-code interactions into measurable business intelligence.

Rather than executing a direct unmonitored redirect, every scan is routed through an asynchronous analytics collection layer. The platform instantly logs deep user engagement telemetries—including client browser, operating system, device taxonomy, response timing, and geographic indicators—before seamlessly routing the user to their target destination.

This project represents an end-to-end full-stack analytics engineering architecture demonstrating modern REST API design, cloud-native PostgreSQL databases, real-time event tracking, automated QR generation, custom domain routing, and scalable production deployment.

---

## 🎯 Vision

> **"To build the most accessible, high-performance QR analytics engine for creators, educators, publishers, and enterprises—turning every physical touchpoint into a rich, data-driven digital experience."**

---

## 💡 Why SQAnalytics?

Traditional QR codes only answer a single basic question:

❌ *"Can I redirect the visitor?"*

**SQAnalytics** powers deep observational insights:

- ✅ **How many total scans** occurred per campaign or asset?
- ✅ **Which exact physical media or QR layout** generates the highest engagement?
- ✅ **What browsers & operating systems** are being used by physical readers?
- ✅ **Is traffic arriving from mobile, tablet, or desktop** devices?
- ✅ **What is the backend latency and redirect performance** for user interactions?
- ✅ **How do dynamic display slugs** improve human context without breaking legacy QR targets?

---

## 🏢 Real-World Use Cases

- 📚 **Publishing & Print Books:** Connect readers to supplementary video lectures, audio clips, or online code repos while tracking reader drop-off across chapters.
- 📦 **FMCG & Packaging:** Track customer onboarding, digital instruction manuals, and promotional loyalty rewards directly from product packaging.
- 🎓 **Higher Education & Academics:** Measure student engagement with physical course handouts and campus bulletin boards.
- 🏛 **Museums & Exhibitions:** Analyze visitor flow and exhibit popularity using location-specific QR checkpoints.
- 🍽 **Hospitality & Menus:** Gain visibility into peak scan hours and menu interaction rates.
- 📢 **Marketing & Billboard Campaigns:** Measure exact ROI and conversion rates across different geographic ad placements.

---

## ✨ Core Capabilities

### 🔲 QR Code Lifecycle & Branding
- **Automated Generation:** Instant generation of optimized vector/raster QR codes via standard parameters.
- **Custom Branded Overlay:** Automatically inject logos and custom branding into generated QR images.
- **PNG Download Pipeline:** Dedicated API endpoints for seamless image export and integration.
- **Human-Friendly Dynamic URLs:** Support for display slugs (e.g., `/r/{short_code}-{display_slug}`) that enhance user trust and SEO readability.
- **Backward Compatibility:** Guarantees legacy QR codes without display slugs continue to resolve perfectly (`/r/{short_code}`).

### 📊 Scan Event Analytics & Telemetry
- **Low-Latency Redirect Engine:** Fast redirect handling using FastAPI and SQLAlchemy ORM.
- **Browser & OS Identification:** Automatic parsing of User-Agent strings down to browser family and operating system version.
- **Device Classification:** Categorization of scan traffic into Mobile, Tablet, and Desktop.
- **Timestamp & Latency Metrics:** High-precision automated timestamps (`created_at`) powered by native PostgreSQL default expressions.
- **Analytics Aggregation API:** Real-time metrics breakdown endpoint providing total scan counts and categorical breakdowns.

---

## 📐 System Architecture

### Physical-to-Digital Flow

```text
                  Physical World
┌────────────────────────────────────────────────────────┐
│  Books • Product Packaging • Posters • Business Cards   │
└────────────────────────────────────────────────────────┘
                           │
                           ▼
                 Smart Printed QR Code
                           │
                           ▼
          https://[subdomain].kndb.stream
                           │
                           ▼
                FastAPI Backend (Render)
      ┌──────────────────────────────────────────┐
      │  • Slug Normalization & Matcher          │
      │  • User-Agent Telemetry Extraction       │
      │  • Asynchronous Event Logger             │
      │  • Analytics API                         │
      └──────────────────────────────────────────┘
             │                            │
             ▼                            ▼
   PostgreSQL DB (Supabase)       307 HTTP Redirect
   ┌──────────────────────┐      ┌─────────────────────────┐
   │ • qr_records         │      │ YouTube / Web Content   │
   │ • scan_logs          │      │ External Destination    │
   └──────────────────────┘      └─────────────────────────┘
             │
             ▼
    Next.js Dashboard (Planned)
```

---

## 🛠 Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) | High-performance asynchronous Python API framework |
| **ASGI Server** | [Uvicorn](https://www.uvicorn.org/) | Lightning-fast async server implementation |
| **Database ORM** | [SQLAlchemy](https://www.sqlalchemy.org/) | Python SQL toolkit and Object Relational Mapper |
| **Database Engine** | [PostgreSQL 17](https://www.postgresql.org/) | Enterprise relational database |
| **Cloud Database** | [Supabase](https://supabase.com/) | Cloud PostgreSQL hosting and connection management |
| **Database Driver** | `psycopg2` / `psycopg2-binary` | PostgreSQL database adapter for Python |
| **QR Engine** | Python `qrcode` + `Pillow` | Algorithmic QR generation and image processing |
| **Agent Parser** | `user-agents` | User-agent string parsing and device identification |
| **Hosting Platform** | [Render](https://render.com/) | Production Cloud Application Hosting |
| **DNS & Security** | [Cloudflare](https://www.cloudflare.com/) | DNS routing, SSL/TLS termination, and edge caching |
| **Version Control** | Git & GitHub | Distributed version control and source code management |
| **Planned Frontend** | [Next.js](https://nextjs.org/) | React Framework for interactive user dashboard |

---

## 📁 Project Structure

```text
SQAnalytics/
├── backend/
├── assets/
│   ├── main_logo.png
│   └── branded_qr.png
├── docs/
│   └── architecture_spec.md
├── generated_qr/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🔌 API Overview & Endpoints

Interactive Swagger UI documentation is live at `/docs` when running the application.

### Endpoint Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root status health check |
| `GET` | `/health` | System health and environment ping |
| `GET` | `/version` | System build and software version response |
| `GET` | `/db-test` | Verifies active connection to Supabase PostgreSQL |
| `POST` | `/qr` | Register a new target URL and generate short code |
| `GET` | `/qr` | Retrieve paginated list of all active QR records |
| `GET` | `/r/{short_code}` | Redirect legacy QR scan and record analytics |
| `GET` | `/r/{short_code}-{display_slug}` | Human-friendly URL redirect and scan logging |
| `GET` | `/analytics/summary` | Aggregate scan analytics (total scans, device, OS, browser) |
| `GET` | `/qr/{short_code}/generate` | On-demand dynamic generation of QR image |
| `GET` | `/qr/{short_code}/download` | Direct image download endpoint for PNG assets |

---

## ☁️ Production Deployment

The SQAnalytics backend API is fully deployed and running in production.

- ⚡ **Production API Base URL:** `https://sqanalytics-api.onrender.com`
- 🌐 **Permanent QR Redirect Domain:** `https://[Sub-domain].kndb.stream`
- 📖 **Interactive OpenAPI Docs:** `https://sqanalytics-api.onrender.com/docs`

> **Note on Architecture:** Utilizing a custom, permanent sub-domain (`.kndb.stream`) for all physical QR generation ensures that all printed assets remain valid indefinitely, even if backend hosting providers change in the future.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.11+
- PostgreSQL 17 database instance (Local or Supabase)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/ThilinaPerera-DataAnalytics/Fun_with_Vibe_Coding_SQAnalytics.git
cd Fun_with_Vibe_Coding_SQAnalytics
```

### 2. Set Up Virtual Environment
```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql://<user>:<password>@<host>:5432/<dbname>
BASE_REDIRECT_URL=https://<subdomain>.kndb.stream
ENVIRONMENT=development
```

### 5. Launch the Local Server
```bash
uvicorn app.main:app --reload --port 8000
```
Access the local API documentation at `http://127.0.0.1:8000/docs`.

---

## 🗓 Detailed Roadmap & Milestones

### 🟢 Backend v1.0 — Core Foundation ✅
- [x] REST API architecture initialization
- [x] QR Registry data modeling
- [x] Automated QR image generation engine
- [x] Basic scan redirect handler
- [x] Initial Render deployment & Supabase integration

### 🟢 Backend v1.1 — Analytics & Telemetry Engine ✅
- [x] Browser family detection
- [x] Operating System identification
- [x] Device classification (Mobile / Desktop / Tablet)
- [x] Real-time analytics summary API (`/analytics/summary`)
- [x] Cloudflare SSL and DNS integration

### 🟢 Backend v1.2 — Human-Friendly URLs & Hardening ✅
- [x] Dynamic display slug routing (`/r/{short_code}-{display_slug}`)
- [x] Slug normalization and fallback algorithms
- [x] Custom branded QR generation with logo overlays
- [x] Direct image export and download endpoints (`/download`)
- [x] Automated PostgreSQL database timestamps

### 🟡 Backend v1.2.1 — Refactoring & Stability 🚧
- [ ] Duplicate slug handling logic
- [ ] Enhanced HTTP exception handling middleware
- [ ] URL Builder helper utilities
- [ ] Comprehensive test suite execution

### 🔵 Backend v1.3 — Advanced Geo & Session Analytics (Planned)
- [ ] GeoIP geolocation tracking (Country, Region, City)
- [ ] Timezone detection
- [ ] Returning visitor cohort identification
- [ ] Session duration tracking

### 🟣 Frontend v2.0 — Web Application (Planned)
- [ ] Next.js multi-tenant portal
- [ ] Interactive Power BI-style dashboard charts
- [ ] Self-service QR generator and management UI
- [ ] Role-based Access Control (RBAC) & Authentication

---

## 📜 Version History

### **Backend v1.2.1**
- **Refactored:** Structured logging formatters across backend modules.
- **Enhanced:** Production configuration centralization.
- **Added:** Full display slug support for SEO-friendly QR links.
- **Improved:** Codebase organization and production documentation.

---

## 👤 Author & Acknowledgments

**Thilina Perera**
*Data with TP*

- 📌 **Specialization:** Data Science | Data Engineering | Analytics Engineering | Business Intelligence
- 📌 **Focus:** Machine Learning, Deep Learning, LLM/LMM Applications, SQL Architecture
- 🐙 **GitHub:** [@ThilinaPerera-DataAnalytics](https://github.com/ThilinaPerera-DataAnalytics)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for complete details.

---

<p align="center">
  <b>SQAnalytics</b> • Connecting Physical Media to Digital Intelligence
</p>