<p align="center">
  <img src="./main_logo.png" alt="SQAnalytics Banner" width="100%">
</p>

<h1 align="center">Google Analytics for Printed QR Codes</h1>

<p align="center">
  <b>Smart QR Analytics Platform</b><br>
  Transforming every QR scan into measurable business intelligence.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-17-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Supabase-Cloud-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase">
  <img src="https://img.shields.io/badge/Render-Production-5B5FFF?style=for-the-badge&logo=render&logoColor=white" alt="Render">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="MIT">
</p>

---

## 📖 Table of Contents

-   [Overview](#-overview)
-   [Vision](#-vision)
-   [Why SQAnalytics?](#-why-sqanalytics)
-   [Real-World Use Cases](#-real-world-use-cases)
-   [Core Features](#-core-features)
-   [Architecture](#-architecture)
-   [Technology Stack](#-technology-stack)
-   [Project Structure](#-project-structure)
-   [API Overview](#-api-overview)
-   [Quick Start](#-quick-start)
-   [Project Status & Roadmap](#-project-status--roadmap)
-   [Version History](#-version-history)
-   [Screenshots](#-screenshots)
-   [Author](#-author)
-   [License](#-license)

---

## 🌟 Overview

SQAnalytics is a full-stack analytics platform that transforms ordinary QR codes into measurable digital touchpoints.

Instead of redirecting users directly to a destination, every scan passes through an analytics layer that records engagement metrics before forwarding the visitor to the final destination.

The platform bridges the physical and digital worlds, allowing organizations to understand how printed QR codes perform across books, packaging, posters, business cards, educational material, restaurants, museums, and marketing campaigns.

---

## 🎯 Vision

> **Build the most accessible QR analytics platform for creators, educators, publishers, and businesses by turning every printed QR code into a measurable digital experience.**

---

## 🤔 Why SQAnalytics?

Traditional QR codes answer only one question:

> "Can I redirect the visitor?"

SQAnalytics answers much more:

-   🧮 How many people scanned?
-   📊 Which QR performs best?
-   🌐 Which browser was used?
-   💻 Which operating system?
-   📱 Desktop or mobile?
-   ⚡ How quickly did redirects complete?

---

## 💡 Real-World Use Cases

-   📚 **Books & Publications:** Link readers to supplementary content, author interviews, or purchase pages.
-   📦 **FMCG Product Packaging:** Provide usage instructions, promotional content, or sustainability information.
-   🎓 **Education:** Connect students to interactive learning materials, quizzes, and additional resources.
-   🏛 **Museums & Exhibitions:** Offer detailed artifact information, audio guides, and immersive experiences.
-   🍽 **Restaurants:** Enable digital menus, reservation systems, and customer feedback.
-   💼 **Business Cards:** Share portfolios, LinkedIn profiles, and company information instantly.
-   📢 **Marketing Campaigns:** Track engagement across different channels and optimize campaign performance.
-   🎤 **Events & Conferences:** Facilitate check-ins, session feedback, and networking.

---

## ✨ Core Features

| QR Platform              | Analytics                          |
| ------------------------ | ---------------------------------- |
| ✅ QR Registry           | ✅ Browser Detection               |
| ✅ Branded QR Images     | ✅ Device Detection                |
| ✅ Human-Friendly URLs   | ✅ Operating System Detection      |
| ✅ Permanent Redirects   | ✅ Response Time Tracking          |
| ✅ PNG Downloads         | ✅ Analytics REST API              |

---

## 🏗 Architecture

```text
                            Physical World
            ┌──────────────────────────────────────────┐
            | Books • Packaging • Posters • Cards      |
            └──────────────────────────────────────────┘
                                  │
                                  ▼
                             Smart QR Code
                                  │
                                  ▼
                   https://<subdomain>.kndb.stream
                                  │
                                  ▼
                        FastAPI Backend (Render)
                          ┌────────────────┐
                          │ Redirect Layer │
                          │ QR Registry    │
                          │ Analytics API  │
                          └────────────────┘
                                  │
                                  ▼
                      PostgreSQL (Supabase)
                                  │
                                  ▼
                      Next.js Dashboard (Planned)
```

---

## 🛠 Technology Stack

| Layer              | Technology               |
| ------------------ | ------------------------ |
| Backend API        | FastAPI                  |
| API Server         | Uvicorn                  |
| ORM                | SQLAlchemy               |
| Database           | PostgreSQL 17            |
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

## 📁 Project Structure

```text
SQAnalytics/
├── backend/               # FastAPI application
│   ├── app/               # Main application package
│   │   ├── models/        # SQLAlchemy models
│   │   ├── services/      # Business logic
│   │   ├── routes/        # API endpoints
│   │   └── utils/         # Helper functions
│   ├── generated_qr/      # Generated QR code images
│   ├── requirements.txt   # Python dependencies
│   └── .env.example       # Example environment variables
├── frontend/           # (Planned) Next.js application
├── docs/               # Documentation
├── assets/             # Images and assets
├── LICENSE
└── README.md          # This file
```

---

## 📌 API Overview

| Method | Endpoint                               | Description                 |
| ------ | -------------------------------------- | --------------------------- |
| GET    | `/`                                    | Home                        |
| GET    | `/health`                              | Health Check                |
| GET    | `/version`                             | API Version                 |
| GET    | `/db-test`                             | Database Test               |
| POST   | `/qr`                                  | Create QR                   |
| GET    | `/qr`                                  | List QR Codes               |
| GET    | `/r/{short_code}-{display_slug}`       | Redirect                    |
| GET    | `/analytics/summary`                   | Analytics Summary           |
| GET    | `/qr/{short_code}/generate`            | Generate QR Code Image      |
| GET    | `/qr/{short_code}/download`            | Download QR Code PNG        |

**Interactive API Documentation:** `/docs` (Swagger UI)

---

## 🚀 Quick Start

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ThilinaPerera-DataAnalytics/Fun_with_Vibe_Coding_SQAnalytics.git
    cd SQAnalytics/backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:** Create a `.env` file based on `.env.example` and fill in your credentials (e.g., database URL, secret key).

5.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The server will start at `http://127.0.0.1:8000`.

---

## 📊 Project Status & Roadmap

### ✅ Completed (Backend v1.2.0)

-   [x] Git and GitHub foundation
-   [x] FastAPI backend with REST API
-   [x] PostgreSQL database & Supabase integration
-   [x] SQLAlchemy ORM for data modeling
-   [x] QR registry, automatic generation, and branding
-   [x] QR download endpoint
-   [x] Redirect engine with analytics logging
-   [x] Browser, OS, and device detection
-   [x] Analytics summary API
-   [x] Production deployment on Render
-   [x] Cloudflare custom domain (HTTPS)
-   [x] Human-friendly QR URLs (display slug support)

### 🚧 Next Milestone (Backend v1.2.1)

-   [ ] Duplicate slug handling
-   [ ] HTTP exception improvements
-   [ ] URL helper refactoring
-   [ ] Structured logging
-   [ ] Configuration centralization

### 🚧 Future Milestones

-   **Backend v1.3:** GeoIP detection, returning visitor analytics, session tracking.
-   **Frontend v2.0:** Next.js web application, QR management portal, analytics dashboard, authentication, user management.

---

## 📜 Version History

### Backend v1.2.1 (Planned)

-   Structured Logging
-   Configuration Centralization
-   Duplicate Slug Handling
-   HTTP Exception Improvements
-   Codebase Cleanup

### Backend v1.2.0 ✅

-   Human-Friendly QR URLs
-   Display Slug Support
-   URL Slug Normalization
-   Friendly Redirect URLs
-   Improved QR Generation

### Backend v1.1.0 ✅

-   Browser, OS, and Device Detection
-   Analytics Summary API
-   Cloudflare Custom Domain
-   HTTPS

### Backend v1.0.0 ✅

-   REST API, QR Registry, Generation & Download
-   Analytics Logging
-   Production Deployment

---

## 🖼 Screenshots

*Future repository screenshots:*

-   **Swagger UI:** Interactive API documentation
-   **QR Generation:** Creating a new QR code
-   **Generated QR:** Example of a branded QR code
-   **Analytics Dashboard:** Visualizing scan data
-   **User Portal:** Managing QR codes

---

## 👨‍💻 Author

**Thilina Perera | Data with TP**

-   📌 Data Science/Data Analytics Technosavant
-   📌 Machine Learning/Deep Learning, LLM/LMM, NLP, and Data Engineering Inquisitive
-   📧 [thilina.perera@datawithtp.com](mailto:thilina.perera@datawithtp.com)
-   🔗 [LinkedIn](https://www.linkedin.com/in/thilinaperera-dataanalytics/) (Replace with actual URL)

---

## 📄 License

Released under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> **SQAnalytics is more than a QR code generator. It is a platform for measuring engagement between the physical and digital worlds, bringing web-style analytics to every printed QR code.**

<p align="center">
  Made with ❤️ by Thilina Perera
</p>
```