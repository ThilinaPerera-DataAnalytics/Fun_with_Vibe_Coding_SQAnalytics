<p align="center">
  <img src="./main_logo.png" alt="SQAnalytics Banner" width="100%">
</p>

<h1 align="center">📊 SQAnalytics</h1>
<h3 align="center">Google Analytics for Printed QR Codes</h3>

<p align="center">
  <b>Smart QR Analytics Platform</b><br>
  Transforming every QR scan into measurable business intelligence.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-17-4169E1?logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Supabase-Cloud-3ECF8E?logo=supabase&logoColor=white">
  <img src="https://img.shields.io/badge/Render-Production-5B5FFF?logo=render&logoColor=white">
  <img src="https://img.shields.io/badge/Status-v1.2.1_Production-success">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

## 📑 Table of Contents

- [🔎 Overview](#-overview)
- [🎯 Vision](#-vision)
- [💡 Why SQAnalytics?](#-why-sqanalytics)
- [🌍 Real-World Use Cases](#-real-world-use-cases)
- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🧠 Technology Stack](#-technology-stack)
- [📁 Project Structure](#-project-structure)
- [🔌 API Overview](#-api-overview)
- [📈 Scan Analytics Captured](#-scan-analytics-captured)
- [🚀 Quick Start](#-quick-start)
- [☁️ Production Deployment](#️-production-deployment)
- [🗺️ Roadmap](#️-roadmap)
- [🕓 Version History](#-version-history)
- [🖼️ Screenshots](#️-screenshots)
- [👤 Author](#-author)
- [📄 License](#-license)

---

## 🔎 Overview

**SQAnalytics** is a full-stack analytics engineering platform that transforms ordinary QR codes into measurable digital touchpoints.

Instead of redirecting users straight to a destination, every scan passes through an **analytics layer** that logs engagement data — browser, device, OS, and timing — before forwarding the visitor onward. This project is an end-to-end demonstration of **API development, cloud database design, event tracking, and production deployment.**

> 🖨️ Print it. 📲 Scan it. 📊 Measure it.

---

## 🎯 Vision

> **Build the most accessible QR analytics platform for creators, educators, publishers, and businesses — turning every printed QR code into a measurable digital experience.**

---

## 💡 Why SQAnalytics?

A traditional QR code answers only one question:

> *"Can I redirect the visitor?"*

**SQAnalytics answers a lot more:**

| ❓ Question | 📊 Answered By |
|---|---|
| How many people scanned? | Scan count logging |
| Which QR performs best? | Analytics summary API |
| Which browser was used? | Browser detection |
| Which operating system? | OS detection |
| Desktop or mobile? | Device-type detection |
| How fast did the redirect complete? | Redirect response-time tracking |

---

## 🌍 Real-World Use Cases

| | | |
|---|---|---|
| 📚 Books & Publications | 📦 FMCG Product Packaging | 🎓 Education |
| 🏛️ Museums & Exhibitions | 🍽️ Restaurants | 💼 Business Cards |
| 📢 Marketing Campaigns | 🎤 Events & Conferences | 🖼️ Printed Media at Large |

The original real-world driver: enabling **printed publications** to link readers to digital content while capturing measurable engagement analytics.

---

## ✨ Features

### 🧩 QR Platform
- ✅ QR registry — create & manage QR records via REST API
- ✅ Human-friendly QR URLs with custom destination identifiers
- ✅ Automatic branded QR image generation (`qrcode` + Pillow)
- ✅ PNG download endpoint
- ✅ Permanent, backward-compatible redirect engine
- ✅ Display-slug support with slug normalization

### 📊 Analytics Engine
- ✅ Every scan logged to PostgreSQL
- ✅ Browser detection
- ✅ Operating system detection
- ✅ Device-type detection
- ✅ Redirect response-time tracking
- ✅ Redirect success/failure status
- ✅ Analytics summary REST API
- ✅ Automatic timestamp management (PostgreSQL defaults)

### ☁️ Platform & Ops
- ✅ Production deployment on Render
- ✅ Cloud-hosted PostgreSQL via Supabase
- ✅ Custom domain routing via Cloudflare (DNS + SSL)
- ✅ HTTPS enforced end-to-end
- ✅ Interactive Swagger docs at `/docs`

---

## 🏗️ Architecture

```text
                                  🌐 Physical World
                ┌──────────────────────────────────────────────────────────┐
                |  📚 Books  •  📦 Packaging  •  🖼️ Posters  •  💼 Cards |
                └──────────────────────────────────────────────────────────┘
                                        │
                                        ▼
                                📲 Smart QR Code
                                        │
                                        ▼
                      https://[sub-domain].kndb.stream/r/{short_code}-{slug}
                                        │
                                        ▼
                            ⚡ FastAPI Backend (Render)
                      ┌───────────────────────────────────┐
                      │   🔀 Redirect Engine              │
                      │   🗂️  QR Registry                 │
                      │   📈 Analytics API                │
                      └───────────────────────────────────┘
                                        │
                                        ▼
                            🐘 PostgreSQL (Supabase)
                                        │
                                        ▼
                            🎯 Redirect → Destination
                      (YouTube / Website / Digital Content)
                                        │
                                        ▼
                        📊 Analytics Dashboard (Next.js — Planned)
```

---

## 🧠 Technology Stack

| Layer | Technology |
|---|---|
| 🐍 Backend API | FastAPI |
| 🚀 API Server | Uvicorn |
| 🗃️ ORM | SQLAlchemy |
| 🐘 Database | PostgreSQL 17 |
| ☁️ Cloud Database | Supabase |
| 🔌 PostgreSQL Driver | psycopg2 |
| 🔲 QR Generation | Python `qrcode` + Pillow |
| 🕵️ User-Agent Parsing | `user-agents` |
| 🌐 Backend Hosting | Render |
| 🛡️ DNS / SSL | Cloudflare |
| 🗂️ Source Control | Git |
| 📦 Repository Hosting | GitHub |
| 🖥️ Planned Frontend | Next.js |

---

## 📁 Project Structure

```text
SQAnalytics/
├── backend/             ⚙️  FastAPI app, models, routes
├── frontend/            🖥️  (planned) Next.js dashboard
├── docs/                📄  Documentation
├── generated_qr/        🔲  Generated QR image assets
├── assets/              🖼️  Banners, logos, screenshots
├── LICENSE
└── README.md
```

---

## 🔌 API Overview

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Home |
| `GET` | `/health` | Health check |
| `GET` | `/version` | API version |
| `GET` | `/db-test` | Database connectivity test |
| `POST` | `/qr` | Create a QR record |
| `GET` | `/qr` | List QR records |
| `GET` | `/r/{short_code}` | Redirect (legacy, backward-compatible) |
| `GET` | `/r/{short_code}-{display_slug}` | Redirect (human-friendly) |
| `GET` | `/analytics/summary` | Analytics summary |
| `GET` | `/qr/{short_code}/generate` | Generate QR |
| `GET` | `/qr/{short_code}/download` | Download QR as PNG |

📘 Full interactive docs via **Swagger UI** → `/docs`

**Redirect examples** — both resolve to the same destination:
```
/r/19fba1ff
/r/19fba1ff-where-words-meet-music
```

---

## 📈 Scan Analytics Captured

- ⏱️ Scan timestamp
- 🌐 Browser
- 💻 Operating system
- 📱 Device type
- 🧾 Raw User-Agent string
- 🕓 Scan creation timestamp
- 🎯 Redirect destination URL
- ✅ Redirect success status
- ⚡ Redirect response time

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/ThilinaPerera-DataAnalytics/Fun_with_Vibe_Coding_SQAnalytics.git

# Move into the backend
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload
```

Once running, visit `http://localhost:8000/docs` for the interactive Swagger UI. 🎉

---

## ☁️ Production Deployment

SQAnalytics is **live in production**, running on Render and backed by a cloud-hosted PostgreSQL database on Supabase.

| Component | Address |
|---|---|
| 🔗 Production API | `https://sqanalytics-api.onrender.com` |
| 📲 QR Redirect Domain | `https://[sub-domain].kndb.stream` |

The custom domain ensures **printed QR codes remain permanent**, even if the underlying hosting provider changes in the future — a critical design decision for anything printed physically and distributed widely. 🖨️

---

## 🗺️ Roadmap

### ✅ Backend v1.0
- REST API • QR Registry • Automatic QR Generation • Branded QR Codes
- QR Download • Analytics Logging • Production Deployment • Custom Domain • HTTPS

### ✅ Backend v1.1
- Browser Detection • OS Detection • Device Detection
- Analytics Summary API • Cloudflare Custom Domain

### ✅ Backend v1.2
- Human-Friendly QR URLs • Display Slug Support • Slug Normalization
- Friendly Redirect URLs • Redirect URL API Response • Automatic DB Timestamps

### ✅ Backend v1.2.1 *(current)*
- Structured Logging • Configuration Centralization • Production Hardening
- Swagger Documentation • Codebase Cleanup

### 🚧 Backend v1.3 *(next)*
- [ ] Duplicate slug handling
- [ ] HTTP exception improvements
- [ ] URL builder helper refactor
- [ ] GeoIP country / region / city detection
- [ ] Timezone detection
- [ ] Returning-visitor analytics
- [ ] Visitor session tracking

### 🔮 Frontend v2.0 *(planned)*
- [ ] Next.js web application
- [ ] QR management portal
- [ ] Analytics dashboard
- [ ] Authentication & user management
- [ ] Organizations & subscription plans
- [ ] AI-driven insights

---

## 🕓 Version History

| Version | Highlights |
|---|---|
| **v1.0** ✅ | REST API, QR registry, automatic + branded QR generation, download, analytics logging, production deployment, custom domain, HTTPS |
| **v1.1** ✅ | Browser / OS / device detection, analytics summary API |
| **v1.2** ✅ | Human-friendly URLs, display-slug support, slug normalization, friendly redirects, auto DB timestamps |
| **v1.2.1** ✅ *(current)* | Structured logging, config centralization, production hardening, Swagger docs, codebase cleanup |

---

## 🖼️ Screenshots

> 📌 *Coming soon — to be added as the project matures:*
- Swagger UI
- QR generation flow
- Sample generated QR
- Analytics dashboard
- User portal

---

## 👤 Author

### **Thilina Perera** — *Data with TP*

  ```
📌 Data Science / Data Analytics — D-Technosavant
 📌 Machine Learning • Deep Learning • LLM/LMM • NLP • Data Engineering — Inquisitive
```
---

## 📄 License

Released under the **MIT License**.

---

<p align="center">
<i>SQAnalytics is more than a QR code generator — it's a platform for measuring engagement between the physical and digital worlds, bringing web-style analytics to every printed QR code.</i> 🌉
</p>