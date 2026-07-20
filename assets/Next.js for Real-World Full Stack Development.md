# Next.js for Real-World Full Stack Development

## A Practical Beginner Guide for Building SQAnalytics

---

# Table of Contents

1. [Why Do We Need a Frontend?](#chapter-1-why-do-we-need-a-frontend)
2. [What is React?](#chapter-2-what-is-react)
3. [What is Next.js?](#chapter-3-what-is-nextjs)
4. [Folder Structure](#chapter-4-folder-structure)
5. [Pages & Routing](#chapter-5-pages--routing)
6. [JSX](#chapter-6-jsx)
7. [Components](#chapter-7-components)
8. [Props](#chapter-8-props)
9. [State](#chapter-9-state)
10. [Forms](#chapter-10-forms)
11. [Calling FastAPI](#chapter-11-calling-fastapi)
12. [Displaying Data](#chapter-12-displaying-data)
13. [Loading States](#chapter-13-loading-states)
14. [Project Architecture](#chapter-14-project-architecture)
15. [Deployment](#chapter-15-deployment)
16. [Building SQAnalytics](#chapter-16-building-sqanalytics)

---

# Chapter 1: Why Do We Need a Frontend?

## The Problem: Swagger UI vs. Real Application

### What You Have Now (Swagger UI)

```
┌─────────────────────────────────────────┐
│           SWAGGER UI                    │
│  ┌─────────────────────────────────┐   │
│  │  GET /qr                        │   │
│  │  POST /qr                       │   │
│  │  GET /analytics/summary        │   │
│  │  DELETE /qr/{id}               │   │
│  └─────────────────────────────────┘   │
│                                         │
│  [Execute]  [Execute]  [Execute]       │
│                                         │
│  Response:                              │
│  { "data": [...], "status": 200 }      │
└─────────────────────────────────────────┘
```

**Problems:**
- ❌ Ugly and technical
- ❌ No visual design
- ❌ No user experience
- ❌ Not accessible to non-developers
- ❌ Can't share with clients

### What You Need (SQAnalytics Application)

```
┌─────────────────────────────────────────────────────┐
│  🔍 SQAnalytics                        [Login]      │
│  ┌──────────────────────────────────────────────┐   │
│  │  📊 Dashboard                               │    │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐      │  │
│  │  │Total  │ │Active │ │Scans  │ │CTR   │      │  │
│  │  │QRs: 42│ │QRs: 15│ │1,234  │ │3.2%  │      │  │
│  │  └──────┘ └──────┘ └──────┘ └──────┘      │  │
│  │                                            │  │
│  │  [+ Create QR]                            │  │
│  │                                            │  │
│  │  ┌────────────────────────────────────┐   │  │
│  │  │  QR Card 1          📱 235 scans  │   │  │
│  │  │  destination.com/page1             │   │  │
│  │  └────────────────────────────────────┘   │  │
│  │  ┌────────────────────────────────────┐   │  │
│  │  │  QR Card 2          📱 189 scans  │   │  │
│  │  │  destination.com/page2             │   │  │
│  │  └────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## The Complete SQAnalytics Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER BROWSER                          │
│  https://sqanalytics.com                                      │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      NEXT.JS FRONTEND                         │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  What Next.js Provides:                                 │ │
│  │  • User Interface (React components)                    │ │
│  │  • Routing (/create, /analytics, /settings)            │ │
│  │  • State Management (loading, data, errors)            │ │
│  │  • API Calls to FastAPI                                 │ │
│  │  • Performance Optimization                             │ │
│  │  • SEO & Meta Tags                                      │ │
│  └──────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ HTTPS / REST API
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FASTAPI BACKEND                          │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  What FastAPI Provides:                                 │ │
│  │  • Authentication (JWT)                                 │ │
│  │  • Business Logic                                       │ │
│  │  • QR Code Generation                                   │ │
│  │  • Analytics Processing                                 │ │
│  │  • API Endpoints: /qr, /analytics, /auth               │ │
│  └──────────────────────────────────────────────────────────┘ │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                        SUPABASE (PostgreSQL)                  │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Data Storage:                                          │ │
│  │  • qr_codes (id, title, destination_url, scan_count)   │ │
│  │  • users (id, email, password_hash)                    │ │
│  │  • analytics (id, qr_id, timestamp, location)          │ │
│  └──────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Why We Need Next.js

| Feature | Swagger UI | Next.js Application |
|---------|------------|---------------------|
| **Visual Design** | ❌ Technical UI | ✅ Beautiful, branded |
| **User Experience** | ❌ Clunky | ✅ Smooth, intuitive |
| **Shareability** | ❌ Developers only | ✅ Anyone can use |
| **SEO** | ❌ None | ✅ Optimized |
| **Performance** | ❌ Slow | ✅ Fast, optimized |
| **Security** | ⚠️ Basic | ✅ Advanced |
| **Mobile Ready** | ❌ No | ✅ Responsive |

---

# Chapter 2: What is React?

## React is a UI Library

React helps us build user interfaces using **components** - reusable pieces of UI.

### SQAnalytics Component Tree

```
┌──────────────────────────────────────────────────────────┐
│                     App (Root)                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │              Header Component                     │ │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐        │ │
│  │  │ Logo │  │ Nav  │  │Search│  │Profile│        │ │
│  │  └──────┘  └──────┘  └──────┘  └──────┘        │ │
│  └────────────────────────────────────────────────────┘ │
│                                                         │
│  ┌────────────────────────────────────────────────────┐ │
│  │              Sidebar Component                    │ │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐         │ │
│  │  │Dashboard│  │ Create  │  │Settings │         │ │
│  │  └─────────┘  └─────────┘  └─────────┘         │ │
│  └────────────────────────────────────────────────────┘ │
│                                                         │
│  ┌────────────────────────────────────────────────────┐ │
│  │           Analytics Cards Component               │ │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐        │ │
│  │  │Total  │  │Active │  │Scans  │  │CTR   │        │ │
│  │  │QRs: 42│  │QRs: 15│  │1,234  │  │3.2%  │        │ │
│  │  └──────┘  └──────┘  └──────┘  └──────┘        │ │
│  └────────────────────────────────────────────────────┘ │
│                                                         │
│  ┌────────────────────────────────────────────────────┐ │
│  │            QR Form Component                      │ │
│  │  ┌────────────────────────────────────────────┐  │ │
│  │  │  Title: [________________]                │  │ │
│  │  │  URL:  [________________]                │  │ │
│  │  │  [ Generate QR Code ]                    │  │ │
│  │  └────────────────────────────────────────────┘  │ │
│  └────────────────────────────────────────────────────┘ │
│                                                         │
│  ┌────────────────────────────────────────────────────┐ │
│  │             QR List Component                     │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐      │ │
│  │  │QR Card 1 │  │QR Card 2 │  │QR Card 3 │      │ │
│  │  └──────────┘  └──────────┘  └──────────┘      │ │
│  └────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

## Why React Exists

### The Problem Before React

```html
<!-- Traditional HTML - Everything is mixed together -->
<div id="app">
  <div class="header">
    <h1>SQAnalytics</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/create">Create</a>
    </nav>
  </div>
  
  <!-- Hard to update, no reusability -->
  <div class="qr-card">
    <h3>QR 1</h3>
    <p>https://example.com</p>
    <span>235 scans</span>
  </div>
  
  <!-- Copy-paste same code again -->
  <div class="qr-card">
    <h3>QR 2</h3>
    <p>https://test.com</p>
    <span>189 scans</span>
  </div>
</div>
```

### The React Solution

```jsx
// React - Components are reusable!
const App = () => {
  return (
    <div>
      <Header />
      <Sidebar />
      <AnalyticsCards data={analyticsData} />
      <QRForm />
      <QRList qrs={qrData} />
    </div>
  );
};

// Use QRCard anywhere, as many times as needed
const QRList = ({ qrs }) => {
  return (
    <div>
      {qrs.map(qr => (
        <QRCard 
          key={qr.id}
          title={qr.title}
          url={qr.destination_url}
          scans={qr.scan_count}
        />
      ))}
    </div>
  );
};
```

**Benefits of React:**
- ✅ Reusable components
- ✅ Easy to update
- ✅ Maintainable code
- ✅ Faster development
- ✅ Better user experience

---

# Chapter 3: What is Next.js?

## React + Next.js = Complete Solution

```
┌─────────────────────────────────────────────────────────────┐
│                    REACT ALONE                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  What you get:                                     │  │
│  │  • Components                                      │  │
│  │  • State management                                │  │
│  │  • Props & data flow                               │  │
│  │                                                    │  │
│  │  What's MISSING:                                   │  │
│  │  ❌ Routing (need React Router)                    │  │
│  │  ❌ Performance optimization                        │  │
│  │  ❌ SEO (bad for search engines)                   │  │
│  │  ❌ API routes (need separate server)              │  │
│  │  ❌ Deployment configuration                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                               +
┌─────────────────────────────────────────────────────────────┐
│                    NEXT.JS                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  What Next.js ADDS:                                │  │
│  │  ✅ File-based routing (app/ folder)              │  │
│  │  ✅ Automatic performance optimization             │  │
│  │  ✅ SEO built-in (meta tags, sitemaps)            │  │
│  │  ✅ API routes (backend in same project)          │  │
│  │  ✅ Easy deployment (Vercel)                       │  │
│  │  ✅ Image optimization                             │  │
│  │  ✅ Server-side rendering (SSR)                    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                               =
┌─────────────────────────────────────────────────────────────┐
│              NEXT.JS = COMPLETE SOLUTION                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Everything you need to build SQAnalytics!          │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## How Next.js Fits with FastAPI

```
┌───────────────────────────────────────────────────────────────┐
│                    COMPLETE STACK                            │
│                                                              │
│  ┌────────────────────────────────────────────────────┐      │
│  │  NEXT.JS (Frontend)                               │      │
│  │  • Serves: HTML, CSS, JavaScript                  │      │
│  │  • Port: 3000                                     │      │
│  │  • Handles: UI, routing, user interactions        │      │
│  └────────────────┬───────────────────────────────────┘      │
│                   │                                         │
│                   │ fetch() calls to API                    │
│                   │ http://localhost:8000/api/v1          │
│                   ▼                                         │
│  ┌────────────────────────────────────────────────────┐      │
│  │  FASTAPI (Backend)                                │      │
│  │  • Serves: REST API endpoints                     │      │
│  │  • Port: 8000                                     │      │
│  │  • Handles: Business logic, database queries      │      │
│  └────────────────┬───────────────────────────────────┘      │
│                   │                                         │
│                   │ SQL Queries                             │
│                   ▼                                         │
│  ┌────────────────────────────────────────────────────┐      │
│  │  SUPABASE (PostgreSQL Database)                   │      │
│  │  • Stores: QR codes, users, analytics             │      │
│  └────────────────────────────────────────────────────┘      │
└───────────────────────────────────────────────────────────────┘
```

## Development Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                   DEVELOPMENT PROCESS                       │
│                                                             │
│  1. Start FastAPI Backend                                   │
│     $ uvicorn main:app --reload                            │
│     http://localhost:8000                                   │
│                                                             │
│  2. Start Next.js Frontend                                  │
│     $ npm run dev                                          │
│     http://localhost:3000                                   │
│                                                             │
│  3. Both servers run simultaneously                        │
│     ┌─────────────────────────────────────────────────┐    │
│     │  Browser → localhost:3000 (Next.js)            │    │
│     │  Next.js → localhost:8000 (FastAPI)            │    │
│     │  FastAPI → Supabase (Database)                 │    │
│     └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 4: Folder Structure

## Real SQAnalytics Project Structure

```
sqanalytics-frontend/
│
├── app/                          # Next.js App Router (Pages)
│   ├── layout.js                # Root layout (shared across pages)
│   ├── page.js                  # Homepage (/)
│   │
│   ├── create/                  # Create QR page (/create)
│   │   └── page.js
│   │
│   ├── analytics/               # Analytics page (/analytics)
│   │   └── page.js
│   │
│   ├── settings/                # Settings page (/settings)
│   │   └── page.js
│   │
│   └── api/                     # API routes (backend in Next.js)
│       └── qr/
│           └── route.js         # API endpoint (/api/qr)
│
├── components/                   # Reusable React components
│   ├── Header.jsx
│   ├── Sidebar.jsx
│   ├── QRCard.jsx
│   ├── QRForm.jsx
│   ├── AnalyticsCard.jsx
│   ├── QRList.jsx
│   └── LoadingSpinner.jsx
│
├── lib/                          # Utilities and helpers
│   ├── api.js                   # API calls to FastAPI
│   └── constants.js
│
├── styles/                       # CSS styles
│   └── globals.css
│
├── public/                       # Static files
│   ├── logo.svg
│   └── favicon.ico
│
├── .env.local                    # Environment variables
├── next.config.js                # Next.js configuration
├── package.json                  # Dependencies
└── README.md
```

## Key Folders Explained

```
┌─────────────────────────────────────────────────────────────┐
│                    FOLDER PURPOSES                          │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  app/                                            │    │
│  │  • Contains your pages/routes                    │    │
│  │  • Each folder = a route                         │    │
│  │  • page.js = the actual page                     │    │
│  │  • layout.js = shared layout                     │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  components/                                      │    │
│  │  • Reusable UI pieces                             │    │
│  │  • Each component in its own file                 │    │
│  │  • Can be used across multiple pages             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  lib/                                             │    │
│  │  • Helper functions                               │    │
│  │  • API call functions                             │    │
│  │  • Shared utilities                               │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  public/                                          │    │
│  │  • Static assets: images, fonts, icons            │    │
│  │  • Served directly by Next.js                     │    │
│  │  • Accessible via /logo.svg                       │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## The Magic of File-Based Routing

```
┌─────────────────────────────────────────────────────────────┐
│              FILE-BASED ROUTING EXAMPLE                     │
│                                                             │
│  app/                                                       │
│  ├── page.js           →  /                                │
│  ├── create/                                                │
│  │   └── page.js       →  /create                         │
│  ├── analytics/                                             │
│  │   └── page.js       →  /analytics                      │
│  ├── settings/                                              │
│  │   └── page.js       →  /settings                       │
│  └── qr/                                                    │
│      └── [id]/                                              │
│          └── page.js    →  /qr/123                         │
│                                                             │
│  You don't need to configure routing!                      │
│  Just create files and folders.                            │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 5: Pages & Routing

## SQAnalytics Routes

```
┌─────────────────────────────────────────────────────────────┐
│                SQANALYTICS ROUTES MAP                       │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  URL: / (Home)                                    │    │
│  │  Page: Dashboard                                  │    │
│  │  Content:                                         │    │
│  │  • Analytics summary cards                       │    │
│  │  • Recent QR list                                 │    │
│  │  • Quick create button                            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  URL: /create                                     │    │
│  │  Page: Create QR                                  │    │
│  │  Content:                                         │    │
│  │  • Title input field                              │    │
│  │  • Destination URL input                          │    │
│  │  • Generate button                                │    │
│  │  • QR code preview                                │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  URL: /analytics                                  │    │
│  │  Page: Analytics Dashboard                        │    │
│  │  Content:                                         │    │
│  │  • Charts and graphs                              │    │
│  │  • Total scans                                    │    │
│  │  • QR performance metrics                         │    │
│  │  • Time filters                                   │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  URL: /settings                                   │    │
│  │  Page: Settings                                   │    │
│  │  Content:                                         │    │
│  │  • User profile                                   │    │
│  │  • API keys                                       │    │
│  │  • Theme preferences                              │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  URL: /qr/[id]                                    │    │
│  │  Page: QR Details                                 │    │
│  │  Content:                                         │    │
│  │  • QR code image                                  │    │
│  │  • Statistics                                     │    │
│  │  • Edit/Delete buttons                            │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Page Code Examples

### Homepage (/)
```jsx
// app/page.js
export default function HomePage() {
  return (
    <div>
      <h1>Welcome to SQAnalytics</h1>
      <AnalyticsSummary />
      <RecentQRList />
      <QuickActions />
    </div>
  );
}
```

### Create QR Page (/create)
```jsx
// app/create/page.js
export default function CreateQRPage() {
  return (
    <div>
      <h1>Create New QR Code</h1>
      <QRForm />
    </div>
  );
}
```

### Analytics Page (/analytics)
```jsx
// app/analytics/page.js
export default function AnalyticsPage() {
  return (
    <div>
      <h1>Analytics Dashboard</h1>
      <AnalyticsCards />
      <Charts />
      <QRPerformanceTable />
    </div>
  );
}
```

## How Routing Works

```
┌─────────────────────────────────────────────────────────────┐
│                    ROUTING FLOW                             │
│                                                             │
│  User clicks link: "Create QR"                             │
│               │                                             │
│               ▼                                             │
│  Browser navigates to: /create                             │
│               │                                             │
│               ▼                                             │
│  Next.js looks in: app/create/                             │
│               │                                             │
│               ▼                                             │
│  Finds: app/create/page.js                                │
│               │                                             │
│               ▼                                             │
│  Renders: CreateQRPage component                           │
│               │                                             │
│               ▼                                             │
│  User sees the Create QR form                              │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  ⚡ No route configuration needed!                 │    │
│  │  Just create files in the app/ folder.           │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 6: JSX

## JSX = HTML + JavaScript

```
┌─────────────────────────────────────────────────────────────┐
│                    WHAT IS JSX?                             │
│                                                             │
│  It's a syntax extension that lets you write HTML         │
│  directly inside JavaScript.                               │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  HTML is for structure                            │    │
│  │  +                                                │    │
│  │  JavaScript is for logic                          │    │
│  │  =                                                │    │
│  │  JSX is for building React components             │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## HTML vs JSX Comparison

### Regular HTML
```html
<!-- This is HTML -->
<div class="qr-card">
  <h3>My QR Code</h3>
  <p>https://example.com</p>
  <span class="scan-count">235 scans</span>
  <button onclick="handleClick()">View</button>
</div>
```

### JSX (React)
```jsx
// This is JSX - similar but with JavaScript power
const QRCard = ({ title, url, scans }) => {
  const handleClick = () => {
    console.log('QR clicked!');
  };
  
  return (
    <div className="qr-card">
      <h3>{title}</h3>
      <p>{url}</p>
      <span className="scan-count">{scans} scans</span>
      <button onClick={handleClick}>View</button>
    </div>
  );
};
```

## Key JSX Differences

```
┌─────────────────────────────────────────────────────────────┐
│              HTML vs JSX CHEAT SHEET                        │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  ATTRIBUTES                                       │    │
│  │  HTML:  class="card"                             │    │
│  │  JSX:   className="card"  ← camelCase            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  EVENTS                                           │    │
│  │  HTML:  onclick="handleClick()"                  │    │
│  │  JSX:   onClick={handleClick}   ← camelCase      │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  JAVASCRIPT IN HTML                              │    │
│  │  HTML:  Can't do this directly                    │    │
│  │  JSX:   {variable}  or  {function()}             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  SELF-CLOSING TAGS                                │    │
│  │  HTML:  <img src="...">                          │    │
│  │  JSX:   <img src="..." />  ← Always close!      │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## JSX Examples for SQAnalytics

### Example 1: Displaying Data
```jsx
// JavaScript logic
const qrTitle = "My First QR Code";
const scanCount = 235;
const isActive = true;

// JSX with embedded JavaScript
return (
  <div>
    <h3>{qrTitle}</h3>
    <p>Scans: {scanCount}</p>
    <span>Status: {isActive ? '✅ Active' : '❌ Inactive'}</span>
  </div>
);
```

### Example 2: Conditional Rendering
```jsx
const QRCard = ({ qr }) => {
  return (
    <div className="qr-card">
      <h3>{qr.title}</h3>
      {qr.scan_count > 100 ? (
        <span className="popular">🔥 Popular</span>
      ) : (
        <span className="new">✨ New</span>
      )}
    </div>
  );
};
```

### Example 3: Looping Data
```jsx
const QRList = ({ qrs }) => {
  return (
    <div className="qr-list">
      {qrs.map((qr) => (
        <QRCard 
          key={qr.id}        // Always add key for lists!
          title={qr.title}
          scans={qr.scan_count}
        />
      ))}
    </div>
  );
};
```

## SQAnalytics UI Mockup in JSX

```jsx
// app/page.js
export default function DashboardPage() {
  const [qrData, setQrData] = useState([]);
  const [loading, setLoading] = useState(true);

  return (
    <div className="dashboard">
      {/* Header */}
      <header className="header">
        <h1>📊 SQAnalytics</h1>
        <button>+ Create QR</button>
      </header>

      {/* Analytics Cards */}
      <div className="analytics-grid">
        <AnalyticsCard title="Total QRs" value={42} />
        <AnalyticsCard title="Active" value={15} />
        <AnalyticsCard title="Total Scans" value="1,234" />
        <AnalyticsCard title="CTR" value="3.2%" />
      </div>

      {/* QR List */}
      <div className="qr-list">
        {loading ? (
          <LoadingSpinner />
        ) : (
          qrData.map((qr) => (
            <QRCard 
              key={qr.id}
              title={qr.title}
              url={qr.destination_url}
              scans={qr.scan_count}
            />
          ))
        )}
      </div>
    </div>
  );
}
```

---

# Chapter 7: Components

## Components = Building Blocks of UI

```
┌─────────────────────────────────────────────────────────────┐
│                    COMPONENT ANALOGY                        │
│                                                             │
│  Think of components like LEGO bricks:                     │
│                                                             │
│  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐          │
│  │     │  │     │  │     │  │     │  │     │          │
│  │Header│  │Button│  │Card │  │Form │  │List │          │
│  │     │  │     │  │     │  │     │  │     │          │
│  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘          │
│                                                             │
│  Each piece:                                               │
│  • Has a specific purpose                                  │
│  • Can be reused anywhere                                  │
│  • Can be combined to build complex UIs                    │
│  • Is independent and self-contained                      │
└─────────────────────────────────────────────────────────────┘
```

## SQAnalytics Components

### 1. Header Component
```jsx
// components/Header.jsx
const Header = ({ user }) => {
  return (
    <header className="header">
      <div className="logo">
        <img src="/logo.svg" alt="SQAnalytics" />
        <span>SQAnalytics</span>
      </div>
      <nav className="nav">
        <a href="/">Dashboard</a>
        <a href="/create">Create</a>
        <a href="/analytics">Analytics</a>
        <a href="/settings">Settings</a>
      </nav>
      <div className="user-profile">
        <span>{user?.email || 'Guest'}</span>
        <img src={user?.avatar} alt="Avatar" />
      </div>
    </header>
  );
};
```

### 2. Sidebar Component
```jsx
// components/Sidebar.jsx
const Sidebar = () => {
  return (
    <aside className="sidebar">
      <nav>
        <ul>
          <li>📊 Dashboard</li>
          <li>➕ Create QR</li>
          <li>📈 Analytics</li>
          <li>⚙️ Settings</li>
          <li>🚪 Logout</li>
        </ul>
      </nav>
    </aside>
  );
};
```

### 3. QRCard Component
```jsx
// components/QRCard.jsx
const QRCard = ({ title, url, scans, createdAt }) => {
  return (
    <div className="qr-card">
      <div className="qr-card-header">
        <h3>{title}</h3>
        <span className="date">{createdAt}</span>
      </div>
      <div className="qr-card-body">
        <p className="url">{url}</p>
        <div className="stats">
          <span>📱 {scans} scans</span>
        </div>
      </div>
      <div className="qr-card-footer">
        <button>View Details</button>
        <button>Download</button>
      </div>
    </div>
  );
};
```

### 4. GenerateButton Component
```jsx
// components/GenerateButton.jsx
const GenerateButton = ({ onClick, loading, disabled }) => {
  return (
    <button 
      className={`btn-generate ${loading ? 'loading' : ''}`}
      onClick={onClick}
      disabled={disabled || loading}
    >
      {loading ? (
        <>
          <span className="spinner">⏳</span> Generating...
        </>
      ) : (
        '🚀 Generate QR Code'
      )}
    </button>
  );
};
```

### 5. AnalyticsCard Component
```jsx
// components/AnalyticsCard.jsx
const AnalyticsCard = ({ title, value, change, icon }) => {
  return (
    <div className="analytics-card">
      <div className="card-icon">{icon}</div>
      <div className="card-content">
        <h4>{title}</h4>
        <p className="value">{value}</p>
        {change && (
          <span className={`change ${change > 0 ? 'positive' : 'negative'}`}>
            {change > 0 ? '↑' : '↓'} {Math.abs(change)}%
          </span>
        )}
      </div>
    </div>
  );
};
```

## Parent-Child Relationships

```
┌─────────────────────────────────────────────────────────────┐
│              COMPONENT HIERARCHY                            │
│                                                             │
│                    DashboardPage (Parent)                   │
│                          │                                  │
│          ┌───────────────┼───────────────┐                 │
│          │               │               │                 │
│          ▼               ▼               ▼                 │
│      Header          Sidebar        AnalyticsGrid          │
│          │               │               │                 │
│          │               │         ┌─────┴─────┐          │
│          │               │         │           │          │
│          ▼               ▼         ▼           ▼          │
│      NavLinks        NavItems   Analytics  Analytics      │
│      UserProfile      Links      Card 1     Card 2        │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Parent Component → Contains child components     │    │
│  │  Child Component → Rendered inside parent         │    │
│  │  Sibling Components → Same level in hierarchy     │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Component Reusability

```
┌─────────────────────────────────────────────────────────────┐
│              REUSING COMPONENTS                             │
│                                                             │
│  QRCard Component (Defined once):                          │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  const QRCard = ({ title, url, scans }) => {     │    │
│  │    return <div>...</div>;                          │    │
│  │  };                                                │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  Used multiple times:                                      │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  <QRCard title="QR 1" url="https://a.com" scans=5/> │    │
│  │  <QRCard title="QR 2" url="https://b.com" scans=10/>│    │
│  │  <QRCard title="QR 3" url="https://c.com" scans=3/> │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  Benefits:                                                 │
│  ✅ Write once, use anywhere                               │
│  ✅ Consistent look and feel                               │
│  ✅ Easy to update (change one file)                      │
│  ✅ Less code to write                                    │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 8: Props

## Props = Properties = Component Inputs

```
┌─────────────────────────────────────────────────────────────┐
│                    WHAT ARE PROPS?                          │
│                                                             │
│  Props are like function parameters for components.        │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Function:                                       │    │
│  │  function greet(name) {                          │    │
│  │    return `Hello ${name}`;                       │    │
│  │  }                                                │    │
│  │  greet("Alice") → "Hello Alice"                  │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Component:                                       │    │
│  │  const QRCard = (props) => {                     │    │
│  │    return <div>{props.title}</div>;              │    │
│  │  };                                               │    │
│  │  <QRCard title="My QR" /> → Renders "My QR"      │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## SQAnalytics Prop Examples

### Example 1: QRCard Props

```jsx
// QRCard Component Definition
const QRCard = ({ title, destinationUrl, scanCount, createdAt }) => {
  return (
    <div className="qr-card">
      <h3>{title}</h3>
      <p>URL: {destinationUrl}</p>
      <p>Scans: {scanCount}</p>
      <p>Created: {createdAt}</p>
    </div>
  );
};

// Using QRCard with props
const Dashboard = () => {
  return (
    <div>
      {/* QR Card 1 */}
      <QRCard 
        title="Marketing Campaign" 
        destinationUrl="https://bit.ly/campaign" 
        scanCount={235} 
        createdAt="2024-01-15"
      />
      
      {/* QR Card 2 */}
      <QRCard 
        title="Product Page" 
        destinationUrl="https://bit.ly/product" 
        scanCount={189} 
        createdAt="2024-01-14"
      />
    </div>
  );
};
```

### Example 2: AnalyticsCard Props

```jsx
// AnalyticsCard Component
const AnalyticsCard = ({ title, value, change, icon, color }) => {
  return (
    <div className={`analytics-card ${color}`}>
      <span className="icon">{icon}</span>
      <h4>{title}</h4>
      <p className="value">{value}</p>
      <span className="change">{change > 0 ? '↑' : '↓'} {Math.abs(change)}%</span>
    </div>
  );
};

// Using AnalyticsCard with props
const AnalyticsGrid = () => {
  return (
    <div className="grid">
      <AnalyticsCard 
        title="Total QRs" 
        value={42} 
        change={12} 
        icon="📊" 
        color="blue"
      />
      <AnalyticsCard 
        title="Active QRs" 
        value={15} 
        change={-3} 
        icon="✅" 
        color="green"
      />
      <AnalyticsCard 
        title="Total Scans" 
        value="1,234" 
        change={25} 
        icon="📱" 
        color="purple"
      />
    </div>
  );
};
```

### Example 3: Passing Data from API

```jsx
// Fetch data from FastAPI
const QRList = () => {
  const [qrData, setQrData] = useState([]);
  
  // ... fetch data ...
  
  return (
    <div className="qr-list">
      {qrData.map((qr) => (
        <QRCard
          key={qr.id}                    // React needs unique key
          title={qr.title}               // From API
          destinationUrl={qr.destination_url} // From API
          scanCount={qr.scan_count}      // From API
          createdAt={qr.created_at}      // From API
        />
      ))}
    </div>
  );
};
```

## Prop Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    PROP DATA FLOW                           │
│                                                             │
│  1. Data is stored in parent component                     │
│                                                             │
│     const Dashboard = () => {                              │
│       const qr = {                                         │
│         title: "My QR",                                   │
│         scans: 235                                        │
│       };                                                  │
│       return <QRCard {...qr} />;                          │
│     };                                                     │
│                                                             │
│  2. Data flows DOWN to children via props                  │
│                                                             │
│     ┌────────────────────────────────────────────────┐    │
│     │  Parent Component                             │    │
│     │  Data: {title: "My QR", scans: 235}          │    │
│     │                    │                          │    │
│     │                    ▼ (props)                  │    │
│     │  Child Component                              │    │
│     │  Receives: title="My QR", scans=235         │    │
│     │  Renders: "My QR - 235 scans"               │    │
│     └────────────────────────────────────────────────┘    │
│                                                             │
│  3. Data flows UP via callback functions (optional)        │
│                                                             │
│     const QRCard = ({ onDelete, id }) => {                 │
│       return <button onClick={() => onDelete(id)}>Delete</button>; │
│     };                                                     │
└─────────────────────────────────────────────────────────────┘
```

## Props Cheat Sheet

```
┌─────────────────────────────────────────────────────────────┐
│                    PROPS REFERENCE                          │
│                                                             │
│  ✅ DO:                                                    │
│  • Pass data from parent to child                          │
│  • Pass callback functions to children                     │
│  • Pass configuration options                              │
│  • Pass styling variants                                   │
│  • Use descriptive prop names                              │
│                                                             │
│  ❌ DON'T:                                                 │
│  • Modify props directly (they're read-only)              │
│  • Pass unnecessary props                                  │
│  • Use props for complex logic                             │
│  • Mutate props in child components                        │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Tip: Use object destructuring for cleaner code: │    │
│  │                                                   │    │
│  │  // Good                                           │    │
│  │  const QRCard = ({ title, scans, url }) => {...} │    │
│  │                                                   │    │
│  │  // Bad                                            │    │
│  │  const QRCard = (props) => {                      │    │
│  │    return <div>{props.title}</div>;              │    │
│  │  };                                               │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 9: State

## State = Data That Changes

```
┌─────────────────────────────────────────────────────────────┐
│                    WHAT IS STATE?                           │
│                                                             │
│  State is memory for your component. It's data that       │
│  changes over time and causes the component to re-render. │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Props vs State:                                  │    │
│  │                                                   │    │
│  │  PROPS (External)     STATE (Internal)           │    │
│  │  • Passed from parent  • Managed inside          │    │
│  │  • Read-only           • Can be changed          │    │
│  │  • Don't change        • Triggers re-render     │    │
│  │  • Outside control    • Component controls       │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## The useState Hook

```
┌─────────────────────────────────────────────────────────────┐
│                    HOW useState WORKS                       │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  const [state, setState] = useState(initialValue) │    │
│  │         │         │                │              │    │
│  │         │         │                │              │    │
│  │    Current    Function        Starting           │    │
│  │    Value     to Update        Value              │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  Example:                                                   │
│  const [title, setTitle] = useState('');                   │
│  const [isLoading, setIsLoading] = useState(false);        │
│  const [qrData, setQrData] = useState([]);                │
└─────────────────────────────────────────────────────────────┘
```

## SQAnalytics State Examples

### Example 1: Typing Title (Controlled Input)

```jsx
const CreateQR = () => {
  // State for form inputs
  const [title, setTitle] = useState('');
  const [url, setUrl] = useState('');
  
  return (
    <div>
      <input 
        type="text" 
        value={title}  // Controlled by state
        onChange={(e) => setTitle(e.target.value)}  // Update state
        placeholder="Enter QR title"
      />
      <p>You typed: {title}</p>
      
      <input 
        type="url" 
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter destination URL"
      />
    </div>
  );
};
```

### Example 2: Generate Button States

```jsx
const QRGenerator = () => {
  // Multiple states for the generate flow
  const [isLoading, setIsLoading] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  const [error, setError] = useState(null);
  const [qrCode, setQrCode] = useState(null);
  
  const handleGenerate = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        body: JSON.stringify({ title, url })
      });
      const data = await response.json();
      
      setQrCode(data);  // Save the generated QR
      setIsSuccess(true);
    } catch (err) {
      setError('Failed to generate QR code');
    } finally {
      setIsLoading(false);
    }
  };
  
  return (
    <div>
      {isLoading && <LoadingSpinner />}
      {isSuccess && <SuccessMessage qr={qrCode} />}
      {error && <ErrorMessage message={error} />}
      
      <button 
        onClick={handleGenerate}
        disabled={isLoading}
      >
        Generate QR
      </button>
    </div>
  );
};
```

### Example 3: Loading QR List

```jsx
const QRList = () => {
  // State for loading data from FastAPI
  const [qrData, setQrData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    // Fetch QR codes from FastAPI
    const fetchQRs = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/v1/qr');
        const data = await response.json();
        setQrData(data);
      } catch (err) {
        setError('Failed to load QR codes');
      } finally {
        setLoading(false);
      }
    };
    
    fetchQRs();
  }, []); // Empty array = run once on mount
  
  return (
    <div>
      {loading && <div>Loading QR codes...</div>}
      {error && <div className="error">{error}</div>}
      {!loading && !error && (
        <div>
          {qrData.map(qr => (
            <QRCard key={qr.id} {...qr} />
          ))}
        </div>
      )}
    </div>
  );
};
```

## State Change Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    STATE LIFE CYCLE                         │
│                                                             │
│  1. INITIAL STATE                                           │
│     ┌──────────────────────────────────────────┐           │
│     │  isLoading = false                       │           │
│     │  data = []                               │           │
│     │  error = null                            │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   │ User clicks "Generate"                 │
│                   ▼                                         │
│  2. LOADING STATE                                           │
│     ┌──────────────────────────────────────────┐           │
│     │  isLoading = true                        │           │
│     │  data = []                               │           │
│     │  error = null                            │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   │ API call completes                    │
│                   ▼                                         │
│  3. SUCCESS/FALURE STATE                                    │
│     ┌──────────────────────────────────────────┐           │
│     │  isLoading = false                       │           │
│     │  data = [new QR, ...]                   │           │
│     │  error = null                            │           │
│     │                  OR                       │           │
│     │  isLoading = false                       │           │
│     │  data = []                               │           │
│     │  error = "Failed to generate"            │           │
│     └──────────────────────────────────────────┘           │
│                                                             │
│  ⚡ Every state change triggers a re-render!               │
└─────────────────────────────────────────────────────────────┘
```

## SQAnalytics State Examples

```
┌─────────────────────────────────────────────────────────────┐
│              STATE USE CASES IN SQANALYTICS                 │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  QR Form                                          │    │
│  │  • title: string                                 │    │
│  │  • url: string                                   │    │
│  │  • isValid: boolean                              │    │
│  │  • submitted: boolean                            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Analytics Dashboard                              │    │
│  │  • summaryData: object                           │    │
│  │  • chartData: array                              │    │
│  │  • dateRange: {start, end}                      │    │
│  │  • isLoading: boolean                            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  QR List                                          │    │
│  │  • qrs: array                                    │    │
│  │  • filter: string                                │    │
│  │  • sortBy: string                                │    │
│  │  • page: number                                  │    │
│  │  • totalPages: number                            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Settings                                         │    │
│  │  • theme: 'light' | 'dark'                      │    │
│  │  • notifications: boolean                        │    │
│  │  • apiKey: string                                │    │
│  │  • isSaving: boolean                             │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 10: Forms

## Building the Create QR Form

```
┌─────────────────────────────────────────────────────────────┐
│                    CREATE QR FORM UI                        │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  ✨ Create New QR Code                            │    │
│  │                                                   │    │
│  │  QR Title                                         │    │
│  │  [____________________________]                   │    │
│  │  Marketing Campaign 2024                         │    │
│  │                                                   │    │
│  │  Destination URL                                  │    │
│  │  [____________________________]                   │    │
│  │  https://mywebsite.com/campaign                  │    │
│  │                                                   │    │
│  │  [ 🚀 Generate QR Code ]                         │    │
│  │                                                   │    │
│  │  ┌──────────┐                                   │    │
│  │  │  QR CODE │  ✅ QR Code generated!             │    │
│  │  │  IMAGE   │  📥 Download QR                    │    │
│  │  └──────────┘                                   │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Complete Form Component

```jsx
// components/QRForm.jsx
import { useState } from 'react';

const QRForm = () => {
  // Form state
  const [formData, setFormData] = useState({
    title: '',
    destinationUrl: ''
  });
  const [isLoading, setIsLoading] = useState(false);
  const [generatedQR, setGeneratedQR] = useState(null);
  const [error, setError] = useState('');
  const [validationErrors, setValidationErrors] = useState({});

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Clear validation error when user types
    if (validationErrors[name]) {
      setValidationErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  // Validate form
  const validateForm = () => {
    const errors = {};
    
    if (!formData.title.trim()) {
      errors.title = 'Title is required';
    } else if (formData.title.length < 3) {
      errors.title = 'Title must be at least 3 characters';
    }
    
    if (!formData.destinationUrl.trim()) {
      errors.destinationUrl = 'URL is required';
    } else if (!isValidUrl(formData.destinationUrl)) {
      errors.destinationUrl = 'Please enter a valid URL';
    }
    
    setValidationErrors(errors);
    return Object.keys(errors).length === 0;
  };

  // URL validation helper
  const isValidUrl = (string) => {
    try {
      new URL(string);
      return true;
    } catch (_) {
      return false;
    }
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setIsLoading(true);
    setError('');
    setGeneratedQR(null);

    try {
      // Call FastAPI backend
      const response = await fetch('http://localhost:8000/api/v1/qr', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Failed to generate QR code');
      }

      const data = await response.json();
      setGeneratedQR(data);
      
      // Reset form on success
      setFormData({ title: '', destinationUrl: '' });
    } catch (err) {
      setError(err.message || 'Something went wrong');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="qr-form-container">
      <h2>✨ Create New QR Code</h2>
      
      <form onSubmit={handleSubmit} className="qr-form">
        {/* Title Input */}
        <div className="form-group">
          <label htmlFor="title">QR Title</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            placeholder="Enter a descriptive title"
            className={validationErrors.title ? 'error' : ''}
            disabled={isLoading}
          />
          {validationErrors.title && (
            <span className="error-message">{validationErrors.title}</span>
          )}
        </div>

        {/* URL Input */}
        <div className="form-group">
          <label htmlFor="destinationUrl">Destination URL</label>
          <input
            type="url"
            id="destinationUrl"
            name="destinationUrl"
            value={formData.destinationUrl}
            onChange={handleChange}
            placeholder="https://example.com"
            className={validationErrors.destinationUrl ? 'error' : ''}
            disabled={isLoading}
          />
          {validationErrors.destinationUrl && (
            <span className="error-message">{validationErrors.destinationUrl}</span>
          )}
        </div>

        {/* Error Message */}
        {error && (
          <div className="error-message global">
            ❌ {error}
          </div>
        )}

        {/* Submit Button */}
        <button 
          type="submit" 
          className="generate-button"
          disabled={isLoading}
        >
          {isLoading ? (
            <>
              <span className="spinner">⏳</span> Generating...
            </>
          ) : (
            '🚀 Generate QR Code'
          )}
        </button>
      </form>

      {/* Generated QR Display */}
      {generatedQR && (
        <div className="qr-result">
          <h3>✅ QR Code Generated!</h3>
          <div className="qr-image-container">
            <img 
              src={generatedQR.qr_image_url} 
              alt="Generated QR Code"
              className="qr-image"
            />
          </div>
          <button 
            className="download-button"
            onClick={() => downloadQR(generatedQR.qr_image_url)}
          >
            📥 Download QR Code
          </button>
        </div>
      )}
    </div>
  );
};

// Download helper
const downloadQR = (url) => {
  const link = document.createElement('a');
  link.href = url;
  link.download = 'qr-code.png';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

export default QRForm;
```

## Form Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    FORM FLOW                                │
│                                                             │
│  1. USER TYPES                                              │
│     ┌──────────────────────────────────────────┐           │
│     │  User enters title and URL              │           │
│     │  State updates with each keystroke      │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   ▼                                         │
│  2. VALIDATION                                              │
│     ┌──────────────────────────────────────────┐           │
│     │  Check title: Not empty, ≥3 chars       │           │
│     │  Check URL: Valid URL format            │           │
│     │  Show errors if invalid                  │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   ▼                                         │
│  3. SUBMIT                                                 │
│     ┌──────────────────────────────────────────┐           │
│     │  Button: disabled → "Generating..."     │           │
│     │  Show loading spinner                    │           │
│     │  Clear any previous errors               │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   ▼                                         │
│  4. API CALL                                                │
│     ┌──────────────────────────────────────────┐           │
│     │  POST http://localhost:8000/api/v1/qr  │           │
│     │  Body: { title, destination_url }       │           │
│     │  Wait for response                       │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   ▼                                         │
│  5. SUCCESS / ERROR                                         │
│     ┌──────────────────────────────────────────┐           │
│     │  SUCCESS:                               │           │
│     │  • Show QR code image                    │           │
│     │  • Show download button                  │           │
│     │  • Reset form                            │           │
│     │                                          │           │
│     │  ERROR:                                  │           │
│     │  • Show error message                    │           │
│     │  • Keep form data                        │           │
│     │  • Enable retry                          │           │
│     └──────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 11: Calling FastAPI

## Setting Up API Communication

```
┌─────────────────────────────────────────────────────────────┐
│              FRONTEND → BACKEND COMMUNICATION               │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  NEXT.JS (Frontend)                              │    │
│  │  http://localhost:3000                           │    │
│  └────────────────┬───────────────────────────────────┘    │
│                   │                                         │
│                   │ fetch() / axios                        │
│                   │ REST API Calls                         │
│                   │ Content-Type: application/json         │
│                   ▼                                         │
│  ┌────────────────────────────────────────────────────┐    │
│  │  FASTAPI (Backend)                               │    │
│  │  http://localhost:8000/api/v1                    │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## API Service Configuration

```jsx
// lib/api.js
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

// API client with common headers
const apiClient = async (endpoint, options = {}) => {
  const url = `${API_BASE_URL}${endpoint}`;
  
  const defaultOptions = {
    headers: {
      'Content-Type': 'application/json',
      // Add auth token if needed
      // 'Authorization': `Bearer ${token}`,
    },
  };

  const mergedOptions = {
    ...defaultOptions,
    ...options,
    headers: {
      ...defaultOptions.headers,
      ...options.headers,
    },
  };

  try {
    const response = await fetch(url, mergedOptions);
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'API request failed');
    }
    
    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export default apiClient;
```

## API Endpoints Used in SQAnalytics

```
┌─────────────────────────────────────────────────────────────┐
│              FASTAPI ENDPOINTS MAP                          │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  GET /api/v1/qr                                   │    │
│  │  → Get all QR codes                               │    │
│  │  → Used in: Dashboard, QR List                    │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  POST /api/v1/qr                                  │    │
│  │  → Create new QR code                             │    │
│  │  → Used in: Create QR Form                        │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  GET /api/v1/qr/{id}                              │    │
│  │  → Get specific QR code                           │    │
│  │  → Used in: QR Details page                       │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  GET /api/v1/analytics/summary                    │    │
│  │  → Get dashboard statistics                       │    │
│  │  → Used in: Analytics Cards                       │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  DELETE /api/v1/qr/{id}                           │    │
│  │  → Delete QR code                                 │    │
│  │  → Used in: QR Card actions                       │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Complete API Call Examples

### Example 1: GET All QR Codes

```jsx
// app/page.js
import { useEffect, useState } from 'react';
import apiClient from '@/lib/api';

const DashboardPage = () => {
  const [qrs, setQrs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchQRs = async () => {
      try {
        const data = await apiClient('/qr');
        setQrs(data);
      } catch (err) {
        setError('Failed to load QR codes');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchQRs();
  }, []);

  if (loading) return <div>Loading QR codes...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>My QR Codes</h1>
      <div className="qr-grid">
        {qrs.map(qr => (
          <QRCard key={qr.id} {...qr} />
        ))}
      </div>
    </div>
  );
};
```

### Example 2: POST Create New QR

```jsx
// app/create/page.js
import { useState } from 'react';
import apiClient from '@/lib/api';

const CreateQRPage = () => {
  const [formData, setFormData] = useState({
    title: '',
    destination_url: ''
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await apiClient('/qr', {
        method: 'POST',
        body: JSON.stringify(formData),
      });
      
      setResult(response);
      setFormData({ title: '', destination_url: '' });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Create QR Code</h1>
      
      {error && <div className="error">{error}</div>}
      
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="QR Title"
          value={formData.title}
          onChange={(e) => setFormData({
            ...formData,
            title: e.target.value
          })}
          required
        />
        
        <input
          type="url"
          placeholder="Destination URL"
          value={formData.destination_url}
          onChange={(e) => setFormData({
            ...formData,
            destination_url: e.target.value
          })}
          required
        />
        
        <button type="submit" disabled={loading}>
          {loading ? 'Creating...' : 'Create QR'}
        </button>
      </form>

      {result && (
        <div className="success">
          <h3>QR Code Created!</h3>
          <img src={result.qr_image_url} alt="QR Code" />
          <button onClick={() => window.location.href = `/qr/${result.id}`}>
            View Details
          </button>
        </div>
      )}
    </div>
  );
};
```

### Example 3: GET Analytics Summary

```jsx
// components/AnalyticsDashboard.jsx
import { useEffect, useState } from 'react';
import apiClient from '@/lib/api';

const AnalyticsDashboard = () => {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const data = await apiClient('/analytics/summary');
        setSummary(data);
      } catch (error) {
        console.error('Failed to fetch analytics:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchSummary();
  }, []);

  if (loading) return <AnalyticsSkeleton />;
  if (!summary) return <div>No data available</div>;

  return (
    <div className="analytics-grid">
      <AnalyticsCard
        title="Total QRs"
        value={summary.total_qrs}
        icon="📊"
      />
      <AnalyticsCard
        title="Active QRs"
        value={summary.active_qrs}
        icon="✅"
      />
      <AnalyticsCard
        title="Total Scans"
        value={summary.total_scans}
        icon="📱"
      />
      <AnalyticsCard
        title="Click-Through Rate"
        value={`${summary.ctr}%`}
        icon="🎯"
      />
    </div>
  );
};
```

## Request-Response Flow

```
┌─────────────────────────────────────────────────────────────┐
│              REQUEST-RESPONSE SEQUENCE                      │
│                                                             │
│  User                                                       │
│   │                                                         │
│   │ 1. Clicks "Generate QR"                                │
│   ▼                                                         │
│  Next.js Frontend                                          │
│   │                                                         │
│   │ 2. Creates request:                                    │
│   │    POST /api/v1/qr                                    │
│   │    Body: { title: "My QR", destination_url: "..." }   │
│   │    Headers: { Content-Type: "application/json" }      │
│   ▼                                                         │
│  FastAPI Backend                                           │
│   │                                                         │
│   │ 3. Validates request                                   │
│   │ 4. Generates QR code                                   │
│   │ 5. Saves to database                                   │
│   │ 6. Creates response:                                  │
│   │    Status: 200 OK                                     │
│   │    Body: { id: 42, title: "My QR", qr_image_url: ...}│
│   ▼                                                         │
│  Next.js Frontend                                          │
│   │                                                         │
│   │ 7. Receives response                                   │
│   │ 8. Updates state with new QR                          │
│   │ 9. Renders QR code image                              │
│   │ 10. Shows success message                              │
│   ▼                                                         │
│  User                                                       │
│   │                                                         │
│   │ 11. Sees generated QR code                             │
│   │ 12. Can download or share                              │
│   └                                                         │
│                                                             │
│  ⚡ Full round trip: ~200-500ms                           │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 12: Displaying Data

## Dynamic Data Display Patterns

### Pattern 1: QR Cards Grid

```jsx
// components/QRGrid.jsx
const QRGrid = ({ qrs }) => {
  if (!qrs || qrs.length === 0) {
    return (
      <div className="empty-state">
        <p>No QR codes yet</p>
        <a href="/create">Create your first QR code →</a>
      </div>
    );
  }

  return (
    <div className="qr-grid">
      {qrs.map((qr) => (
        <QRCard
          key={qr.id}
          id={qr.id}
          title={qr.title}
          destinationUrl={qr.destination_url}
          scanCount={qr.scan_count}
          createdAt={new Date(qr.created_at).toLocaleDateString()}
        />
      ))}
    </div>
  );
};

// In the page
const Dashboard = () => {
  const [qrData, setQrData] = useState([]);
  
  // ... fetch data ...
  
  return (
    <div className="dashboard">
      <h2>Your QR Codes</h2>
      <QRGrid qrs={qrData} />
    </div>
  );
};
```

### Pattern 2: Analytics Cards

```jsx
// components/AnalyticsGrid.jsx
const AnalyticsGrid = ({ summaryData }) => {
  const cards = [
    {
      title: 'Total QRs',
      value: summaryData.total_qrs,
      icon: '📊',
      color: '#4F46E5'
    },
    {
      title: 'Active QRs',
      value: summaryData.active_qrs,
      icon: '✅',
      color: '#059669'
    },
    {
      title: 'Total Scans',
      value: summaryData.total_scans.toLocaleString(),
      icon: '📱',
      color: '#D946EF'
    },
    {
      title: 'Click-Through Rate',
      value: `${summaryData.ctr}%`,
      icon: '🎯',
      color: '#F59E0B'
    }
  ];

  return (
    <div className="analytics-grid">
      {cards.map((card, index) => (
        <AnalyticsCard
          key={index}
          title={card.title}
          value={card.value}
          icon={card.icon}
          color={card.color}
        />
      ))}
    </div>
  );
};
```

### Pattern 3: QR List Table

```jsx
// components/QRTable.jsx
const QRTable = ({ qrs }) => {
  return (
    <table className="qr-table">
      <thead>
        <tr>
          <th>Title</th>
          <th>Destination URL</th>
          <th>Scans</th>
          <th>Created</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {qrs.map((qr) => (
          <tr key={qr.id}>
            <td>{qr.title}</td>
            <td>
              <a href={qr.destination_url} target="_blank" rel="noopener noreferrer">
                {qr.destination_url}
              </a>
            </td>
            <td>{qr.scan_count}</td>
            <td>{new Date(qr.created_at).toLocaleDateString()}</td>
            <td>
              <button onClick={() => handleView(qr.id)}>View</button>
              <button onClick={() => handleDelete(qr.id)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

### Pattern 4: Charts with Data

```jsx
// components/QRChart.jsx
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const QRChart = ({ scanData }) => {
  // scanData: [{ date: '2024-01-01', scans: 45 }, ...]
  
  return (
    <div className="chart-container">
      <h3>Daily Scans</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={scanData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="scans" stroke="#4F46E5" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};
```

## Data Processing Before Display

```jsx
// lib/data-processing.js
export const processQRData = (rawData) => {
  if (!rawData) return [];
  
  return rawData.map(qr => ({
    id: qr.id,
    title: qr.title,
    destinationUrl: qr.destination_url,
    scanCount: qr.scan_count,
    // Format date
    createdAt: new Date(qr.created_at).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    }),
    // Add derived data
    isPopular: qr.scan_count > 100,
    shortUrl: qr.destination_url.length > 30 
      ? qr.destination_url.substring(0, 30) + '...' 
      : qr.destination_url
  }));
};

// Use in component
const QRList = () => {
  const [qrs, setQrs] = useState([]);
  
  useEffect(() => {
    fetchQRs().then(rawData => {
      const processedData = processQRData(rawData);
      setQrs(processedData);
    });
  }, []);
  
  return (
    <div>
      {qrs.map(qr => (
        <QRCard 
          key={qr.id}
          title={qr.title}
          url={qr.shortUrl}  // Truncated URL
          scans={qr.scanCount}
          isPopular={qr.isPopular}
        />
      ))}
    </div>
  );
};
```

## Data Visualization Flow

```
┌─────────────────────────────────────────────────────────────┐
│              DATA FLOW PIPELINE                             │
│                                                             │
│  1. FETCH RAW DATA                                          │
│     ┌──────────────────────────────────────────┐           │
│     │  GET /api/v1/qr                          │           │
│     │  Response: [{ id: 1, title: "QR 1", ... }]│         │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   ▼                                         │
│  2. PROCESS DATA                                            │
│     ┌──────────────────────────────────────────┐           │
│     │  • Format dates                         │           │
│     │  • Truncate long text                   │           │
│     │  • Calculate derived values             │           │
│     │  • Filter/sort data                     │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   ▼                                         │
│  3. STORE IN STATE                                          │
│     ┌──────────────────────────────────────────┐           │
│     │  const [displayData, setDisplayData] =  │           │
│     │    useState(processedData);              │           │
│     └──────────────────────────────────────────┘           │
│                   │                                         │
│                   ▼                                         │
│  4. RENDER UI                                               │
│     ┌──────────────────────────────────────────┐           │
│     │  displayData.map(qr => (                │           │
│     │    <QRCard ... />                        │           │
│     │  ))                                      │           │
│     └──────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────┘
```

---

# Chapter 13: Loading States

## Loading State Management

```
┌─────────────────────────────────────────────────────────────┐
│              LOADING STATE LIFE CYCLE                       │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  IDLE                                            │    │
│  │  • Initial state before any action              │    │
│  │  • Show empty or default content                │    │
│  └────────────────────────────────────────────────────┘    │
│                   │                                         │
│                   ▼                                         │
│  ┌────────────────────────────────────────────────────┐    │
│  │  LOADING                                         │    │
│  │  • Action in progress                            │    │
│  │  • Show loading indicators                       │    │
│  │  • Disable interactions                           │    │
│  └────────────────────────────────────────────────────┘    │
│                   │                                         │
│          ┌────────┴────────┐                               │
│          ▼                 ▼                               │
│  ┌──────────────┐  ┌──────────────┐                      │
│  │   SUCCESS    │  │   ERROR      │                      │
│  │  • Show data │  │  • Show error│                      │
│  │  • Reset UI  │  │  • Enable    │                      │
│  │              │  │    retry     │                      │
│  └──────────────┘  └──────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

## Complete Loading Component

```jsx
// components/QRGenerator.jsx
import { useState } from 'react';
import LoadingSpinner from './LoadingSpinner';
import SkeletonLoader from './SkeletonLoader';

const QRGenerator = () => {
  // State management
  const [state, setState] = useState({
    status: 'idle', // 'idle' | 'loading' | 'success' | 'error'
    data: null,
    error: null
  });

  const handleGenerate = async (formData) => {
    // Set loading state
    setState({ status: 'loading', data: null, error: null });
    
    try {
      const response = await fetch('/api/v1/qr', {
        method: 'POST',
        body: JSON.stringify(formData)
      });
      
      if (!response.ok) throw new Error('Generation failed');
      
      const data = await response.json();
      setState({ status: 'success', data, error: null });
    } catch (error) {
      setState({ status: 'error', data: null, error: error.message });
    }
  };

  // Render based on state
  const renderContent = () => {
    switch (state.status) {
      case 'idle':
        return <QRForm onGenerate={handleGenerate} />;
        
      case 'loading':
        return (
          <div className="loading-container">
            <LoadingSpinner />
            <p>Generating your QR code...</p>
          </div>
        );
        
      case 'success':
        return (
          <div className="success-container">
            <h3>✅ QR Code Generated!</h3>
            <QRDisplay data={state.data} />
            <button onClick={() => setState({ status: 'idle', data: null, error: null })}>
              Create Another
            </button>
          </div>
        );
        
      case 'error':
        return (
          <div className="error-container">
            <h3>❌ Something went wrong</h3>
            <p>{state.error}</p>
            <button onClick={() => setState({ status: 'idle', data: null, error: null })}>
              Try Again
            </button>
          </div>
        );
        
      default:
        return null;
    }
  };

  return (
    <div className="qr-generator">
      {renderContent()}
    </div>
  );
};
```

## Skeleton Loading

```jsx
// components/SkeletonLoader.jsx
const SkeletonLoader = () => {
  return (
    <div className="skeleton-container">
      <div className="skeleton-header">
        <div className="skeleton-title"></div>
        <div className="skeleton-subtitle"></div>
      </div>
      
      <div className="skeleton-grid">
        <div className="skeleton-card"></div>
        <div className="skeleton-card"></div>
        <div className="skeleton-card"></div>
        <div className="skeleton-card"></div>
      </div>
    </div>
  );
};

// CSS for skeleton animation
// .skeleton-card {
//   height: 150px;
//   background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
//   background-size: 200% 100%;
//   animation: shimmer 1.5s infinite;
// }
//
// @keyframes shimmer {
//   0% { background-position: -200% 0; }
//   100% { background-position: 200% 0; }
// }
```

## Loading State UI Examples

```
┌─────────────────────────────────────────────────────────────┐
│              LOADING UI PATTERNS                            │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  SPINNER LOADING                                  │    │
│  │  ┌──────┐                                        │    │
│  │  │  ⭕  │  Loading QR codes...                    │    │
│  │  └──────┘                                        │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  SKELETON LOADING                                 │    │
│  │  ████████████████                                │    │
│  │  ████████████████                                │    │
│  │  ████████████████                                │    │
│  │  ████████████████                                │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  PROGRESS BAR LOADING                             │    │
│  │  [████████░░░░░░░░] 60%                          │    │
│  │  Generating QR code...                            │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  SUCCESS STATE                                    │    │
│  │  ✅ QR Code Generated!                           │    │
│  │  ┌──────────┐                                    │    │
│  │  │ QR CODE  │                                    │    │
│  │  │  IMAGE   │                                    │    │
│  │  └──────────┘                                    │    │
│  │  [Download] [Share] [Create Another]              │    │
│  └────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  ERROR STATE                                      │    │
│  │  ❌ Failed to generate QR                         │    │
│  │  "Network timeout"                               │    │
│  │  [Try Again]                                      │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Optimistic UI Pattern

```jsx
// Optimistic update - UI updates before API confirms
const QRList = () => {
  const [qrs, setQrs] = useState([]);
  const [deletingId, setDeletingId] = useState(null);

  const handleDelete = async (id) => {
    // Optimistic update: remove immediately
    setQrs(prev => prev.filter(qr => qr.id !== id));
    setDeletingId(id);
    
    try {
      await fetch(`/api/v1/qr/${id}`, { method: 'DELETE' });
    } catch (error) {
      // Rollback on error
      const originalData = await fetch('/api/v1/qr');
      const data = await originalData.json();
      setQrs(data);
    } finally {
      setDeletingId(null);
    }
  };

  return (
    <div>
      {qrs.map(qr => (
        <QRCard
          key={qr.id}
          {...qr}
          onDelete={() => handleDelete(qr.id)}
          isDeleting={deletingId === qr.id}
        />
      ))}
    </div>
  );
};
```

---

# Chapter 14: Project Architecture

## Complete SQAnalytics Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     SQANALYTICS ARCHITECTURE                           │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  USER BROWSER                                                  │  │
│  │  • User interacts with the UI                                  │  │
│  │  • Renders HTML/CSS/JS from Next.js                           │  │
│  │  • Sends HTTP requests to Next.js                             │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  NEXT.JS APPLICATION (Frontend)                                │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Components Layer                                        │ │  │
│  │  │  • Pages: Dashboard, Create, Analytics, Settings        │ │  │
│  │  │  • Reusable: QRCard, AnalyticsCard, Form, Button       │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  State Management                                        │ │  │
│  │  │  • useState for component-level state                   │ │  │
│  │  │  • useEffect for side effects                           │ │  │
│  │  │  • Props for parent-child communication                  │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  API Client                                              │ │  │
│  │  │  • fetch() calls to FastAPI                             │ │  │
│  │  │  • Error handling                                       │ │  │
│  │  │  • Authentication headers                               │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           │ HTTP/REST API Calls                      │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  FASTAPI BACKEND                                               │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Routes/Endpoints                                        │ │  │
│  │  │  • GET /qr - Get all QR codes                           │ │  │
│  │  │  • POST /qr - Create new QR code                        │ │  │
│  │  │  • GET /qr/{id} - Get specific QR                       │ │  │
│  │  │  • DELETE /qr/{id} - Delete QR                          │ │  │
│  │  │  • GET /analytics/summary - Get statistics              │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Business Logic                                          │ │  │
│  │  │  • QR code generation                                   │ │  │
│  │  │  • Analytics processing                                 │ │  │
│  │  │  • Authentication                                       │ │  │
│  │  │  • Validation                                          │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           │ SQL Queries                              │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  SUPABASE (PostgreSQL Database)                               │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Tables                                                 │ │  │
│  │  │  • qr_codes: id, title, destination_url, scan_count    │ │  │
│  │  │  • users: id, email, password_hash                     │ │  │
│  │  │  • analytics: id, qr_id, timestamp, location          │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  ANALYTICS ENGINE                                              │  │
│  │  • Track QR code scans                                         │  │
│  │  • Aggregates metrics                                          │  │
│  │  • Generates reports                                           │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Layer Responsibilities

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    LAYER RESPONSIBILITIES                               │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  BROWSER LAYER                                                │  │
│  │  • Renders HTML/CSS/JS                                        │  │
│  │  • Handles user input (click, type, scroll)                  │  │
│  │  • Displays UI updates                                        │  │
│  │  • Sends requests to Next.js                                 │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  FRONTEND LAYER (Next.js)                                     │  │
│  │  • Serves the application                                     │  │
│  │  • Manages UI state                                           │  │
│  │  • Handles routing                                           │  │
│  │  • Communicates with FastAPI                                  │  │
│  │  • Transforms data for display                                │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  BACKEND LAYER (FastAPI)                                      │  │
│  │  • Business logic                                             │  │
│  │  • QR generation logic                                        │  │
│  │  • User authentication                                        │  │
│  │  • Data validation                                            │  │
│  │  • Database operations                                        │  │
│  │  • Analytics calculation                                      │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  DATABASE LAYER (Supabase)                                    │  │
│  │  • Stores QR data                                            │  │
│  │  • Stores user data                                          │  │
│  │  • Stores analytics data                                     │  │
│  │  • Handles database queries                                   │  │
│  │  • Data persistence                                          │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  ANALYTICS LAYER                                               │  │
│  │  • Processes scan events                                       │  │
│  │  • Aggregates metrics                                         │  │
│  │  • Generates insights                                         │  │
│  │  • Provides reporting data                                    │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DATA FLOW SEQUENCE                                  │
│                                                                         │
│  1. User creates QR                                                    │
│     ┌─────────────┐                                                    │
│     │  USER       │                                                    │
│     │  Clicks     │                                                    │
│     │  Generate   │                                                    │
│     └──────┬──────┘                                                    │
│            │                                                           │
│            ▼                                                           │
│  2. Frontend sends data                                                │
│     ┌────────────────────────────────┐                               │
│     │  NEXT.JS                      │                               │
│     │  POST /api/v1/qr             │                               │
│     │  { title: "My QR", url: "..." }│                             │
│     └──────────────┬─────────────────┘                               │
│                    │                                                  │
│                    ▼                                                  │
│  3. Backend processes                                                │
│     ┌────────────────────────────────┐                               │
│     │  FASTAPI                      │                               │
│     │  • Validates input            │                               │
│     │  • Generates QR code          │                               │
│     │  • Creates short URL          │                               │
│     └──────────────┬─────────────────┘                               │
│                    │                                                  │
│                    ▼                                                  │
│  4. Database stores                                                  │
│     ┌────────────────────────────────┐                               │
│     │  SUPABASE                     │                               │
│     │  INSERT INTO qr_codes         │                               │
│     │  VALUES (title, url, ...)    │                               │
│     └──────────────┬─────────────────┘                               │
│                    │                                                  │
│                    ▼                                                  │
│  5. Backend responds                                                 │
│     ┌────────────────────────────────┐                               │
│     │  FASTAPI                      │                               │
│     │  200 OK                       │                               │
│     │  { id: 123, qr_image: "..." }│                               │
│     └──────────────┬─────────────────┘                               │
│                    │                                                  │
│                    ▼                                                  │
│  6. Frontend displays                                                │
│     ┌────────────────────────────────┐                               │
│     │  NEXT.JS                      │                               │
│     │  • Updates state              │                               │
│     │  • Renders QR image           │                               │
│     │  • Shows success message      │                               │
│     └──────────────┬─────────────────┘                               │
│                    │                                                  │
│                    ▼                                                  │
│  7. User sees result                                                 │
│     ┌────────────────────────────────┐                               │
│     │  USER                         │                               │
│     │  Sees generated QR code       │                               │
│     │  Can download or share        │                               │
│     └────────────────────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# Chapter 15: Deployment

## Complete Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PRODUCTION DEPLOYMENT                               │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  GITHUB (Source Control)                                       │  │
│  │  • Code repository                                            │  │
│  │  • Version control                                            │  │
│  │  • Triggers CI/CD pipelines                                   │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           │ Git Push                                 │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  VERCEL (Frontend Hosting)                                     │  │
│  │  • Builds Next.js application                                  │  │
│  │  • Deploys to CDN                                             │  │
│  │  • Provides SSL certificates                                  │  │
│  │  • Auto-scaling                                              │  │
│  │  • URL: https://sqanalytics.vercel.app                       │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           │ API Calls                                 │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  RENDER (Backend Hosting)                                      │  │
│  │  • Hosts FastAPI server                                       │  │
│  │  • Provides SSL certificates                                  │  │
│  │  • Environment variables                                      │  │
│  │  • Auto-restart on crash                                     │  │
│  │  • URL: https://sqanalytics-api.onrender.com                 │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           │ Database Connection                      │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  SUPABASE (Database Hosting)                                   │  │
│  │  • Hosted PostgreSQL                                          │  │
│  │  • Row-level security                                         │  │
│  │  • Authentication                                              │  │
│  │  • Real-time subscriptions                                     │  │
│  │  • Auto-backups                                               │  │
│  └────────────────────────┬────────────────────────────────────────┘  │
│                           │                                           │
│                           │ Content Delivery                          │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  CLOUDFLARE (CDN & DNS)                                        │  │
│  │  • DNS management                                              │  │
│  │  • Global CDN                                                 │  │
│  │  • DDoS protection                                            │  │
│  │  • SSL/TLS termination                                        │  │
│  │  • Custom domain: https://sqanalytics.com                     │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Environment Variables

```bash
# .env.local (Frontend)
NEXT_PUBLIC_API_URL=https://sqanalytics-api.onrender.com/api/v1
NEXT_PUBLIC_SITE_URL=https://sqanalytics.vercel.app
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key

# .env (Backend - FastAPI)
DATABASE_URL=postgresql://user:password@host:5432/db
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_KEY=your-service-key
JWT_SECRET=your-secret-key
```

## Deployment Steps

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT STEPS                                     │
│                                                                         │
│  1. Push code to GitHub                                                │
│     ┌────────────────────────────────────────────────────────────┐    │
│     │  $ git add .                                              │    │
│     │  $ git commit -m "Deploy to production"                  │    │
│     │  $ git push origin main                                  │    │
│     └────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  2. Vercel auto-deploys frontend                                       │
│     ┌────────────────────────────────────────────────────────────┐    │
│     │  • Vercel detects changes                                  │    │
│     │  • Installs dependencies                                   │    │
│     │  • Builds application                                      │    │
│     │  • Deploys to CDN                                          │    │
│     │  • Allocates preview URL                                   │    │
│     └────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  3. Render auto-deploys backend                                        │
│     ┌────────────────────────────────────────────────────────────┐    │
│     │  • Render detects changes                                  │    │
│     │  • Installs dependencies                                   │    │
│     │  • Starts FastAPI server                                  │    │
│     │  • Health check endpoint                                   │    │
│     └────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  4. Supabase manages database                                         │
│     ┌────────────────────────────────────────────────────────────┐    │
│     │  • Runs migrations                                          │    │
│     │  • Updates schema                                           │    │
│     │  • Maintains backups                                       │    │
│     └────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  5. Cloudflare resolves DNS                                            │
│     ┌────────────────────────────────────────────────────────────┐    │
│     │  • Routes traffic to correct services                     │    │
│     │  • Handles SSL                                             │    │
│     │  • Optimizes delivery                                      │    │
│     └────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
```

## Security Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SECURITY CONFIGURATION                              │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  FRONTEND (Next.js)                                            │  │
│  │  • CORS configuration                                          │  │
│  │  • Environment variables (NOT in code)                        │  │
│  │  • HTTPS only                                                 │  │
│  │  • XSS protection                                             │  │
│  │  • Content Security Policy                                     │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  BACKEND (FastAPI)                                             │  │
│  │  • JWT Authentication                                          │  │
│  │  • Rate limiting                                               │  │
│  │  • Input validation                                           │  │
│  │  • SQL injection prevention                                   │  │
│  │  • CORS configuration                                         │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  DATABASE (Supabase)                                           │  │
│  │  • Row Level Security (RLS)                                   │  │
│  │  • Encrypted connections                                      │  │
│  │  • Strong passwords                                           │  │
│  │  • Regular backups                                           │  │
│  │  • Least privilege access                                    │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# Chapter 16: Building SQAnalytics

## Development Roadmap

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SQANALYTICS BUILD ROADMAP                           │
│                                                                         ││  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  PHASE 1: Landing Page                                        │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Goals:                                                   │ │  │
│  │  │  ✓ Create homepage with hero section                    │ │  │
│  │  │  ✓ Add navigation                                        │ │  │
│  │  │  ✓ Design responsive layout                              │ │  │
│  │  │  ✓ Add call-to-action buttons                           │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  PHASE 2: QR Generator                                        │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Goals:                                                   │ │  │
│  │  │  ✓ Create form (title, URL)                              │ │  │
│  │  │  ✓ Connect to FastAPI                                    │ │  │
│  │  │  ✓ Display generated QR code                             │ │  │
│  │  │  ✓ Handle loading/error states                           │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  PHASE 3: QR Download                                         │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Goals:                                                   │ │  │
│  │  │  ✓ Add download button                                   │ │  │
│  │  │  ✓ Implement QR code download                            │ │  │
│  │  │  ✓ Support multiple formats (PNG, SVG)                  │ │  │
│  │  │  ✓ Add share functionality                               │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  PHASE 4: QR List                                             │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Goals:                                                   │ │  │
│  │  │  ✓ Fetch all QR codes                                    │ │  │
│  │  │  ✓ Display in grid layout                                │ │  │
│  │  │  ✓ Add search/filter functionality                        │ │  │
│  │  │  ✓ Implement pagination                                  │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  PHASE 5: Analytics Dashboard                                 │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Goals:                                                   │ │  │
│  │  │  ✓ Display summary cards                                 │ │  │
│  │  │  ✓ Add charts (line, bar, pie)                          │ │  │
│  │  │  ✓ Show QR performance metrics                           │ │  │
│  │  │  ✓ Implement date filtering                              │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  PHASE 6: Authentication                                      │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Goals:                                                   │ │  │
│  │  │  ✓ Implement signup page                                 │ │  │
│  │  │  ✓ Implement login page                                  │ │  │
│  │  │  ✓ Add JWT token management                              │ │  │
│  │  │  ✓ Protected routes                                      │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                           │                                           │
│                           ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  PHASE 7: Admin Portal                                        │  │
│  │  ┌──────────────────────────────────────────────────────────┐ │  │
│  │  │  Goals:                                                   │ │  │
│  │  │  ✓ User management                                       │ │  │
│  │  │  ✓ QR code moderation                                    │ │  │
│  │  │  ✓ System analytics                                      │ │  │
│  │  │  ✓ Settings & configuration                              │ │  │
│  │  └──────────────────────────────────────────────────────────┘ │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Technology Stack

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    TECHNOLOGY STACK SUMMARY                            │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  FRONTEND                                                      │  │
│  │  • Framework: Next.js 14+                                     │  │
│  │  • Language: JavaScript/JSX                                   │  │
│  │  • Styling: CSS Modules / Tailwind CSS                        │  │
│  │  • State: React hooks (useState, useEffect)                  │  │
│  │  • HTTP: fetch() API                                          │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  BACKEND                                                       │  │
│  │  • Framework: FastAPI                                         │  │
│  │  • Language: Python 3.10+                                     │  │
│  │  • Database: Supabase (PostgreSQL)                            │  │
│  │  • ORM: SQLAlchemy                                            │  │
│  │  • Auth: JWT                                                  │  │
│  │  • QR: qrcode library                                         │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │  DEPLOYMENT                                                    │  │
│  │  • Frontend: Vercel                                            │  │
│  │  • Backend: Render                                             │  │
│  │  • Database: Supabase                                          │  │
│  │  • CDN: Cloudflare                                             │  │
│  │  • Version Control: GitHub                                     │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Next Steps

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    YOUR JOURNEY BEGINS HERE                            │
│                                                                         │
│  ✅ You've learned:                                                    │
│  • Why we need a frontend                                             │
│  • What React is and why it exists                                   │
│  • What Next.js adds to React                                        │
│  • How to structure your project                                     │
│  • How routing works in Next.js                                     │
│  • How to write JSX                                                  │
│  • How to build components                                           │
│  • How to pass data with props                                       │
│  • How to manage state                                              │
│  • How to build forms                                               │
│  • How to call FastAPI APIs                                         │
│  • How to display data dynamically                                  │
│  • How to handle loading states                                     │
│  • How the complete architecture works                              │
│  • How to deploy to production                                      │
│                                                                         │
│  🚀 Now you're ready to build SQAnalytics!                           │
│                                                                         │
│  Start with:                                                           │
│  1. Create new Next.js project: `npx create-next-app@latest`         │
│  2. Set up your folder structure                                     │
│  3. Create your first page (Dashboard)                              │
│  4. Build the QR form and connect to FastAPI                        │
│  5. Display QR codes dynamically                                    │
│  6. Add analytics and charts                                        │
│  7. Implement authentication                                        │
│  8. Deploy to Vercel!                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# Quick Reference

## Common Commands

```bash
# Create new Next.js project
npx create-next-app@latest sqanalytics-frontend

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Deploy to Vercel (after connecting GitHub)
vercel --prod
```

## Useful Resources

- **Next.js Documentation**: https://nextjs.org/docs
- **React Documentation**: https://react.dev
- **FastAPI Documentation**: https://fastapi.tiangolo.com
- **Supabase Documentation**: https://supabase.com/docs
- **Vercel Documentation**: https://vercel.com/docs

