# HTTP Redirects & URL Routing for Modern Web Applications

## A Practical Beginner Guide for Building SQAnalytics with FastAPI, PostgreSQL, Supabase & GitHub

---

# COVER PAGE

---

**HTTP REDIRECTS & URL ROUTING FOR MODERN WEB APPLICATIONS**

*A Practical Beginner Guide for Building SQAnalytics with FastAPI, PostgreSQL, Supabase & GitHub*

---

**Senior Backend Architecture Handbook | Version 1.0**

---

*"Build redirect services. Track every click. Master web request flow."*

---

---

# TABLE OF CONTENTS

---

**SECTION 1** — What Is an HTTP Redirect? .................................. 7

**SECTION 2** — How the Web Handles Redirects ............................ 15

**SECTION 3** — HTTP Status Codes for Redirects ......................... 23

**SECTION 4** — URL Routing Fundamentals ................................... 31

**SECTION 5** — FastAPI Redirects ............................................... 39

**SECTION 6** — URL Shortener Architecture .................................. 47

**SECTION 7** — QR Analytics Architecture ..................................... 55

**SECTION 8** — Redirect-Based Tracking ...................................... 63

**SECTION 9** — Redirect Performance Considerations ................... 71

**SECTION 10** — Common Developer Mistakes ............................... 79

**SECTION 11** — SQAnalytics Case Study ...................................... 87

**SECTION 12** — Hands-On Exercises ........................................... 97

**SECTION 13** — Redirect Architecture Roadmap ......................... 107

**SECTION 14** — Redirect Cheat Sheet ......................................... 113

**SECTION 15** — Troubleshooting Guide ...................................... 121

**SECTION 16** — Interview Preparation Guide .............................. 129

---

---

# SECTION 1

## WHAT IS AN HTTP REDIRECT?

---

### 📖 Learning Objectives

- Understand what HTTP redirects are
- Recognize real-world redirect use cases
- Understand why redirects are essential
- Connect redirects to SQAnalytics

---

## 1.1 Definition

An **HTTP Redirect** is a server response that tells the client (browser) to go to a different URL than the one originally requested.

```
┌─────────────────────────────────────────────────────────────┐
│                     WHAT IS A REDIRECT?                    │
│                                                             │
│  User requests:  https://bit.ly/abc123                     │
│                                                             │
│  Server responds: "Go to https://example.com/page"         │
│                                                             │
│  Browser goes to: https://example.com/page                 │
│                                                             │
│  ┌──────────────┐         ┌──────────────┐                │
│  │   USER       │         │   SERVER     │                │
│  │  Requests    │────────▶│   Responds   │                │
│  │  Short URL   │         │  with 302    │                │
│  └──────────────┘         └──────────────┘                │
│         │                        │                         │
│         └────────────────────────┘                         │
│                        │                                   │
│                        ▼                                   │
│              ┌──────────────┐                             │
│              │   BROWSER    │                             │
│              │  Requests    │                             │
│              │  Long URL    │                             │
│              └──────────────┘                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 1.2 Why Redirects Exist

Redirects serve several critical purposes:

| Purpose | Example |
|---------|---------|
| **URL Shortening** | bit.ly/abc → example.com/long-path |
| **QR Code Tracking** | QR → redirect server → analytics → destination |
| **Website Migration** | old-site.com → new-site.com |
| **Marketing Campaigns** | campaign.com → landing-page.com |
| **Link Management** | Update links without changing QR codes |

---

## 1.3 Real-World Redirect Examples

### 📱 URL Shorteners

```
┌─────────────────────────────────────────────────────────────┐
│                    URL SHORTENER FLOW                      │
│                                                             │
│  User clicks:  https://bit.ly/3xYz789                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  bit.ly server looks up "3xYz789" in database     │   │
│  │  Finds: https://very-long-url.com/page/article     │   │
│  │  Sends redirect to: https://very-long-url.com/...  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Result: User ends up at the long URL                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 📊 QR Code Tracking

```
┌─────────────────────────────────────────────────────────────┐
│                    QR CODE TRACKING FLOW                   │
│                                                             │
│  User scans QR: /r/abc123                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Redirect server:                                  │   │
│  │  1. Looks up /r/abc123                            │   │
│  │  2. Logs scan event (location, time, device)      │   │
│  │  3. Redirects to destination URL                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Benefit: Track every scan without changing QR code        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 🔄 Website Migration

```
┌─────────────────────────────────────────────────────────────┐
│                    WEBSITE MIGRATION FLOW                  │
│                                                             │
│  Old URL:  https://oldsite.com/about                       │
│  New URL:  https://newsite.com/about-us                   │
│                                                             │
│  301 Redirect: All traffic from old → new URL             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  User bookmarks old URL                             │   │
│  │  Requests old URL                                   │   │
│  │  Server: "Moved permanently to newsite.com"        │   │
│  │  Browser goes to new URL                           │   │
│  │  User sees new site                                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 1.4 SQAnalytics Use Case

In **SQAnalytics**, redirects are the heart of the platform:

```
┌─────────────────────────────────────────────────────────────┐
│                 SQANALYTICS REDIRECT FLOW                  │
│                                                             │
│  1. User scans QR code                                      │
│     ┌──────────────────────────────────────────────────┐   │
│     │  QR contains: https://sqanalytics.com/r/xyz    │   │
│     └──────────────────────────────────────────────────┘   │
│                                                             │
│  2. Browser requests the short URL                         │
│     ┌──────────────────────────────────────────────────┐   │
│     │  GET /r/xyz                                     │   │
│     └──────────────────────────────────────────────────┘   │
│                                                             │
│  3. SQAnalytics processes the request                      │
│     ┌──────────────────────────────────────────────────┐   │
│     │  a) Looks up xyz in database                    │   │
│     │  b) Records scan event                          │   │
│     │  c) Redirects to destination                    │   │
│     └──────────────────────────────────────────────────┘   │
│                                                             │
│  4. User reaches the destination                          │
│     ┌──────────────────────────────────────────────────┐   │
│     │  https://example.com/product                    │   │
│     └──────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 1.5 The Redirect Chain

```
┌─────────────────────────────────────────────────────────────┐
│                     REDIRECT CHAIN                          │
│                                                             │
│  QR Code            →  Short URL            →  Destination  │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐│
│  │  /r/abc123   │────▶│  Server      │────▶│  example.com ││
│  │              │     │  Redirects   │     │              ││
│  └──────────────┘     └──────────────┘     └──────────────┘│
│                                                                 │
│  Each step:                                                    │
│  1. QR → Short URL (physical encoding)                       │
│  2. Short URL → Redirect (HTTP response)                     │
│  3. Redirect → Destination (browser follows)                 │
│                                                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 1.6 Redirect Types at a Glance

| Type | Status Code | Use Case |
|------|-------------|----------|
| **Permanent Redirect** | 301 | Site moved permanently |
| **Temporary Redirect** | 302 | A/B testing, maintenance |
| **Permanent (Preserve Method)** | 308 | API migration |
| **Temporary (Preserve Method)** | 307 | API maintenance |

---

## 🔍 Knowledge Checkpoint

**Question 1:** What is an HTTP redirect?

**Question 2:** Why does SQAnalytics use redirects for QR codes?

**Question 3:** Name three real-world redirect use cases.

---

## 📝 Section Summary

- **HTTP Redirects** tell browsers to go to different URLs
- **Redirects enable** URL shortening, tracking, and migration
- **SQAnalytics** uses redirects to track QR code scans
- **Redirects** are the foundation of modern tracking systems

---

---

# SECTION 2

## HOW THE WEB HANDLES REDIRECTS

---

### 📖 Learning Objectives

- Understand the browser-server redirect flow
- Understand request-response lifecycle
- Visualize the complete redirect journey
- Recognize redirect chain steps

---

## 2.1 The Complete Redirect Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    COMPLETE REDIRECT FLOW                         │
│                                                                     │
│  ┌──────────────┐    1. User clicks short URL                    │
│  │    USER      │──────────────────────────────────────┐         │
│  └──────────────┘                                      │         │
│                                                        ▼         │
│  ┌──────────────┐    2. Browser sends request         ┌───────────┐
│  │   BROWSER    │─────────────────────────────────────▶│  SERVER   │
│  └──────────────┘        GET /r/abc123                └─────┬─────┘
│         │                                                  │         │
│         │                                                  │         │
│         │    3. Server looks up code, prepares redirect   │         │
│         │    ┌─────────────────────────────────────────┐  │         │
│         │    │  - Find destination in database        │  │         │
│         │    │  - Log analytics event                 │  │         │
│         │    │  - Create redirect response            │  │         │
│         │    └─────────────────────────────────────────┘  │         │
│         │                                                  │         │
│         │    4. Server sends redirect response            │         │
│         │    HTTP/1.1 302 Found                          │         │
│         │    Location: https://example.com/page          │         │
│         │    ◀─────────────────────────────────────────────┘         │
│         │                                                  │         │
│         │    5. Browser automatically follows redirect    │         │
│         │    ┌─────────────────────────────────────────┐  │         │
│         │    │  - Read Location header                 │  │         │
│         │    │  - Create new request to destination    │  │         │
│         │    │  - User sees destination page           │  │         │
│         │    └─────────────────────────────────────────┘  │         │
│         ▼                                                  │         │
│  ┌──────────────┐    6. Request destination URL          │         │
│  │   BROWSER    │─────────────────────────────────────▶  │         │
│  └──────────────┘        GET /page                       │         │
│         │                                                  │         │
│         ▼                                                  │         │
│  ┌──────────────┐    7. Destination server responds      │         │
│  │   BROWSER    │◀─────────────────────────────────────  │         │
│  └──────────────┘        HTML page                       │         │
│         │                                                  │         │
│         ▼                                                  │         │
│  ┌──────────────┐                                         │         │
│  │    USER      │  Sees the destination page              │         │
│  └──────────────┘                                         │         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2.2 Request-Response Details

### Step 1: Initial Request

```
┌─────────────────────────────────────────────────────────────┐
│                 INITIAL REQUEST                            │
│                                                             │
│  HTTP Request:                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  GET /r/abc123 HTTP/1.1                           │   │
│  │  Host: sqanalytics.com                            │   │
│  │  User-Agent: Mozilla/5.0 (iPhone)                │   │
│  │  Accept: text/html,application/xhtml+xml         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  From: Browser                                             │
│  To: SQAnalytics Server                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 2: Redirect Response

```
┌─────────────────────────────────────────────────────────────┐
│                 REDIRECT RESPONSE                          │
│                                                             │
│  HTTP Response:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  HTTP/1.1 302 Found                               │   │
│  │  Location: https://example.com/page                │   │
│  │  Cache-Control: no-cache                          │   │
│  │  Content-Length: 0                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  From: SQAnalytics Server                                   │
│  To: Browser                                                │
│                                                             │
│  Key: Location header tells browser where to go            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 3: Follow Redirect

```
┌─────────────────────────────────────────────────────────────┐
│                 FOLLOWING THE REDIRECT                     │
│                                                             │
│  Browser does:                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Receives 302 response                         │   │
│  │  2. Reads Location: https://example.com/page      │   │
│  │  3. Creates new request to that URL               │   │
│  │  4. Sends GET /page HTTP/1.1                     │   │
│  │  5. Receives response from destination            │   │
│  │  6. Renders page for user                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Note: User never sees the redirect response                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2.3 Redirect Lifecycle Visual

```
┌─────────────────────────────────────────────────────────────┐
│                   REDIRECT LIFECYCLE                       │
│                                                             │
│  Time ─────────────────────────────────────────────────────▶│
│                                                             │
│  t=0:  User clicks QR code                                 │
│        │                                                    │
│        ▼                                                    │
│  t=1:  Browser sends GET /r/abc123                        │
│        │                                                    │
│        ▼                                                    │
│  t=2:  Server processes request                            │
│        │  - Database lookup                                │
│        │  - Analytics logging                              │
│        │                                                    │
│        ▼                                                    │
│  t=3:  Server sends 302 redirect                          │
│        │  Location: https://example.com/page              │
│        │                                                    │
│        ▼                                                    │
│  t=4:  Browser receives redirect                          │
│        │                                                    │
│        ▼                                                    │
│  t=5:  Browser sends GET /page to destination             │
│        │                                                    │
│        ▼                                                    │
│  t=6:  Destination server responds                        │
│        │                                                    │
│        ▼                                                    │
│  t=7:  User sees page                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2.4 Browser Redirect Behavior

### How Browsers Handle Redirects

```
┌─────────────────────────────────────────────────────────────┐
│                 BROWSER REDIRECT BEHAVIOR                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Request sent                                   │   │
│  │     ┌──────────────────────────────────────────┐   │   │
│  │     │  GET /r/abc123                          │   │   │
│  │     └──────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  2. Response received                             │   │
│  │     ┌──────────────────────────────────────────┐   │   │
│  │     │  HTTP/1.1 302 Found                     │   │   │
│  │     │  Location: https://example.com/page    │   │   │
│  │     └──────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  3. Browser reads Location header                  │   │
│  │     ┌──────────────────────────────────────────┐   │   │
│  │     │  https://example.com/page               │   │   │
│  │     └──────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  4. Browser creates new request                    │   │
│  │     ┌──────────────────────────────────────────┐   │   │
│  │     │  GET /page                              │   │   │
│  │     │  Host: example.com                      │   │   │
│  │     └──────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  5. Renders final page                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2.5 Important Redirect Behaviors

### 🔄 Automatic vs Manual

| Behavior | Description |
|----------|-------------|
| **Automatic** | Browser follows redirect without user interaction |
| **Manual** | User must click link (rare, only when configured) |

### 📝 Redirect vs Direct Request

| Aspect | Direct Request | Redirect |
|--------|---------------|----------|
| **Round trips** | 1 | 2+ |
| **Analytics** | Hard | Easy |
| **URL control** | Fixed | Flexible |
| **Speed** | Faster | Slower (but acceptable) |

---

## 2.6 SQAnalytics in Action

```
┌─────────────────────────────────────────────────────────────┐
│                 SQANALYTICS REDIRECT FLOW                  │
│                                                             │
│  User scans QR containing: sqanalytics.com/r/xyz          │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Browser: GET /r/xyz                              │   │
│  │  Server: FastAPI receives request                 │   │
│  │           Looks up "xyz" in database              │   │
│  │           Finds: https://example.com/product      │   │
│  │           Logs scan event                         │   │
│  │           Returns 302 redirect                    │   │
│  │  Browser: Automatically goes to destination       │   │
│  │  User: Sees https://example.com/product          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Result: QR scan tracked, user redirected                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What happens when a browser receives a 302 response?

**Question 2:** What is the Location header used for?

**Question 3:** How many HTTP requests are made in a redirect flow?

---

## 📝 Section Summary

- **Browser requests** short URL
- **Server responds** with redirect status and Location header
- **Browser automatically** follows the redirect
- **User sees** the final destination
- **Analytics** can be logged during the process

---

---

# SECTION 3

## HTTP STATUS CODES FOR REDIRECTS

---

### 📖 Learning Objectives

- Understand redirect status codes
- Know when to use each status code
- Recognize permanent vs temporary redirects
- Apply correct status codes in SQAnalytics

---

## 3.1 Redirect Status Codes Overview

```
┌─────────────────────────────────────────────────────────────┐
│               HTTP REDIRECT STATUS CODES                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   3xx REDIRECTS                    │   │
│  │                                                     │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │   │
│  │  │   301    │  │   302    │  │   307    │        │   │
│  │  │ Permanent│  │ Temporary│  │ Temporary│        │   │
│  │  │   Moved  │  │   Found  │  │ Redirect │        │   │
│  │  └──────────┘  └──────────┘  └──────────┘        │   │
│  │  ┌──────────┐                                    │   │
│  │  │   308    │                                    │   │
│  │  │ Permanent│                                    │   │
│  │  │ Redirect │                                    │   │
│  │  └──────────┘                                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3.2 Detailed Status Code Comparison

### 301 Moved Permanently

```
┌─────────────────────────────────────────────────────────────┐
│                    301 MOVED PERMANENTLY                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  HTTP/1.1 301 Moved Permanently                    │   │
│  │  Location: https://new-site.com/page              │   │
│  │  Cache-Control: max-age=31536000                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Use When:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Website permanently moved to new URL            │   │
│  │  ✅ Domain changed permanently                      │   │
│  │  ✅ HTTPS upgrade (http → https)                   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Browser Behavior:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Caches redirect                                 │   │
│  │  ✅ Updates bookmarks                              │   │
│  │  ✅ Search engines update URLs                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 302 Found (Temporary)

```
┌─────────────────────────────────────────────────────────────┐
│                      302 FOUND                             │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  HTTP/1.1 302 Found                               │   │
│  │  Location: https://example.com/page              │   │
│  │  Cache-Control: no-cache                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Use When:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Temporary maintenance page                     │   │
│  │  ✅ A/B testing                                    │   │
│  │  ✅ QR code tracking (SQAnalytics)                 │   │
│  │  ✅ Marketing campaigns                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Browser Behavior:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ❌ Does NOT cache redirect                        │   │
│  │  ❌ Does NOT update bookmarks                      │   │
│  │  ❌ Search engines keep original URL               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 307 Temporary Redirect

```
┌─────────────────────────────────────────────────────────────┐
│                   307 TEMPORARY REDIRECT                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  HTTP/1.1 307 Temporary Redirect                   │   │
│  │  Location: https://api.example.com/v2/users       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Use When:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ API temporary redirect                         │   │
│  │  ✅ Preserve HTTP method (POST → POST)             │   │
│  │  ✅ Alternative to 302 for APIs                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Browser Behavior:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Preserves original HTTP method                  │   │
│  │  ❌ Does NOT cache                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 308 Permanent Redirect

```
┌─────────────────────────────────────────────────────────────┐
│                   308 PERMANENT REDIRECT                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  HTTP/1.1 308 Permanent Redirect                   │   │
│  │  Location: https://api.example.com/v2/users       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Use When:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ API permanent redirect                         │   │
│  │  ✅ Preserve HTTP method (POST → POST)             │   │
│  │  ✅ API versioning                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Browser Behavior:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Preserves original HTTP method                  │   │
│  │  ✅ Caches redirect                                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3.3 Comparison Table

```
┌─────────────────────────────────────────────────────────────────────┐
│                    STATUS CODE COMPARISON                         │
│                                                                     │
│  ┌────────┬─────────────┬──────────┬──────────┬──────────────┐   │
│  │ CODE   │ NAME        │ PERM?   │ METHOD  │ CACHED?     │   │
│  ├────────┼─────────────┼──────────┼──────────┼──────────────┤   │
│  │ 301    │ Moved       │ ✅      │ Change  │ ✅          │   │
│  │        │ Permanently │         │ to GET  │             │   │
│  ├────────┼─────────────┼──────────┼──────────┼──────────────┤   │
│  │ 302    │ Found       │ ❌      │ Change  │ ❌          │   │
│  │        │             │         │ to GET  │             │   │
│  ├────────┼─────────────┼──────────┼──────────┼──────────────┤   │
│  │ 307    │ Temporary   │ ❌      │ Keep    │ ❌          │   │
│  │        │ Redirect    │         │ method  │             │   │
│  ├────────┼─────────────┼──────────┼──────────┼──────────────┤   │
│  │ 308    │ Permanent   │ ✅      │ Keep    │ ✅          │   │
│  │        │ Redirect    │         │ method  │             │   │
│  └────────┴─────────────┴──────────┴──────────┴──────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3.4 Which Redirect Should You Use?

### Decision Flow

```
┌─────────────────────────────────────────────────────────────┐
│              WHICH REDIRECT TO USE?                        │
│                                                             │
│  Start                                                    │
│    │                                                       │
│    ▼                                                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Is this a permanent change?                       │   │
│  └─────────────────────────────────────────────────────┘   │
│    │                    │                                   │
│    ▼ Yes                ▼ No                               │
│  ┌──────────────┐    ┌──────────────┐                     │
│  │  Use 301 or  │    │  Use 302 or  │                     │
│  │  308         │    │  307         │                     │
│  └──────┬───────┘    └──────┬───────┘                     │
│         │                   │                               │
│         ▼                   ▼                               │
│  ┌──────────────┐    ┌──────────────┐                     │
│  │  Is method   │    │  Is method   │                     │
│  │  important?  │    │  important?  │                     │
│  └──────┬───────┘    └──────┬───────┘                     │
│         │                   │                               │
│    Yes  ▼  No          Yes  ▼  No                         │
│  ┌──────────────┐    ┌──────────────┐                     │
│  │  Use 308     │    │  Use 301     │                     │
│  └──────────────┘    └──────────────┘                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Quick Reference

| Scenario | Recommended |
|----------|-------------|
| **QR Code Redirects** | 302 (Temporary) |
| **Site Migration** | 301 (Permanent) |
| **API Versioning** | 308 (Permanent, keep method) |
| **A/B Testing** | 302 (Temporary) |
| **HTTP → HTTPS** | 301 (Permanent) |
| **Maintenance Page** | 302 (Temporary) |

---

## 3.5 SQAnalytics: Which Redirect to Use?

```
┌─────────────────────────────────────────────────────────────┐
│              SQANALYTICS REDIRECT DECISION                 │
│                                                             │
│  For QR Code Redirects: USE 302 FOUND                     │
│                                                             │
│  Why?                                                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. QR code destinations may change                │   │
│  │  2. Analytics tracking needs fresh requests        │   │
│  │  3. No caching to ensure analytics accuracy        │   │
│  │  4. Temporary by nature                           │   │
│  │  5. Search engines should keep original URL       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Example:                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  GET /r/abc123                                    │   │
│  │  HTTP/1.1 302 Found                              │   │
│  │  Location: https://example.com/product           │   │
│  │  Cache-Control: no-cache, no-store               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** When should you use 301 vs 302 redirect?

**Question 2:** Why does SQAnalytics use 302 redirects?

**Question 3:** What's the difference between 302 and 307?

---

## 📝 Section Summary

- **301** = Permanent, cached, method changes to GET
- **302** = Temporary, not cached, method changes to GET
- **307** = Temporary, not cached, preserves method
- **308** = Permanent, cached, preserves method
- **SQAnalytics** uses **302** for QR redirects

---

---

# SECTION 4

## URL ROUTING FUNDAMENTALS

---

### 📖 Learning Objectives

- Understand URL routing concepts
- Work with route parameters
- Handle dynamic URLs
- Build route matching logic

---

## 4.1 What Is URL Routing?

**URL Routing** is the process of matching incoming HTTP requests to specific handlers (functions) based on the URL path.

```
┌─────────────────────────────────────────────────────────────┐
│                     URL ROUTING                            │
│                                                             │
│  Incoming Request:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  GET /users/123/profile                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Router matches URL pattern:                       │   │
│  │  /users/{user_id}/profile                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Extracts parameters:                             │   │
│  │  user_id = 123                                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Calls handler:                                   │   │
│  │  get_user_profile(user_id=123)                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4.2 Static vs Dynamic Routes

### 📍 Static Routes

```
┌─────────────────────────────────────────────────────────────┐
│                     STATIC ROUTES                          │
│                                                             │
│  URL: /about                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Always matches exactly: /about                    │   │
│  │  Always returns: About page content                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  URL: /contact                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Always matches exactly: /contact                  │   │
│  │  Always returns: Contact page content              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 🎯 Dynamic Routes

```
┌─────────────────────────────────────────────────────────────┐
│                    DYNAMIC ROUTES                          │
│                                                             │
│  Pattern: /users/{user_id}                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  /users/123   → user_id = 123                     │   │
│  │  /users/456   → user_id = 456                     │   │
│  │  /users/789   → user_id = 789                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Pattern: /r/{short_code}                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  /r/abc123   → short_code = abc123                │   │
│  │  /r/xyz789   → short_code = xyz789                │   │
│  │  /r/qwerty   → short_code = qwerty                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4.3 Route Parameter Types

```
┌─────────────────────────────────────────────────────────────┐
│                   ROUTE PARAMETER TYPES                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  PATH PARAMETERS                                   │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  /users/{id}                                │ │   │
│  │  │  /products/{product_id}                     │ │   │
│  │  │  /r/{short_code}                            │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  QUERY PARAMETERS                                  │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  /users?page=1&limit=10                     │ │   │
│  │  │  /search?q=hello&sort=asc                  │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  PATH vs QUERY                                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Path:   /users/123  (identifies resource)  │ │   │
│  │  │  Query:  /users?page=2 (modifies response)  │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4.4 Route Matching Process

```
┌─────────────────────────────────────────────────────────────┐
│                   ROUTE MATCHING PROCESS                   │
│                                                             │
│  Request: GET /r/abc123                                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Router receives request path: /r/abc123       │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  2. Check registered routes:                      │   │
│  │     ✅ /r/{code}                                 │   │
│  │     ❌ /                                          │   │
│  │     ❌ /api/qrs                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  3. Extract parameters:                           │   │
│  │     code = "abc123"                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  4. Call handler:                                 │   │
│  │     redirect_qr(code="abc123")                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4.5 URL Routing in Different Systems

### 🎯 FastAPI Routing

```python
from fastapi import FastAPI

app = FastAPI()

# Static route
@app.get("/about")
def about():
    return {"message": "About page"}

# Dynamic route with path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Dynamic route with validation
@app.get("/r/{short_code}")
def redirect_qr(short_code: str):
    # short_code is extracted from URL
    return {"code": short_code}
```

### 🌐 Express.js Routing

```javascript
// Static route
app.get('/about', (req, res) => {
    res.send('About page');
});

// Dynamic route
app.get('/users/:user_id', (req, res) => {
    const userId = req.params.user_id;
    res.send({ user_id: userId });
});

// QR route
app.get('/r/:short_code', (req, res) => {
    const code = req.params.short_code;
    // Redirect logic
});
```

### 📱 Django Routing

```python
# urls.py
urlpatterns = [
    path('about/', views.about),
    path('users/<int:user_id>/', views.user_detail),
    path('r/<str:short_code>/', views.redirect_qr),
]
```

---

## 4.6 Route Design Patterns

### Pattern 1: Resource Routes

```
┌─────────────────────────────────────────────────────────────┐
│                    RESOURCE ROUTES                         │
│                                                             │
│  GET    /users          → List all users                   │
│  POST   /users          → Create user                      │
│  GET    /users/{id}     → Get user by ID                   │
│  PUT    /users/{id}     → Update user                      │
│  DELETE /users/{id}     → Delete user                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Pattern 2: Nested Resources

```
┌─────────────────────────────────────────────────────────────┐
│                    NESTED RESOURCES                        │
│                                                             │
│  GET    /users/{id}/posts        → User's posts            │
│  POST   /users/{id}/posts        → Create post for user    │
│  GET    /users/{id}/posts/{pid}  → Specific user post      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Pattern 3: QR Redirect Routes

```
┌─────────────────────────────────────────────────────────────┐
│                    QR REDIRECT ROUTES                      │
│                                                             │
│  GET    /r/{code}         → Redirect to destination        │
│  GET    /r/{code}/stats   → Get QR analytics               │
│  POST   /r/{code}/rescan  → Rescan tracking                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4.7 Route Parameter Examples

```
┌─────────────────────────────────────────────────────────────┐
│                   ROUTE PARAMETER EXAMPLES                 │
│                                                             │
│  Example 1: User Profile                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  URL: /users/123/profile                          │   │
│  │  Pattern: /users/{user_id}/profile                │   │
│  │  Params: user_id = 123                            │   │
│  │  Handler: get_user_profile(user_id)              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Example 2: QR Redirect                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  URL: /r/abc123                                   │   │
│  │  Pattern: /r/{short_code}                         │   │
│  │  Params: short_code = abc123                     │   │
│  │  Handler: redirect_qr(short_code)                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Example 3: Product Details                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  URL: /products/456/reviews/2                     │   │
│  │  Pattern: /products/{product_id}/reviews/{rev_id} │   │
│  │  Params: product_id = 456, rev_id = 2             │   │
│  │  Handler: get_review(product_id, rev_id)          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What's the difference between static and dynamic routes?

**Question 2:** How does route parameter extraction work?

**Question 3:** What is the difference between path and query parameters?

---

## 📝 Section Summary

- **URL Routing** maps URLs to handlers
- **Static routes** match exact paths
- **Dynamic routes** use parameters
- **Path parameters** identify resources
- **Query parameters** modify responses

---

---

# SECTION 5

## FASTAPI REDIRECTS

---

### 📖 Learning Objectives

- Implement redirects in FastAPI
- Use RedirectResponse
- Work with route parameters
- Build QR redirect endpoints

---

## 5.1 FastAPI Redirect Basics

### Importing RedirectResponse

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi import Depends
```

### Simple Redirect

```python
@app.get("/old-page")
async def redirect_old_page():
    return RedirectResponse(url="/new-page")

# Access: /old-page → Redirects to /new-page
```

### Redirect with Status Code

```python
@app.get("/old-site")
async def redirect_old_site():
    return RedirectResponse(
        url="https://new-site.com",
        status_code=302  # Default is 307
    )
```

---

## 5.2 Complete FastAPI Redirect Example

```
┌─────────────────────────────────────────────────────────────┐
│               FASTAPI REDIRECT EXAMPLE                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Client: GET /r/abc123                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  FastAPI Endpoint:                                 │   │
│  │  @app.get("/r/{short_code}")                      │   │
│  │  def redirect_qr(short_code: str):               │   │
│  │      # Logic here                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Database Lookup:                                  │   │
│  │  destination = find_qr_code(short_code)           │   │
│  │  returns: "https://example.com/product"           │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Redirect:                                        │   │
│  │  return RedirectResponse(                         │   │
│  │      url=destination,                            │   │
│  │      status_code=302                             │   │
│  │  )                                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Client Redirects To:                             │   │
│  │  https://example.com/product                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 5.3 FastAPI Redirect with Route Parameters

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# Basic redirect with parameter
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str):
    """
    Redirect to the destination for the given short code.
    """
    # Database lookup would go here
    destination = f"https://example.com/{short_code}"
    
    return RedirectResponse(
        url=destination,
        status_code=302
    )

# Redirect with optional query parameters
@app.get("/r/{short_code}")
async def redirect_qr_with_params(
    short_code: str,
    ref: str | None = None  # Optional query parameter
):
    """
    Redirect with additional query parameters.
    """
    destination = f"https://example.com/{short_code}"
    
    if ref:
        destination = f"{destination}?ref={ref}"
    
    return RedirectResponse(url=destination, status_code=302)
```

---

## 5.4 Redirect with Analytics Logging

```python
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime

app = FastAPI()

# Database dependency
def get_db():
    # Database session setup
    pass

@app.get("/r/{short_code}")
async def redirect_with_analytics(
    short_code: str,
    db: Session = Depends(get_db),
    user_agent: str | None = None,
    ip_address: str | None = None
):
    """
    Redirect with analytics logging.
    """
    # 1. Look up the QR code
    # qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    
    # For demo purposes
    qr = {"destination": "https://example.com/product", "id": 123}
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR code not found")
    
    # 2. Log analytics
    # scan_event = ScanEvent(
    #     qr_id=qr.id,
    #     user_agent=user_agent,
    #     ip_address=ip_address,
    #     scanned_at=datetime.utcnow()
    # )
    # db.add(scan_event)
    # db.commit()
    
    # 3. Redirect
    return RedirectResponse(
        url=qr["destination"],
        status_code=302
    )
```

---

## 5.5 Redirect with Additional Headers

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

@app.get("/r/{short_code}")
async def redirect_with_headers(short_code: str):
    """
    Redirect with custom headers.
    """
    destination = "https://example.com/product"
    
    response = RedirectResponse(
        url=destination,
        status_code=302
    )
    
    # Add custom headers
    response.headers["X-Redirect-Source"] = "SQAnalytics"
    response.headers["X-Short-Code"] = short_code
    response.headers["Cache-Control"] = "no-cache, no-store"
    
    return response
```

---

## 5.6 Error Handling

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_qr_by_code

@app.get("/r/{short_code}")
async def redirect_qr_safe(
    short_code: str,
    db: Session = Depends(get_db)
):
    """
    Safe redirect with error handling.
    """
    try:
        # Look up QR code
        qr = get_qr_by_code(db, short_code)
        
        if not qr:
            raise HTTPException(
                status_code=404,
                detail=f"QR code '{short_code}' not found"
            )
        
        # Check if QR is active
        if not qr.active:
            raise HTTPException(
                status_code=410,  # Gone
                detail="This QR code has been deactivated"
            )
        
        # Redirect
        return RedirectResponse(
            url=qr.destination,
            status_code=302
        )
        
    except HTTPException:
        raise
    except Exception as e:
        # Log error
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        )
```

---

## 5.7 Complete Implementation

```python
# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import logging

from app.database import get_db
from app.models import QRCode, ScanEvent
from app.crud import get_qr_by_code
from datetime import datetime

app = FastAPI(title="SQAnalytics Redirect Service")

@app.get("/r/{short_code}")
async def redirect_qr(
    short_code: str,
    db: Session = Depends(get_db),
    user_agent: str | None = None
):
    """
    Redirect to destination and log scan.
    """
    # 1. Validate
    if not short_code or len(short_code) < 4:
        raise HTTPException(
            status_code=400,
            detail="Invalid short code"
        )
    
    # 2. Lookup QR code
    qr = get_qr_by_code(db, short_code)
    
    if not qr:
        raise HTTPException(
            status_code=404,
            detail=f"QR code '{short_code}' not found"
        )
    
    if not qr.active:
        raise HTTPException(
            status_code=410,
            detail="QR code is no longer active"
        )
    
    # 3. Log analytics
    try:
        scan = ScanEvent(
            qr_id=qr.id,
            short_code=short_code,
            user_agent=user_agent,
            scanned_at=datetime.utcnow()
        )
        db.add(scan)
        db.commit()
    except Exception as e:
        logging.error(f"Failed to log scan: {e}")
        # Don't fail redirect if analytics fails
    
    # 4. Redirect
    return RedirectResponse(
        url=qr.destination,
        status_code=302,
        headers={
            "X-Redirect-Source": "SQAnalytics",
            "X-Short-Code": short_code
        }
    )
```

---

## 5.8 Redirect Response Comparison

```
┌─────────────────────────────────────────────────────────────┐
│               REDIRECT RESPONSE COMPARISON                 │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  RedirectResponse(url="...")                      │   │
│  │  Default: 307 Temporary                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  RedirectResponse(url="...", status_code=301)    │   │
│  │  Permanent redirect                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  RedirectResponse(url="...", status_code=302)    │   │
│  │  Temporary redirect (recommended for SQAnalytics) │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** How do you create a redirect in FastAPI?

**Question 2:** What is the default status code for RedirectResponse?

**Question 3:** How do you add custom headers to a redirect?

---

## 📝 Section Summary

- **RedirectResponse** creates HTTP redirects
- **Route parameters** capture URL values
- **Status codes** control redirect behavior
- **Analytics** can be logged before redirecting
- **Error handling** ensures reliability

---

---

# SECTION 6

## URL SHORTENER ARCHITECTURE

---

### 📖 Learning Objectives

- Understand URL shortener architecture
- Know how services like Bitly work
- Design short URL systems
- Implement redirect resolution

---

## 6.1 How URL Shorteners Work

```
┌─────────────────────────────────────────────────────────────┐
│                  URL SHORTENER ARCHITECTURE               │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │               1. CREATE SHORT URL                  │   │
│  │                                                   │   │
│  │  User: "I want to shorten https://very-long.com"  │   │
│  │  ↓                                                 │   │
│  │  System: Generates unique code (abc123)           │   │
│  │  System: Stores {code → long_url} in database    │   │
│  │  System: Returns https://short.com/abc123        │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │               2. REDIRECT SHORT URL                │   │
│  │                                                   │   │
│  │  User clicks: https://short.com/abc123           │   │
│  │  ↓                                                 │   │
│  │  System: Looks up abc123 in database              │   │
│  │  System: Finds https://very-long.com             │   │
│  │  System: Redirects user to long URL              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6.2 Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                  CORE COMPONENTS                           │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  COMPONENT 1: Generation Engine                   │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Generate unique short codes              │ │   │
│  │  │  - Encode IDs (base62, base64)              │ │   │
│  │  │  - Handle collisions                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  COMPONENT 2: Storage Layer                       │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Store {code → destination}               │ │   │
│  │  │  - Fast lookups                             │ │   │
│  │  │  - Handle millions of records               │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  COMPONENT 3: Redirect Service                    │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Receive requests                         │ │   │
│  │  │  - Look up codes                            │ │   │
│  │  │  - Send redirect responses                  │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  COMPONENT 4: Analytics Layer                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Log clicks                               │ │   │
│  │  │  - Track locations                          │ │   │
│  │  │  - Generate reports                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6.3 Code Generation

### Base62 Encoding

```python
def encode_id_to_base62(num: int) -> str:
    """
    Convert ID to base62 short code.
    """
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    base = len(chars)
    
    if num == 0:
        return chars[0]
    
    result = []
    while num > 0:
        result.append(chars[num % base])
        num //= base
    
    return ''.join(reversed(result))

def decode_base62_to_id(code: str) -> int:
    """
    Convert base62 short code back to ID.
    """
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    base = len(chars)
    
    result = 0
    for char in code:
        result = result * base + chars.index(char)
    
    return result

# Examples
print(encode_id_to_base62(123))      # "B9"
print(encode_id_to_base62(1000000))  # "4c92"
```

### Generate Short Code

```python
import random
import string

def generate_short_code(length: int = 6) -> str:
    """
    Generate a random short code.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def generate_unique_code(db, length: int = 6) -> str:
    """
    Generate a unique short code (with collision handling).
    """
    while True:
        code = generate_short_code(length)
        # Check if already exists
        if not db.query(QRCode).filter(QRCode.short_code == code).first():
            return code
        # If collision, try again
```

---

## 6.4 Database Schema

```sql
-- SQLAlchemy model
class ShortURL(Base):
    __tablename__ = "short_urls"
    
    id = Column(Integer, primary_key=True)
    short_code = Column(String(10), unique=True, index=True)
    destination = Column(String(2048), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    clicks = Column(Integer, default=0)
    active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # For analytics
    last_clicked = Column(DateTime)
    expires_at = Column(DateTime, nullable=True)
```

```
┌─────────────────────────────────────────────────────────────┐
│                     DATABASE SCHEMA                        │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  short_urls                                       │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  id          │  INTEGER    │ PRIMARY KEY     │ │   │
│  │  │  short_code  │  VARCHAR    │ UNIQUE          │ │   │
│  │  │  destination │  VARCHAR    │ REQUIRED        │ │   │
│  │  │  created_at  │  DATETIME   │ DEFAULT NOW     │ │   │
│  │  │  clicks      │  INTEGER    │ DEFAULT 0       │ │   │
│  │  │  active      │  BOOLEAN    │ DEFAULT TRUE    │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6.5 Redirect Service Implementation

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/{short_code}")
async def redirect_to_destination(
    short_code: str,
    db: Session = Depends(get_db)
):
    """
    Redirect to the destination URL.
    """
    # 1. Look up short code
    url = db.query(ShortURL).filter(
        ShortURL.short_code == short_code,
        ShortURL.active == True
    ).first()
    
    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )
    
    # 2. Check expiration
    if url.expires_at and url.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=410,
            detail="Short URL has expired"
        )
    
    # 3. Update analytics
    url.clicks += 1
    url.last_clicked = datetime.utcnow()
    db.commit()
    
    # 4. Redirect
    return RedirectResponse(
        url=url.destination,
        status_code=302
    )
```

---

## 6.6 Bitly Architecture Comparison

```
┌─────────────────────────────────────────────────────────────┐
│                    BITLY ARCHITECTURE                      │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LOAD BALANCER                                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Distributes traffic across servers         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  APPLICATION SERVERS                               │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Handle HTTP requests                     │ │   │
│  │  │  - Process redirects                        │ │   │
│  │  │  - Validate short codes                     │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CACHE LAYER (Redis/Memcached)                    │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Cache frequently accessed codes           │ │   │
│  │  │  - Reduce database load                       │ │   │
│  │  │  - Fast lookups                              │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  DATABASE (PostgreSQL/MySQL)                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Primary data store                       │ │   │
│  │  │  - Short code → destination mapping          │ │   │
│  │  │  - Analytics storage                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6.7 Caching for Performance

```python
from functools import lru_cache
import redis

# Setup Redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_destination_with_cache(short_code: str, db: Session) -> str | None:
    """
    Get destination with caching.
    """
    # 1. Try cache
    cached = redis_client.get(f"short:{short_code}")
    if cached:
        return cached
    
    # 2. Query database
    url = db.query(ShortURL).filter(
        ShortURL.short_code == short_code,
        ShortURL.active == True
    ).first()
    
    if not url:
        return None
    
    # 3. Update cache
    redis_client.setex(
        f"short:{short_code}",
        3600,  # 1 hour TTL
        url.destination
    )
    
    return url.destination
```

---

## 6.8 URL Shortener Flow

```
┌─────────────────────────────────────────────────────────────┐
│               URL SHORTENER COMPLETE FLOW                  │
│                                                             │
│  1. CREATE                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  POST /shorten                                    │   │
│  │  Body: {"url": "https://long-url.com"}           │   │
│  │  ↓                                                 │   │
│  │  Generate: short_code = encode(id)                │   │
│  │  ↓                                                 │   │
│  │  Store: {short_code: url}                         │   │
│  │  ↓                                                 │   │
│  │  Return: {"short_url": "https://short.com/xyz"}   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  2. REDIRECT                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  GET /xyz                                         │   │
│  │  ↓                                                 │   │
│  │  Lookup: xyz → https://long-url.com               │   │
│  │  ↓                                                 │   │
│  │  Log analytics                                     │   │
│  │  ↓                                                 │   │
│  │  Redirect 302: https://long-url.com               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** How do URL shorteners generate short codes?

**Question 2:** Why use caching in a URL shortener?

**Question 3:** What components make up a URL shortener architecture?

---

## 📝 Section Summary

- **URL shorteners** create unique codes for long URLs
- **Code generation** uses base62 encoding or random strings
- **Storage** maps codes to destinations
- **Caching** improves performance
- **Analytics** tracks usage

---

---

# SECTION 7

## QR ANALYTICS ARCHITECTURE

---

### 📖 Learning Objectives

- Understand why QR codes need redirects
- Compare direct vs indirect QR linking
- Design QR analytics systems
- Build tracking architecture

---

## 7.1 Bad Design: Direct QR Linking

```
┌─────────────────────────────────────────────────────────────┐
│                 BAD DESIGN - DIRECT QR                     │
│                                                             │
│  QR Code contains: https://youtube.com/video123           │
│                                                             │
│  ┌──────────────┐                                         │
│  │   QR CODE    │  ───▶  YouTube                          │
│  │   /video123  │         │                                │
│  └──────────────┘         │                                │
│                           │                                │
│                           ▼                                │
│                     User watches video                     │
│                                                             │
│  ❌ PROBLEMS:                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ❌ No analytics                                   │   │
│  │  ❌ Can't change destination                      │   │
│  │  ❌ No tracking                                   │   │
│  │  ❌ No data on scans                               │   │
│  │  ❌ Can't A/B test                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7.2 Good Design: Redirect-Based QR

```
┌─────────────────────────────────────────────────────────────┐
│                 GOOD DESIGN - REDIRECT QR                  │
│                                                             │
│  QR Code contains: https://sqanalytics.com/r/abc123       │
│                                                             │
│  ┌──────────────┐   1. Scan QR            ┌──────────────┐│
│  │   QR CODE    │───────────────────────▶│  SQAnalytics ││
│  │   /r/abc123  │                         │   Redirect   ││
│  └──────────────┘                         └──────┬───────┘│
│                                                  │         │
│                                                  2. Lookup│
│                                                  │         │
│                                                  ▼         │
│                                         ┌──────────────┐ │
│                                         │   Database   │ │
│                                         │ /r/abc123 →  │ │
│                                         │ example.com  │ │
│                                         └──────┬───────┘ │
│                                                  │         │
│                                                  3. Log   │
│                                                  │         │
│                                                  ▼         │
│                                         ┌──────────────┐ │
│                                         │  Analytics   │ │
│                                         │  Log: Scan   │ │
│                                         └──────┬───────┘ │
│                                                  │         │
│                                                  4. Redirect│
│                                                  │         │
│                                                  ▼         │
│                                         ┌──────────────┐ │
│                                         │  Destination │ │
│                                         │  example.com │ │
│                                         └──────────────┘ │
│                                                             │
│  ✅ BENEFITS:                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Track every scan                              │   │
│  │  ✅ Change destination anytime                     │   │
│  │  ✅ A/B test with same QR                         │   │
│  │  ✅ Rich analytics data                            │   │
│  │  ✅ QR code never changes                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7.3 QR Analytics Architecture Components

```
┌─────────────────────────────────────────────────────────────┐
│                 QR ANALYTICS ARCHITECTURE                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. QR CODE GENERATION                             │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Generate short code (abc123)             │ │   │
│  │  │  - Store in database                        │ │   │
│  │  │  - Create QR image                          │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  2. REDIRECT SERVICE                              │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Receive scan requests                    │ │   │
│  │  │  - Look up short codes                      │ │   │
│  │  │  - Log analytics                            │ │   │
│  │  │  - Redirect to destination                  │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  3. ANALYTICS ENGINE                              │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Count scans                              │ │   │
│  │  │  - Track locations                          │ │   │
│  │  │  - Device detection                         │ │   │
│  │  │  - Time patterns                            │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  4. REPORTING & VISUALIZATION                    │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Dashboard                                │ │   │
│  │  │  - Charts                                   │ │   │
│  │  │  - Export reports                           │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7.4 Complete Analytics Flow

```
┌─────────────────────────────────────────────────────────────┐
│               COMPLETE ANALYTICS FLOW                      │
│                                                             │
│  ┌──────────┐                                              │
│  │  SCAN QR │  1. User scans QR code                      │
│  └────┬─────┘                                              │
│       │                                                     │
│       ▼                                                     │
│  ┌──────────┐                                              │
│  │  REQUEST │  2. Browser requests /r/abc123              │
│  │  /r/xyz  │                                              │
│  └────┬─────┘                                              │
│       │                                                     │
│       ▼                                                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  3. SQAnalytics processes request                   │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │  a) Extract: short_code = abc123              │ │  │
│  │  │  b) Lookup: database → destination           │ │  │
│  │  │  c) Log: INSERT INTO scan_events              │ │  │
│  │  │  d) Track: location, device, time             │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│       │                                                     │
│       ▼                                                     │
│  ┌──────────┐                                              │
│  │ REDIRECT │  4. Return 302 to destination              │
│  └────┬─────┘                                              │
│       │                                                     │
│       ▼                                                     │
│  ┌──────────┐                                              │
│  │  DEST   │  5. User reaches destination                 │
│  └──────────┘                                              │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  6. Analytics collected:                            │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │  - Total scans: 1,247                        │ │  │
│  │  │  - Unique users: 892                         │ │  │
│  │  │  - Locations: 45 countries                   │ │  │
│  │  │  - Devices: 65% mobile, 35% desktop          │ │  │
│  │  │  - Peak time: 2:00 PM - 4:00 PM             │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7.5 QR Analytics Data Model

```sql
-- QR Codes table
class QRCode(Base):
    __tablename__ = "qrs"
    
    id = Column(Integer, primary_key=True)
    short_code = Column(String(10), unique=True, index=True)
    destination = Column(String(2048), nullable=False)
    name = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Analytics metrics (denormalized for speed)
    total_scans = Column(Integer, default=0)
    unique_scans = Column(Integer, default=0)

-- Scan Events table
class ScanEvent(Base):
    __tablename__ = "scan_events"
    
    id = Column(Integer, primary_key=True)
    qr_id = Column(Integer, ForeignKey("qrs.id"), nullable=False)
    scanned_at = Column(DateTime, default=datetime.utcnow)
    
    # Analytics fields
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    location_country = Column(String(2))
    location_city = Column(String(100))
    device_type = Column(String(20))  # mobile, desktop, tablet
    browser = Column(String(50))
    referer = Column(String(2048))
    
    # Optional tracking
    campaign_id = Column(String(50))
    source = Column(String(50))
```

---

## 7.6 Implementing QR Analytics

```python
from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import geoip2.database

app = FastAPI()

# GeoIP service
geoip_reader = geoip2.database.Reader('GeoLite2-City.mmdb')

@app.get("/r/{short_code}")
async def track_and_redirect(
    short_code: str,
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Track QR scan and redirect.
    """
    # 1. Look up QR code
    qr = db.query(QRCode).filter(
        QRCode.short_code == short_code,
        QRCode.active == True
    ).first()
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR code not found")
    
    # 2. Extract analytics data
    ip = request.client.host
    user_agent = request.headers.get("user-agent")
    
    # GeoIP lookup
    try:
        geo = geoip_reader.city(ip)
        country = geo.country.iso_code
        city = geo.city.name
    except:
        country = None
        city = None
    
    # Device detection (simplified)
    device = "desktop"
    if "mobile" in user_agent.lower():
        device = "mobile"
    elif "tablet" in user_agent.lower():
        device = "tablet"
    
    # 3. Log scan event
    scan_event = ScanEvent(
        qr_id=qr.id,
        ip_address=ip,
        user_agent=user_agent,
        location_country=country,
        location_city=city,
        device_type=device,
        scanned_at=datetime.utcnow()
    )
    db.add(scan_event)
    
    # Update QR stats
    qr.total_scans += 1
    db.commit()
    
    # 4. Redirect
    return RedirectResponse(
        url=qr.destination,
        status_code=302,
        headers={
            "X-Scan-Tracked": "true",
            "X-Short-Code": short_code
        }
    )
```

---

## 7.7 Why QR Redirects Are Essential

```
┌─────────────────────────────────────────────────────────────┐
│            WHY QR REDIRECTS ARE ESSENTIAL                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. FLEXIBILITY                                   │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Change destination anytime                  │ │   │
│  │  │  A/B test without reprinting QR              │ │   │
│  │  │  Handle seasonal promotions                   │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  2. ANALYTICS                                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Count scans                                │ │   │
│  │  │  Track location and device                   │ │   │
│  │  │  Measure campaign performance                │ │   │
│  │  │  ROI tracking                               │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  3. SECURITY                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Block malicious destinations                │ │   │
│  │  │  Add warning pages                           │ │   │
│  │  │  Control access                              │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** Why should QR codes never point directly to destinations?

**Question 2:** What analytics data can be collected during a redirect?

**Question 3:** How does redirect-based tracking improve flexibility?

---

## 📝 Section Summary

- **Direct QR linking** provides no analytics or flexibility
- **Redirect-based QR** enables tracking and dynamic destinations
- **Analytics data** includes location, device, time
- **Flexibility** allows destination changes without new QR codes

---

---

# SECTION 8

## REDIRECT-BASED TRACKING

---

### 📖 Learning Objectives

- Understand redirect-based tracking
- Implement scan event logging
- Track user behavior
- Build analytics pipelines

---

## 8.1 What Is Redirect-Based Tracking?

**Redirect-Based Tracking** captures data about user interactions during the redirect process.

```
┌─────────────────────────────────────────────────────────────┐
│              REDIRECT-BASED TRACKING                       │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  WITHOUT TRACKING                                  │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  User → QR → Destination                    │ │   │
│  │  │  ❌ No data collected                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  WITH TRACKING                                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  User → QR → Redirect Server               │ │   │
│  │  │              ↓                              │ │   │
│  │  │          Log Scan Event                    │ │   │
│  │  │              ↓                              │ │   │
│  │  │          Destination                       │ │   │
│  │  │  ✅ Analytics collected                     │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 8.2 Tracking Data Points

```
┌─────────────────────────────────────────────────────────────┐
│                  TRACKING DATA POINTS                      │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  REQUEST DATA                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  IP Address                                 │ │   │
│  │  │  User Agent (browser, OS)                   │ │   │
│  │  │  Referer                                   │ │   │
│  │  │  HTTP Method                               │ │   │
│  │  │  Request Headers                           │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LOCATION DATA                                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Country                                    │ │   │
│  │  │  City                                       │ │   │
│  │  │  Timezone                                   │ │   │
│  │  │  Latitude/Longitude                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  DEVICE DATA                                       │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Device Type (mobile/desktop/tablet)        │ │   │
│  │  │  Operating System                           │ │   │
│  │  │  Browser                                    │ │   │
│  │  │  Screen Size                                 │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  BEHAVIOR DATA                                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Time of scan                               │ │   │
│  │  │  Scan frequency                             │ │   │
│  │  │  Return visits                              │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 8.3 Implementing Tracking

### Complete Tracking Implementation

```python
from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import geoip2.database
from user_agents import parse
from datetime import datetime
import hashlib

app = FastAPI()

# Initialize services
geoip_reader = geoip2.database.Reader('GeoLite2-City.mmdb')

def get_device_info(user_agent: str) -> dict:
    """Parse user agent for device info."""
    ua = parse(user_agent)
    return {
        "device_type": "mobile" if ua.is_mobile else "tablet" if ua.is_tablet else "desktop",
        "os": ua.os.family,
        "os_version": ua.os.version_string,
        "browser": ua.browser.family,
        "browser_version": ua.browser.version_string
    }

def get_location_info(ip: str) -> dict:
    """Get location from IP address."""
    try:
        response = geoip_reader.city(ip)
        return {
            "country": response.country.iso_code,
            "country_name": response.country.name,
            "city": response.city.name,
            "latitude": response.location.latitude,
            "longitude": response.location.longitude,
            "timezone": response.location.time_zone
        }
    except:
        return {
            "country": None,
            "country_name": None,
            "city": None,
            "latitude": None,
            "longitude": None,
            "timezone": None
        }

def generate_visitor_id(ip: str, user_agent: str) -> str:
    """Generate unique visitor ID."""
    data = f"{ip}|{user_agent}"
    return hashlib.md5(data.encode()).hexdigest()

@app.get("/r/{short_code}")
async def track_and_redirect(
    short_code: str,
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Track QR scan with comprehensive analytics.
    """
    # 1. Look up QR code
    qr = db.query(QRCode).filter(
        QRCode.short_code == short_code,
        QRCode.active == True
    ).first()
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    # 2. Extract request data
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "")
    referer = request.headers.get("referer")
    
    # 3. Get location
    location = get_location_info(ip)
    
    # 4. Get device info
    device = get_device_info(user_agent)
    
    # 5. Generate visitor ID
    visitor_id = generate_visitor_id(ip, user_agent)
    
    # 6. Create scan event
    scan_event = ScanEvent(
        qr_id=qr.id,
        scanned_at=datetime.utcnow(),
        ip_address=ip,
        user_agent=user_agent,
        referer=referer,
        location_country=location["country"],
        location_city=location["city"],
        latitude=location["latitude"],
        longitude=location["longitude"],
        timezone=location["timezone"],
        device_type=device["device_type"],
        os=device["os"],
        browser=device["browser"],
        visitor_id=visitor_id
    )
    db.add(scan_event)
    
    # 7. Update QR stats
    qr.total_scans += 1
    
    # Check if unique visitor
    existing_visitor = db.query(ScanEvent).filter(
        ScanEvent.qr_id == qr.id,
        ScanEvent.visitor_id == visitor_id
    ).first()
    
    if not existing_visitor:
        qr.unique_scans += 1
    
    db.commit()
    
    # 8. Redirect
    return RedirectResponse(
        url=qr.destination,
        status_code=302,
        headers={
            "X-Visitor-ID": visitor_id,
            "X-Scan-ID": str(scan_event.id)
        }
    )
```

---

## 8.4 Analytics Queries

### Get Scan Statistics

```python
from sqlalchemy import func

def get_qr_analytics(db: Session, qr_id: int) -> dict:
    """
    Get comprehensive analytics for a QR code.
    """
    # Total scans
    total_scans = db.query(ScanEvent).filter(
        ScanEvent.qr_id == qr_id
    ).count()
    
    # Unique visitors
    unique_visitors = db.query(
        func.count(func.distinct(ScanEvent.visitor_id))
    ).filter(ScanEvent.qr_id == qr_id).scalar()
    
    # Scans by device
    device_stats = db.query(
        ScanEvent.device_type,
        func.count(ScanEvent.id)
    ).filter(ScanEvent.qr_id == qr_id).group_by(
        ScanEvent.device_type
    ).all()
    
    # Scans by location
    location_stats = db.query(
        ScanEvent.location_country,
        func.count(ScanEvent.id)
    ).filter(ScanEvent.qr_id == qr_id).group_by(
        ScanEvent.location_country
    ).order_by(func.count(ScanEvent.id).desc()).limit(10).all()
    
    # Scans by hour
    hourly_stats = db.query(
        func.extract('hour', ScanEvent.scanned_at).label('hour'),
        func.count(ScanEvent.id)
    ).filter(ScanEvent.qr_id == qr_id).group_by(
        'hour'
    ).order_by('hour').all()
    
    return {
        "total_scans": total_scans,
        "unique_visitors": unique_visitors,
        "device_stats": {d[0]: d[1] for d in device_stats},
        "top_locations": [
            {"country": loc[0], "count": loc[1]}
            for loc in location_stats
        ],
        "hourly_distribution": [
            {"hour": int(h[0]), "count": h[1]}
            for h in hourly_stats
        ]
    }
```

---

## 8.5 Real-Time Tracking

```python
from fastapi import FastAPI, WebSocket
import asyncio

@app.websocket("/ws/analytics")
async def websocket_analytics(websocket: WebSocket):
    """
    Real-time analytics via WebSocket.
    """
    await websocket.accept()
    
    # Listen for new scan events
    while True:
        # In production, use a pub/sub system
        latest_scan = await get_latest_scan()
        await websocket.send_json(latest_scan)
        await asyncio.sleep(1)
```

---

## 8.6 Event Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                    EVENT PIPELINE                          │
│                                                             │
│  1. EVENT SOURCE                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  QR Scan → Redirect Server                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  2. EVENT CAPTURE                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Log raw event to database                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  3. EVENT PROCESSING                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  - Parse user agent                               │   │
│  │  - GeoIP lookup                                   │   │
│  │  - Device detection                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  4. EVENT STORAGE                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  - Store processed event                          │   │
│  │  - Update aggregates                              │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  5. EVENT CONSUMPTION                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  - Analytics dashboard                           │   │
│  │  - Reports                                       │   │
│  │  - Alerts                                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What data can be collected during redirect-based tracking?

**Question 2:** How do you identify unique visitors?

**Question 3:** What is the event pipeline in analytics?

---

## 📝 Section Summary

- **Redirect-based tracking** captures user data during redirects
- **Data points** include location, device, behavior
- **Unique visitors** identified by IP + user agent
- **Analytics queries** provide insights
- **Event pipelines** process tracking data

---

---

# SECTION 9

## REDIRECT PERFORMANCE CONSIDERATIONS

---

### 📖 Learning Objectives

- Understand redirect performance factors
- Optimize redirect speed
- Ensure reliability and scalability
- Manage URL stability

---

## 9.1 Why Performance Matters

```
┌─────────────────────────────────────────────────────────────┐
│              WHY REDIRECT PERFORMANCE MATTERS              │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  USER EXPERIENCE                                  │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Every 100ms delay → 1% conversion drop    │ │   │
│  │  │  Slow redirects → User abandonment          │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  SCALABILITY                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Millions of scans                           │ │   │
│  │  │  Traffic spikes                              │ │   │
│  │  │  Global users                                │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  RELIABILITY                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  99.9% uptime required                       │ │   │
│  │  │  No broken redirects                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 9.2 Performance Factors

```
┌─────────────────────────────────────────────────────────────┐
│                  PERFORMANCE FACTORS                       │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. DATABASE LOOKUP                               │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Index on short_code                        │ │   │
│  │  │  Query optimization                         │ │   │
│  │  │  Connection pooling                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  2. NETWORK LATENCY                               │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  CDN for static assets                      │ │   │
│  │  │  Global server distribution                  │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  3. RESPONSE SIZE                                 │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Minimal response body                      │ │   │
│  │  │  Compression enabled                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  4. CACHING                                       │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Redis for hot codes                        │ │   │
│  │  │  Browser caching when appropriate            │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 9.3 Optimization Techniques

### Database Indexing

```sql
-- Create index for fast lookups
CREATE INDEX idx_short_code ON qrs(short_code);

-- Composite index for common queries
CREATE INDEX idx_qr_active_code ON qrs(short_code, active);
```

### Connection Pooling

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=10,
    pool_timeout=30
)
```

### Caching with Redis

```python
import redis
import json

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
    socket_connect_timeout=2
)

def get_qr_with_cache(short_code: str, db: Session):
    """
    Get QR with Redis cache.
    """
    # Try cache
    cached = redis_client.get(f"qr:{short_code}")
    if cached:
        return json.loads(cached)
    
    # Query database
    qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    
    if qr:
        # Cache for 1 hour
        redis_client.setex(
            f"qr:{short_code}",
            3600,
            json.dumps(qr.to_dict())
        )
    
    return qr
```

---

## 9.4 Performance Testing

```python
import time
from fastapi.testclient import TestClient

def test_redirect_performance():
    """
    Test redirect performance.
    """
    client = TestClient(app)
    
    # Test 1000 requests
    start = time.time()
    
    for i in range(1000):
        response = client.get("/r/test123")
        assert response.status_code == 302
    
    end = time.time()
    
    avg_time = (end - start) / 1000
    requests_per_second = 1000 / (end - start)
    
    print(f"Average time: {avg_time:.3f}s")
    print(f"Requests per second: {requests_per_second:.1f}")
```

---

## 9.5 Scaling Considerations

```
┌─────────────────────────────────────────────────────────────┐
│                  SCALING CONSIDERATIONS                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEVEL 1: Single Server                            │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - App + DB on same server                  │ │   │
│  │  │  - Up to 100 req/s                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEVEL 2: Separated Services                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - App servers (multiple)                   │ │   │
│  │  │  - Dedicated DB                              │ │   │
│  │  │  - Load balancer                             │ │   │
│  │  │  - Up to 1000 req/s                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEVEL 3: Distributed Systems                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Global CDN                               │ │   │
│  │  │  - Database replication                      │ │   │
│  │  │  - Redis cluster                            │ │   │
│  │  │  - Up to 10,000+ req/s                      │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 9.6 URL Stability

### Long-Term URL Management

```python
def ensure_url_stability(short_code: str, db: Session):
    """
    Ensure long-term URL stability.
    """
    qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    
    if not qr:
        return None
    
    # Handle if destination has changed
    if qr.destination_changed:
        # Option 1: Keep redirecting to new destination
        return qr.current_destination
    
    # Option 2: Return 410 Gone if permanently removed
    if qr.removed:
        raise HTTPException(status_code=410, detail="QR code removed")
    
    return qr.destination

def update_destination_safely(
    short_code: str,
    new_destination: str,
    db: Session
):
    """
    Safely update destination with history.
    """
    qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    
    if not qr:
        return None
    
    # Log destination change
    history = DestinationHistory(
        qr_id=qr.id,
        old_destination=qr.destination,
        new_destination=new_destination,
        changed_at=datetime.utcnow()
    )
    db.add(history)
    
    # Update QR
    qr.destination = new_destination
    qr.updated_at = datetime.utcnow()
    
    db.commit()
    return qr
```

---

## 9.7 Performance Checklist

| Area | Action | Status |
|------|--------|--------|
| **Database** | Index on short_code | ✅ |
| **Database** | Connection pooling | ✅ |
| **Database** | Query optimization | ✅ |
| **Cache** | Redis for frequent codes | ✅ |
| **Cache** | Cache invalidation strategy | ✅ |
| **Network** | CDN for static assets | ✅ |
| **Network** | Gzip compression | ✅ |
| **Code** | Minimal response body | ✅ |
| **Code** | Async/await support | ✅ |
| **Monitoring** | Performance metrics | ✅ |
| **Scaling** | Horizontal scaling ready | ✅ |

---

## 🔍 Knowledge Checkpoint

**Question 1:** Why is redirect performance important?

**Question 2:** How does caching improve redirect performance?

**Question 3:** What strategies ensure long-term URL stability?

---

## 📝 Section Summary

- **Performance affects** user experience and conversions
- **Database indexing** and **caching** improve speed
- **Connection pooling** handles many requests
- **Scaling strategies** handle growth
- **URL stability** ensures long-term reliability

---

---

# SECTION 10

## COMMON DEVELOPER MISTAKES

---

### 📖 Learning Objectives

- Identify common redirect mistakes
- Understand their impact
- Implement solutions
- Avoid redirect anti-patterns

---

## 10.1 Mistake: Direct QR Destinations

### ❌ The Problem

```python
# QR code directly contains destination
QR_CODE = "https://example.com/product"

# No analytics
# No flexibility
# No tracking
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| No scan tracking | Zero analytics |
| Can't change destination | Inflexible |
| No performance data | Blind operations |

### ✅ Solution

```python
# QR code contains redirect URL
QR_CODE = "https://sqanalytics.com/r/abc123"

# Redirect endpoint
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str, db: Session = Depends(get_db)):
    # Look up and log
    qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    # Log analytics
    # Redirect
```

---

## 10.2 Mistake: Redirect Loops

### ❌ The Problem

```python
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str):
    # ⚠️ Potential loop!
    if short_code == "loop":
        return RedirectResponse(url="/r/loop")  # Infinite loop!
    return RedirectResponse(url="https://example.com")
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Browser "too many redirects" | User can't access page |
| Infinite loop | Server overload |
| Poor UX | Abandonment |

### ✅ Solution

```python
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str, db: Session = Depends(get_db)):
    # Look up destination
    qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    # Validate destination
    if qr.destination == f"/r/{short_code}":
        raise HTTPException(
            status_code=400,
            detail="Redirect loop detected"
        )
    
    # Log and redirect
    return RedirectResponse(url=qr.destination, status_code=302)
```

---

## 10.3 Mistake: Broken Redirects

### ❌ The Problem

```python
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str, db: Session = Depends(get_db)):
    # ❌ No validation of destination
    qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    return RedirectResponse(url=qr.destination, status_code=302)
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Redirect to invalid URL | 404 errors |
| Missing protocol | Broken links |
| No error handling | Hard to debug |

### ✅ Solution

```python
from urllib.parse import urlparse

@app.get("/r/{short_code}")
async def redirect_qr(short_code: str, db: Session = Depends(get_db)):
    qr = db.query(QRCode).filter(QRCode.short_code == short_code).first()
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    # Validate destination
    destination = qr.destination
    
    # Ensure URL is valid
    parsed = urlparse(destination)
    if not parsed.scheme:
        destination = f"https://{destination}"
    
    # Check if URL is safe
    if not is_safe_url(destination):
        raise HTTPException(status_code=400, detail="Unsafe URL")
    
    return RedirectResponse(url=destination, status_code=302)
```

---

## 10.4 Mistake: Missing Status Codes

### ❌ The Problem

```python
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str):
    # ❌ No status code specified
    return RedirectResponse(url="https://example.com")
    # Defaults to 307, may not be what you want
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Wrong caching behavior | Unexpected results |
| Method handling issues | API problems |
| SEO implications | Search engine issues |

### ✅ Solution

```python
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str):
    # ✅ Explicit status code
    return RedirectResponse(
        url="https://example.com",
        status_code=302  # Temporary redirect
    )

# For different scenarios
@app.get("/old-site")
async def redirect_old_site():
    return RedirectResponse(
        url="https://new-site.com",
        status_code=301  # Permanent redirect
    )
```

---

## 10.5 Mistake: No Analytics Logging

### ❌ The Problem

```python
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str, db: Session = Depends(get_db)):
    qr = get_qr_by_code(db, short_code)
    # ❌ No analytics logged!
    return RedirectResponse(url=qr.destination, status_code=302)
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| No scan data | Can't measure success |
| No user insights | Blind operations |
| Can't optimize | Guesswork |

### ✅ Solution

```python
@app.get("/r/{short_code}")
async def redirect_qr(
    short_code: str,
    request: Request,
    db: Session = Depends(get_db)
):
    qr = get_qr_by_code(db, short_code)
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    # ✅ Log analytics
    scan_event = ScanEvent(
        qr_id=qr.id,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent"),
        scanned_at=datetime.utcnow()
    )
    db.add(scan_event)
    qr.scan_count += 1
    db.commit()
    
    return RedirectResponse(url=qr.destination, status_code=302)
```

---

## 10.6 Mistake: Ignoring Security

### ❌ The Problem

```python
@app.get("/r/{short_code}")
async def redirect_qr(short_code: str, db: Session = Depends(get_db)):
    qr = get_qr_by_code(db, short_code)
    # ❌ No security checks!
    return RedirectResponse(url=qr.destination, status_code=302)
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Open redirects | Security vulnerability |
| Phishing attacks | Reputation damage |
| Malicious destinations | User harm |

### ✅ Solution

```python
def is_safe_url(url: str) -> bool:
    """
    Check if URL is safe to redirect to.
    """
    # Block non-https
    if not url.startswith("https://"):
        return False
    
    # Check domain whitelist
    parsed = urlparse(url)
    allowed_domains = ["example.com", "trusted-domain.com"]
    if parsed.netloc not in allowed_domains:
        return False
    
    return True

@app.get("/r/{short_code}")
async def redirect_qr(short_code: str, db: Session = Depends(get_db)):
    qr = get_qr_by_code(db, short_code)
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    # ✅ Security check
    if not is_safe_url(qr.destination):
        raise HTTPException(
            status_code=400,
            detail="Destination URL not allowed"
        )
    
    return RedirectResponse(url=qr.destination, status_code=302)
```

---

## 10.7 Mistake Summary

```
┌─────────────────────────────────────────────────────────────┐
│                COMMON MISTAKES SUMMARY                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  MISTAKE                    │  SOLUTION             │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  Direct QR destinations    │  Use redirect service  │   │
│  │  Redirect loops            │  Validate destination  │   │
│  │  Broken redirects          │  Validate URLs        │   │
│  │  Missing status codes      │  Explicit status      │   │
│  │  No analytics              │  Log every scan       │   │
│  │  Security issues           │  URL whitelist        │   │
│  │  No error handling         │  Try/except blocks    │   │
│  │  Poor caching              │  Cache strategy       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** Why is direct QR linking a bad practice?

**Question 2:** How do you prevent redirect loops?

**Question 3:** What security checks should you implement?

---

## 📝 Section Summary

- **Always use redirect services** for QR codes
- **Validate destinations** to prevent loops
- **Implement security checks** for safe redirects
- **Log analytics** for every scan
- **Use explicit status codes** for clarity

---

---

# SECTION 11

## SQANALYTICS CASE STUDY

---

### 📖 Learning Objectives

- Apply redirect concepts to SQAnalytics
- Build complete QR redirect service
- Implement analytics tracking
- Understand every component

---

## 11.1 SQAnalytics Overview

**SQAnalytics** is a Smart QR Analytics Platform that:

1. Generates QR codes with short URLs
2. Tracks every QR code scan
3. Provides analytics about scan behavior
4. Redirects users to destinations

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                SQANALYTICS ARCHITECTURE                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  FRONTEND: React Dashboard                         │   │
│  │  - QR code generation                             │   │
│  │  - Analytics visualization                        │   │
│  │  - QR management                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  BACKEND: FastAPI                                 │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - QR management endpoints                  │ │   │
│  │  │  - Redirect service                         │ │   │
│  │  │  - Analytics endpoints                      │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  DATABASE: PostgreSQL                             │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - qrs (short_code → destination)           │ │   │
│  │  │  - scan_events (analytics)                   │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 11.2 Complete Implementation

### Models

```python
# app/models.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class QRCode(Base):
    __tablename__ = "qrs"
    
    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    destination = Column(Text, nullable=False)
    name = Column(String(100))
    description = Column(Text)
    active = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    
    # Analytics
    total_scans = Column(Integer, default=0)
    unique_scans = Column(Integer, default=0)
    
    # Relationships
    scan_events = relationship("ScanEvent", back_populates="qr")

class ScanEvent(Base):
    __tablename__ = "scan_events"
    
    id = Column(Integer, primary_key=True, index=True)
    qr_id = Column(Integer, ForeignKey("qrs.id"), nullable=False)
    
    scanned_at = Column(DateTime, default=datetime.utcnow)
    
    # Request data
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    referer = Column(Text, nullable=True)
    
    # Location data
    location_country = Column(String(2))
    location_city = Column(String(100))
    latitude = Column(String(20))
    longitude = Column(String(20))
    timezone = Column(String(50))
    
    # Device data
    device_type = Column(String(20))  # mobile, desktop, tablet
    os = Column(String(50))
    browser = Column(String(50))
    
    # Visitor tracking
    visitor_id = Column(String(64))
    session_id = Column(String(64))
    
    # Campaign tracking
    campaign_id = Column(String(50))
    source = Column(String(50))
    medium = Column(String(50))
    
    # Relationships
    qr = relationship("QRCode", back_populates="scan_events")
```

---

## 11.3 Redirect Implementation

```python
# app/api/redirect.py

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from urllib.parse import urlparse
import hashlib
import geoip2.database

from app.database import get_db
from app.models import QRCode, ScanEvent
from app.crud import get_active_qr

router = APIRouter()

# Initialize GeoIP
geoip_reader = geoip2.database.Reader('GeoLite2-City.mmdb')

def is_safe_url(url: str) -> bool:
    """Check if URL is safe."""
    parsed = urlparse(url)
    if not parsed.scheme or parsed.scheme not in ['http', 'https']:
        return False
    # Add your domain whitelist
    allowed_domains = []
    if parsed.netloc not in allowed_domains:
        # Allow all domains for production
        pass
    return True

def get_device_info(user_agent: str) -> dict:
    """Parse user agent for device info."""
    from user_agents import parse
    ua = parse(user_agent)
    return {
        "device_type": "mobile" if ua.is_mobile else "tablet" if ua.is_tablet else "desktop",
        "os": ua.os.family,
        "browser": ua.browser.family
    }

def get_location_info(ip: str) -> dict:
    """Get location from IP."""
    try:
        response = geoip_reader.city(ip)
        return {
            "country": response.country.iso_code,
            "city": response.city.name,
            "latitude": str(response.location.latitude),
            "longitude": str(response.location.longitude),
            "timezone": response.location.time_zone
        }
    except:
        return {
            "country": None,
            "city": None,
            "latitude": None,
            "longitude": None,
            "timezone": None
        }

@router.get("/r/{short_code}")
async def redirect_qr(
    short_code: str,
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Redirect to QR code destination and log analytics.
    """
    # 1. Validate short code
    if not short_code or len(short_code) < 4:
        raise HTTPException(
            status_code=400,
            detail="Invalid short code"
        )
    
    # 2. Look up QR code
    qr = get_active_qr(db, short_code)
    
    if not qr:
        raise HTTPException(
            status_code=404,
            detail=f"QR code '{short_code}' not found"
        )
    
    # 3. Check expiration
    if qr.expires_at and qr.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=410,
            detail="QR code has expired"
        )
    
    # 4. Validate destination
    if not is_safe_url(qr.destination):
        raise HTTPException(
            status_code=400,
            detail="Destination URL is not allowed"
        )
    
    # 5. Extract request data
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "")
    referer = request.headers.get("referer")
    
    # 6. Get location
    location = get_location_info(ip)
    
    # 7. Get device info
    device = get_device_info(user_agent)
    
    # 8. Generate visitor ID
    visitor_id = hashlib.md5(f"{ip}|{user_agent}".encode()).hexdigest()
    
    # 9. Create scan event
    scan_event = ScanEvent(
        qr_id=qr.id,
        ip_address=ip,
        user_agent=user_agent,
        referer=referer,
        location_country=location["country"],
        location_city=location["city"],
        latitude=location["latitude"],
        longitude=location["longitude"],
        timezone=location["timezone"],
        device_type=device["device_type"],
        os=device["os"],
        browser=device["browser"],
        visitor_id=visitor_id
    )
    db.add(scan_event)
    
    # 10. Update QR stats
    qr.total_scans += 1
    
    # Check if unique visitor
    existing = db.query(ScanEvent).filter(
        ScanEvent.qr_id == qr.id,
        ScanEvent.visitor_id == visitor_id
    ).first()
    
    if not existing:
        qr.unique_scans += 1
    
    db.commit()
    
    # 11. Redirect
    return RedirectResponse(
        url=qr.destination,
        status_code=302,
        headers={
            "X-Visitor-ID": visitor_id,
            "X-Scan-ID": str(scan_event.id)
        }
    )
```

---

## 11.4 Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│               SQANALYTICS COMPLETE FLOW                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. CREATE QR CODE                                │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  User: "Create QR for https://example.com"  │ │   │
│  │  │  System: Generate short_code = "abc123"    │ │   │
│  │  │  System: Store in database                  │ │   │
│  │  │  System: Generate QR image                  │ │   │
│  │  │  System: Return QR with /r/abc123          │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  2. SCAN QR CODE                                 │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  User scans QR → GET /r/abc123              │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  3. REDIRECT PROCESS                              │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  a) Look up abc123 → example.com            │ │   │
│  │  │  b) Extract: IP, User Agent, Referer        │ │   │
│  │  │  c) GeoIP: Location detection               │ │   │
│  │  │  d) Device detection                         │ │   │
│  │  │  e) Generate visitor ID                     │ │   │
│  │  │  f) Log scan event                          │ │   │
│  │  │  g) Update QR stats                         │ │   │
│  │  │  h) Redirect to destination                 │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  4. VIEW ANALYTICS                                │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  Dashboard shows:                           │ │   │
│  │  │  - 1,247 total scans                        │ │   │
│  │  │  - 892 unique visitors                      │ │   │
│  │  │  - 45 countries                             │ │   │
│  │  │  - 65% mobile                               │ │   │
│  │  │  - Peak time: 2-4 PM                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 11.5 Analytics Endpoints

```python
# app/api/analytics.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter()

@router.get("/analytics/{short_code}")
async def get_qr_analytics(
    short_code: str,
    db: Session = Depends(get_db)
):
    """
    Get analytics for a QR code.
    """
    qr = get_active_qr(db, short_code)
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    # Total scans
    total_scans = qr.total_scans
    
    # Unique visitors
    unique_visitors = qr.unique_scans
    
    # Device breakdown
    device_stats = db.query(
        ScanEvent.device_type,
        func.count(ScanEvent.id)
    ).filter(ScanEvent.qr_id == qr.id).group_by(
        ScanEvent.device_type
    ).all()
    
    # Location breakdown
    location_stats = db.query(
        ScanEvent.location_country,
        func.count(ScanEvent.id)
    ).filter(ScanEvent.qr_id == qr.id).group_by(
        ScanEvent.location_country
    ).order_by(func.count(ScanEvent.id).desc()).limit(10).all()
    
    # Time series (daily)
    time_series = db.query(
        func.date(ScanEvent.scanned_at).label('date'),
        func.count(ScanEvent.id)
    ).filter(ScanEvent.qr_id == qr.id).group_by(
        'date'
    ).order_by('date').limit(30).all()
    
    return {
        "short_code": short_code,
        "destination": qr.destination,
        "total_scans": total_scans,
        "unique_visitors": unique_visitors,
        "device_breakdown": {
            d[0]: d[1] for d in device_stats
        },
        "top_countries": [
            {"country": loc[0], "scans": loc[1]}
            for loc in location_stats
        ],
        "daily_scans": [
            {"date": d[0], "count": d[1]}
            for d in time_series
        ]
    }
```

---

## 11.6 Deployment Considerations

```
┌─────────────────────────────────────────────────────────────┐
│              DEPLOYMENT CONSIDERATIONS                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ENVIRONMENT VARIABLES                             │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  DATABASE_URL                               │ │   │
│  │  │  REDIS_URL                                  │ │   │
│  │  │  ALLOWED_DOMAINS                            │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  MONITORING                                       │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Request latency                          │ │   │
│  │  │  - Error rates                              │ │   │
│  │  │  - Scan volume                              │ │   │
│  │  │  - Database performance                      │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  SCALING                                          │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Horizontal scaling                       │ │   │
│  │  │  - Database replication                      │ │   │
│  │  │  - Global CDN                               │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What are the key components of SQAnalytics?

**Question 2:** How does the redirect process work?

**Question 3:** What analytics data is collected?

---

## 📝 Section Summary

- **SQAnalytics** combines QR generation with redirect tracking
- **Redirect service** logs analytics before redirecting
- **Analytics data** includes location, device, time
- **Complete flow** from QR creation to analytics

---

---

# SECTION 12

## HANDS-ON EXERCISES

---

### 📖 Learning Objectives

- Build redirect services
- Implement URL shortening
- Create analytics tracking
- Solve real problems

---

## 12.1 Guided Exercise: Basic Redirect

### Objective
Create a basic redirect service.

### Step 1: Setup FastAPI

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()

# Store redirects (in memory for exercise)
redirects = {
    "google": "https://google.com",
    "github": "https://github.com"
}
```

### Step 2: Create Redirect Endpoint

```python
@app.get("/r/{short_code}")
async def redirect_to_url(short_code: str):
    """
    Redirect to the stored URL.
    """
    destination = redirects.get(short_code)
    
    if not destination:
        raise HTTPException(
            status_code=404,
            detail=f"Short code '{short_code}' not found"
        )
    
    return RedirectResponse(url=destination, status_code=302)
```

### Step 3: Test It

```python
# Test with curl
# curl -v http://localhost:8000/r/google

# Expected: Redirect to https://google.com
```

---

## 12.2 Guided Exercise: URL Shortener

### Objective
Create a simple URL shortener.

### Step 1: Add Shorten Endpoint

```python
import random
import string
from pydantic import BaseModel

class URLData(BaseModel):
    url: str

def generate_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

short_urls = {}

@app.post("/shorten")
async def shorten_url(data: URLData):
    """
    Create a shortened URL.
    """
    # Generate unique code
    while True:
        code = generate_code()
        if code not in short_urls:
            break
    
    short_urls[code] = data.url
    
    return {
        "short_code": code,
        "short_url": f"http://localhost:8000/r/{code}"
    }
```

### Step 2: Test It

```python
# Test with curl
# curl -X POST http://localhost:8000/shorten \
#   -H "Content-Type: application/json" \
#   -d '{"url": "https://very-long-url.com/page"}'

# Response: {"short_code": "abc123", "short_url": "http://localhost:8000/r/abc123"}
```

---

## 12.3 Mini Project: QR Redirect Service

### Objective
Build a complete QR redirect service with analytics.

### Requirements

1. QR code generation
2. Redirect with tracking
3. Analytics logging
4. Dashboard (optional)

### Implementation

```python
# Complete QR redirect service

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime
import hashlib

app = FastAPI()

# Models (simplified)
class QRCode:
    def __init__(self, code, destination):
        self.code = code
        self.destination = destination
        self.scans = 0

class ScanEvent:
    def __init__(self, code, ip, user_agent):
        self.code = code
        self.ip = ip
        self.user_agent = user_agent
        self.timestamp = datetime.utcnow()

# Storage
qrs = {}
scans = []

@app.get("/r/{code}")
async def redirect_qr(
    code: str,
    request: Request
):
    """
    Redirect QR code with tracking.
    """
    # Look up QR
    qr = qrs.get(code)
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    # Log scan
    scan = ScanEvent(
        code=code,
        ip=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    scans.append(scan)
    
    # Update stats
    qr.scans += 1
    
    # Redirect
    return RedirectResponse(url=qr.destination, status_code=302)

@app.post("/qrs")
async def create_qr(destination: str):
    """
    Create a new QR code.
    """
    import random
    import string
    
    # Generate code
    code = ''.join(random.choices(
        string.ascii_letters + string.digits,
        k=6
    ))
    
    # Store
    qrs[code] = QRCode(code, destination)
    
    return {
        "code": code,
        "url": f"/r/{code}",
        "destination": destination
    }

@app.get("/analytics/{code}")
async def get_analytics(code: str):
    """
    Get analytics for a QR code.
    """
    qr = qrs.get(code)
    
    if not qr:
        raise HTTPException(status_code=404, detail="QR not found")
    
    qr_scans = [s for s in scans if s.code == code]
    
    return {
        "code": code,
        "destination": qr.destination,
        "total_scans": len(qr_scans),
        "unique_ips": len(set(s.ip for s in qr_scans))
    }
```

---

## 12.4 Mini Project: Analytics Dashboard

### Objective
Build analytics endpoints for QR tracking.

### Implementation

```python
@app.get("/analytics/dashboard")
async def analytics_dashboard():
    """
    Get global analytics.
    """
    total_qrs = len(qrs)
    total_scans = len(scans)
    
    # Scans by QR
    qr_stats = []
    for code, qr in qrs.items():
        qr_scans = [s for s in scans if s.code == code]
        qr_stats.append({
            "code": code,
            "destination": qr.destination,
            "scans": len(qr_scans)
        })
    
    # Sort by scans
    qr_stats.sort(key=lambda x: x["scans"], reverse=True)
    
    # Top IPs
    ip_counts = {}
    for scan in scans:
        ip_counts[scan.ip] = ip_counts.get(scan.ip, 0) + 1
    
    top_ips = sorted(
        [{"ip": ip, "scans": count} for ip, count in ip_counts.items()],
        key=lambda x: x["scans"],
        reverse=True
    )[:10]
    
    return {
        "total_qrs": total_qrs,
        "total_scans": total_scans,
        "top_qrs": qr_stats[:10],
        "top_ips": top_ips,
        "scans_by_time": get_scans_by_time()
    }

def get_scans_by_time():
    """Group scans by hour."""
    hourly = {}
    for scan in scans:
        hour = scan.timestamp.hour
        hourly[hour] = hourly.get(hour, 0) + 1
    
    return [
        {"hour": h, "scans": count}
        for h, count in sorted(hourly.items())
    ]
```

---

## 12.5 Troubleshooting Labs

### Lab 1: Missing QR Code

```python
# Scenario: User scans QR but gets 404

# ❌ Problem: QR code not found in database
@app.get("/r/{code}")
async def redirect_qr(code: str):
    qr = qrs.get(code)  # qrs is empty!
    if not qr:
        raise HTTPException(status_code=404, detail="Not found")

# ✅ Solution: Check if QR was created
# First create a QR:
# POST /qrs?destination=https://example.com
# Then scan it:
# GET /r/{generated_code}
```

### Lab 2: Redirect Loop

```python
# ❌ Problem: Infinite redirect
@app.get("/r/loop")
async def redirect_loop():
    return RedirectResponse(url="/r/loop")

# ✅ Solution: Detect loops
@app.get("/r/{code}")
async def redirect_qr(code: str):
    if code == "loop":
        raise HTTPException(status_code=400, detail="Redirect loop detected")
    # Normal redirect
```

### Lab 3: Broken Redirect

```python
# ❌ Problem: Missing protocol
@app.get("/r/broken")
async def redirect_broken():
    return RedirectResponse(url="example.com")  # No protocol!

# ✅ Solution: Validate URL
from urllib.parse import urlparse

def validate_url(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.scheme:
        return f"https://{url}"
    return url
```

---

## 12.6 Exercise Solutions

### Solution: Create QR Code

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random
import string

app = FastAPI()
database = {}

def generate_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

@app.post("/create")
async def create_qr(destination: str):
    code = generate_code()
    database[code] = destination
    return {
        "code": code,
        "url": f"/r/{code}"
    }

@app.get("/r/{code}")
async def redirect_qr(code: str):
    destination = database.get(code)
    if not destination:
        raise HTTPException(status_code=404, detail="Not found")
    return RedirectResponse(url=destination, status_code=302)
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** How do you generate unique short codes?

**Question 2:** What data should be logged for analytics?

**Question 3:** How do you prevent redirect loops?

---

## 📝 Section Summary

- **Guided exercises** build fundamental skills
- **Mini projects** create complete services
- **Troubleshooting labs** solve real problems
- **Practice** reinforces learning

---

---

# SECTION 13

## REDIRECT ARCHITECTURE ROADMAP

---

### 📖 Learning Objectives

- Understand redirect architecture evolution
- Plan system growth
- Identify scaling strategies
- Build production-ready systems

---

## 13.1 Architecture Evolution

```
┌─────────────────────────────────────────────────────────────┐
│               ARCHITECTURE EVOLUTION ROADMAP               │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEVEL 1: BASIC REDIRECT                          │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - In-memory storage                        │ │   │
│  │  │  - Single endpoint                          │ │   │
│  │  │  - No analytics                             │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEVEL 2: PERSISTENT STORAGE                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Database storage                         │ │   │
│  │  │  - Analytics logging                         │ │   │
│  │  │  - Multiple endpoints                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEVEL 3: CACHED REDIRECTS                        │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Redis cache                               │ │   │
│  │  │  - Load balancing                            │ │   │
│  │  │  - Analytics pipeline                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEVEL 4: DISTRIBUTED SYSTEM                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Global CDN                               │ │   │
│  │  │  - Database replication                      │ │   │
│  │  │  - Real-time analytics                       │ │   │
│  │  │  - Auto-scaling                             │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 13.2 Implementation Roadmap

### Phase 1: Core Redirect (Week 1)

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 1: CORE REDIRECT                  │
│                                                             │
│  Tasks:                                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Set up FastAPI project                         │   │
│  │  ✅ Create /r/{code} endpoint                     │   │
│  │  ✅ Implement basic redirect                       │   │
│  │  ✅ Add 302 status code                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Deliverables:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  - Working redirect endpoint                       │   │
│  │  - In-memory storage                               │   │
│  │  - Basic error handling                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Phase 2: Database Integration (Week 2)

```
┌─────────────────────────────────────────────────────────────┐
│                PHASE 2: DATABASE INTEGRATION               │
│                                                             │
│  Tasks:                                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Set up PostgreSQL                             │   │
│  │  ✅ Create QRCode model                           │   │
│  │  ✅ Implement database CRUD                       │   │
│  │  ✅ Add SQLAlchemy integration                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Deliverables:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  - Persistent storage                              │   │
│  │  - QR management endpoints                         │   │
│  │  - Database migrations                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Phase 3: Analytics (Week 3)

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 3: ANALYTICS                      │
│                                                             │
│  Tasks:                                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Create ScanEvent model                         │   │
│  │  ✅ Log scan events                                │   │
│  │  ✅ Add location tracking                          │   │
│  │  ✅ Build analytics endpoints                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Deliverables:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  - Complete analytics pipeline                     │   │
│  │  - Dashboard endpoints                              │   │
│  │  - Visitor tracking                                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Phase 4: Performance (Week 4)

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE 4: PERFORMANCE                    │
│                                                             │
│  Tasks:                                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ Add Redis cache                               │   │
│  │  ✅ Database indexing                             │   │
│  │  ✅ Connection pooling                            │   │
│  │  ✅ Performance testing                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Deliverables:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  - Cached redirects                                │   │
│  │  - Optimized queries                               │   │
│  │  - Load testing results                            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 13.3 Scaling Strategies

```
┌─────────────────────────────────────────────────────────────┐
│                  SCALING STRATEGIES                        │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  VERTICAL SCALING                                 │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Upgrade server hardware                  │ │   │
│  │  │  - More RAM, CPU                            │ │   │
│  │  │  - Faster storage                           │ │   │
│  │  │  - Limit: Single server capacity            │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  HORIZONTAL SCALING                               │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Multiple servers                         │ │   │
│  │  │  - Load balancer                             │ │   │
│  │  │  - Database replication                      │ │   │
│  │  │  - Distributed cache                         │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  OPTIMIZATION                                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Caching frequently accessed codes        │ │   │
│  │  │  - Database indexing                        │ │   │
│  │  │  - Query optimization                        │ │   │
│  │  │  - CDN for static assets                     │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 13.4 Production Checklist

```
┌─────────────────────────────────────────────────────────────┐
│                  PRODUCTION CHECKLIST                      │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  SECURITY                                         │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  ✅ HTTPS enabled                            │ │   │
│  │  │  ✅ URL validation                           │ │   │
│  │  │  ✅ Rate limiting                            │ │   │
│  │  │  ✅ Input sanitization                        │ │   │
│  │  │  ✅ Environment variables                    │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  PERFORMANCE                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  ✅ Database indexing                        │ │   │
│  │  │  ✅ Connection pooling                       │ │   │
│  │  │  ✅ Caching strategy                         │ │   │
│  │  │  ✅ Query optimization                       │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  RELIABILITY                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  ✅ Error handling                          │ │   │
│  │  │  ✅ Logging                                  │ │   │
│  │  │  ✅ Monitoring                               │ │   │
│  │  │  ✅ Backups                                  │ │   │
│  │  │  ✅ Health checks                            │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  SCALABILITY                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  ✅ Horizontal scaling ready                 │ │   │
│  │  │  ✅ Load balancer                            │ │   │
│  │  │  ✅ Stateless design                         │ │   │
│  │  │  ✅ Auto-scaling configured                   │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 13.5 Next Steps

```
┌─────────────────────────────────────────────────────────────┐
│                      NEXT STEPS                            │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CONTINUE BUILDING                                │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Add authentication                        │ │   │
│  │  │  - User management                          │ │   │
│  │  │  - Payment integration                       │ │   │
│  │  │  - Advanced analytics                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  LEARN MORE                                      │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Advanced caching strategies              │ │   │
│  │  │  - Database sharding                        │ │   │
│  │  │  - Event-driven architecture                 │ │   │
│  │  │  - Microservices design                     │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What are the phases of redirect architecture evolution?

**Question 2:** How do you scale a redirect service?

**Question 3:** What's on the production checklist?

---

## 📝 Section Summary

- **Architecture evolves** from basic to distributed
- **Phases** include core, database, analytics, performance
- **Scaling** strategies include vertical and horizontal
- **Production checklist** ensures reliability
- **Next steps** add advanced features

---

---

# SECTION 14

## REDIRECT CHEAT SHEET

---

### 📖 Learning Objectives

- Quick reference for redirects
- Common patterns and code
- Status codes reference
- Best practices summary

---

## 14.1 HTTP Status Codes

```
┌─────────────────────────────────────────────────────────────┐
│                  HTTP STATUS CODES                         │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CODE  │ NAME              │ USE                   │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  301   │ Moved Permanently │ Permanent redirect    │   │
│  │  302   │ Found             │ Temporary redirect    │   │
│  │  307   │ Temporary Redirect│ Temporary (keep POST) │   │
│  │  308   │ Permanent Redirect│ Permanent (keep POST) │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 14.2 FastAPI Redirect Patterns

### Basic Redirect

```python
from fastapi.responses import RedirectResponse

@app.get("/old")
async def redirect():
    return RedirectResponse(url="/new", status_code=302)
```

### Redirect with Parameter

```python
@app.get("/r/{code}")
async def redirect_qr(code: str):
    destination = get_destination(code)
    return RedirectResponse(url=destination, status_code=302)
```

### Redirect with Headers

```python
@app.get("/r/{code}")
async def redirect_qr(code: str):
    response = RedirectResponse(url=destination, status_code=302)
    response.headers["X-Track-ID"] = code
    return response
```

### Redirect with Error Handling

```python
@app.get("/r/{code}")
async def redirect_qr(code: str):
    destination = get_destination(code)
    if not destination:
        raise HTTPException(status_code=404, detail="Not found")
    return RedirectResponse(url=destination, status_code=302)
```

---

## 14.3 Route Parameter Patterns

```
┌─────────────────────────────────────────────────────────────┐
│                  ROUTE PARAMETER PATTERNS                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  BASIC                                            │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  @app.get("/r/{code}")                     │ │   │
│  │  │  def redirect(code: str):                  │ │   │
│  │  │      # code = "abc123"                     │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  WITH QUERY PARAMETERS                             │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  @app.get("/r/{code}")                     │ │   │
│  │  │  def redirect(code: str, ref: str = None): │ │   │
│  │  │      # URL: /r/abc123?ref=email            │ │   │
│  │  │      # ref = "email"                        │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  MULTIPLE PARAMETERS                               │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  @app.get("/{user}/{code}")                │ │   │
│  │  │  def redirect(user: str, code: str):       │ │   │
│  │  │      # URL: /john/abc123                    │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 14.4 Common Functions

### URL Validation

```python
from urllib.parse import urlparse

def validate_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in ['http', 'https'] and parsed.netloc

def fix_url(url: str) -> str:
    if not url.startswith('http'):
        return f'https://{url}'
    return url
```

### Code Generation

```python
import random
import string

def generate_code(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
```

### Visitor ID

```python
import hashlib

def generate_visitor_id(ip: str, user_agent: str) -> str:
    data = f"{ip}|{user_agent}"
    return hashlib.md5(data.encode()).hexdigest()
```

---

## 14.5 Best Practices

```
┌─────────────────────────────────────────────────────────────┐
│                     BEST PRACTICES                         │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ✅ DO                                             │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Use 302 for QR redirects                  │ │   │
│  │  │  - Log analytics before redirecting          │ │   │
│  │  │  - Validate destination URLs                  │ │   │
│  │  │  - Handle errors gracefully                   │ │   │
│  │  │  - Use caching for performance                │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ❌ DON'T                                          │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Don't use 301 unless permanent           │ │   │
│  │  │  - Don't skip analytics logging              │ │   │
│  │  │  - Don't redirect to unsafe URLs             │ │   │
│  │  │  - Don't create redirect loops               │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 14.6 Error Responses

```
┌─────────────────────────────────────────────────────────────┐
│                     ERROR RESPONSES                        │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CODE  │ MEANING                                   │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  400   │ Bad Request - Invalid short code          │   │
│  │  404   │ Not Found - QR code doesn't exist         │   │
│  │  410   │ Gone - QR code expired/deactivated        │   │
│  │  500   │ Internal Server Error - Something broke   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 14.7 Quick Reference Code

```python
# Complete redirect endpoint
@app.get("/r/{short_code}")
async def redirect_qr(
    short_code: str,
    request: Request,
    db: Session = Depends(get_db)
):
    # 1. Validate
    if not short_code:
        raise HTTPException(400, "Invalid code")
    
    # 2. Lookup
    qr = db.query(QRCode).filter(
        QRCode.short_code == short_code,
        QRCode.active == True
    ).first()
    
    if not qr:
        raise HTTPException(404, "QR not found")
    
    # 3. Log
    scan = ScanEvent(
        qr_id=qr.id,
        ip=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    db.add(scan)
    qr.scans += 1
    db.commit()
    
    # 4. Redirect
    return RedirectResponse(
        url=qr.destination,
        status_code=302
    )
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What status code should you use for QR redirects?

**Question 2:** How do you generate unique short codes?

**Question 3:** What's the complete redirect pattern?

---

## 📝 Section Summary

- **Status codes** determine redirect behavior
- **FastAPI patterns** make redirects easy
- **Best practices** ensure reliability
- **Error handling** improves user experience

---

---

# SECTION 15

## TROUBLESHOOTING GUIDE

---

### 📖 Learning Objectives

- Diagnose common redirect issues
- Fix routing problems
- Solve database lookup failures
- Handle performance issues

---

## 15.1 Redirect Failures

### Issue: "Too Many Redirects"

```
┌─────────────────────────────────────────────────────────────┐
│                  "TOO MANY REDIRECTS"                      │
│                                                             │
│  Symptom:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Browser shows: "This page isn't working"          │   │
│  │  "ERR_TOO_MANY_REDIRECTS"                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Cause:                                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Redirect loop: A → B → A → B → ...              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Solution:                                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Check redirect targets                         │   │
│  │  2. Ensure no self-referential redirects           │   │
│  │  3. Add loop detection                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Code:                                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  def redirect_qr(code):                           │   │
│  │      if code == destination:                       │   │
│  │          raise HTTPException(400, "Loop detected")│   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Issue: 404 Not Found

```
┌─────────────────────────────────────────────────────────────┐
│                     404 NOT FOUND                          │
│                                                             │
│  Symptom:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Browser shows: "404 Not Found"                    │   │
│  │  "QR code not found"                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Causes:                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. QR code doesn't exist in database              │   │
│  │  2. QR code is inactive/deleted                    │   │
│  │  3. Wrong short code format                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Solutions:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Check database for code                       │   │
│  │  2. Verify code is active                         │   │
│  │  3. Check for typos in short code                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Debug:                                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  logger.info(f"Looking up code: {short_code}")   │   │
│  │  qr = db.query(QRCode).filter(...).first()       │   │
│  │  logger.info(f"Found: {qr}")                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 15.2 Route Mismatches

### Issue: Route Not Matching

```
┌─────────────────────────────────────────────────────────────┐
│                    ROUTE NOT MATCHING                      │
│                                                             │
│  Symptom:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Request: GET /r/abc123                            │   │
│  │  Response: {"detail": "Not Found"}                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Causes:                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Route pattern mismatch                         │   │
│  │  2. Wrong HTTP method                              │   │
│  │  3. Trailing slash issues                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Solutions:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  # Check route definition                         │   │
│  │  @app.get("/r/{short_code}")  # ✅ Correct        │   │
│  │  @app.get("/r/{code}")        # ✅ Also works    │   │
│  │  @app.get("/r")               # ❌ Wrong         │   │
│  │                                                   │   │
│  │  # Check HTTP method                               │   │
│  │  # Use @app.get() for GET requests                │   │
│  │  # Use @app.post() for POST requests              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 15.3 Invalid URLs

### Issue: Broken Redirect Destination

```
┌─────────────────────────────────────────────────────────────┐
│                   BROKEN DESTINATION                       │
│                                                             │
│  Symptom:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Redirect works but destination is broken          │   │
│  │  User sees: "This site can't be reached"           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Causes:                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Missing http:// or https://                    │   │
│  │  2. Domain doesn't exist                           │   │
│  │  3. URL has typos                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Solutions:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  # Validate before storing                         │   │
│  │  def validate_url(url: str) -> bool:              │   │
│  │      parsed = urlparse(url)                       │   │
│  │      return parsed.scheme in ['http', 'https']   │   │
│  │                                                   │   │
│  │  # Auto-fix common issues                         │   │
│  │  if not url.startswith('http'):                   │   │
│  │      url = f'https://{url}'                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 15.4 Performance Issues

### Issue: Slow Redirects

```
┌─────────────────────────────────────────────────────────────┐
│                     SLOW REDIRECTS                         │
│                                                             │
│  Symptom:                                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Redirect takes > 500ms to complete               │   │
│  │  Users experience delays                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Causes:                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. Slow database queries                          │   │
│  │  2. Missing indexes                                │   │
│  │  3. No caching                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Solutions:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  # Add database index                              │   │
│  │  CREATE INDEX idx_short_code ON qrs(short_code);  │   │
│  │                                                   │   │
│  │  # Add caching                                    │   │
│  │  @lru_cache(maxsize=1000)                         │   │
│  │  def get_destination(code):                       │   │
│  │      return db.query(...)                         │   │
│  │                                                   │   │
│  │  # Use Redis                                      │   │
│  │  cached = redis.get(f"qr:{code}")                │   │
│  │  if cached: return cached                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 15.5 Troubleshooting Steps

```
┌─────────────────────────────────────────────────────────────┐
│                  TROUBLESHOOTING STEPS                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  STEP 1: Check Logs                               │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Application logs                         │ │   │
│  │  │  - Database logs                            │ │   │
│  │  │  - Server logs                              │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  STEP 2: Test Endpoints                           │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Use curl to test                         │ │   │
│  │  │  - Check response codes                      │ │   ││  │  │  - Verify redirect Location header           │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  STEP 3: Check Database                           │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Verify record exists                     │ │   │
│  │  │  - Check active status                       │ │   │
│  │  │  - Validate destination URL                  │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  STEP 4: Test Redirect Chain                     │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  - Follow redirects manually                 │ │   │
│  │  │  - Check for loops                           │ │   │
│  │  │  - Verify final destination                  │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 15.6 Common Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| `404 Not Found` | QR code doesn't exist | Check short code |
| `410 Gone` | QR code expired/deactivated | Reactivate or recreate |
| `400 Bad Request` | Invalid short code | Validate format |
| `502 Bad Gateway` | Server issue | Check server status |
| `ERR_TOO_MANY_REDIRECTS` | Redirect loop | Check redirect chain |

---

## 15.7 Debug Commands

```bash
# Test redirect
curl -v http://localhost:8000/r/abc123

# Follow redirects
curl -L http://localhost:8000/r/abc123

# Show headers only
curl -I http://localhost:8000/r/abc123

# Check database
psql -d sqanalytics -c "SELECT * FROM qrs WHERE short_code='abc123';"

# Clear cache
redis-cli del qr:abc123

# View logs
tail -f /var/log/sqanalytics/access.log
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What causes "too many redirects"?

**Question 2:** How do you debug 404 errors?

**Question 3:** How do you fix slow redirects?

---

## 📝 Section Summary

- **Common issues** include loops, 404, and slow redirects
- **Debugging** starts with logs and tests
- **Database checks** verify record existence
- **Performance fixes** include indexes and caching

---

---

# SECTION 16

## INTERVIEW PREPARATION GUIDE

---

### 📖 Learning Objectives

- Prepare for redirect-related interviews
- Answer beginner and advanced questions
- Solve scenario-based problems
- Demonstrate architecture knowledge

---

## 16.1 Beginner Questions

### Question 1: What is an HTTP redirect?

**Answer:** An HTTP redirect is a server response (3xx status code) that tells the browser to go to a different URL. The server sends a `Location` header with the new URL, and the browser automatically makes a new request to that URL.

### Question 2: What's the difference between 301 and 302?

**Answer:**
- **301** means "Moved Permanently" - browsers cache this and update bookmarks. Search engines transfer link equity.
- **302** means "Found" (temporary) - browsers don't cache it. The original URL remains in search results.

### Question 3: How does a URL shortener work?

**Answer:** A URL shortener generates a unique short code for a long URL, stores the mapping in a database, and redirects when someone visits the short URL. The flow is:
1. Create: Generate code, store {code → long_url}
2. Redirect: Look up code, redirect to long_url

### Question 4: What is RedirectResponse in FastAPI?

**Answer:** `RedirectResponse` is a FastAPI response class that sends an HTTP redirect. Usage:
```python
from fastapi.responses import RedirectResponse
return RedirectResponse(url="https://example.com", status_code=302)
```

---

## 16.2 Intermediate Questions

### Question 1: Why use a redirect service for QR codes?

**Answer:** Redirect services provide:
- **Analytics:** Track who scans, when, where
- **Flexibility:** Change destination without reprinting QR
- **Security:** Block malicious destinations
- **A/B testing:** Rotate destinations

### Question 2: How do you track QR scans?

**Answer:** On every redirect request:
1. Extract IP, User Agent, Referer
2. Log scan event with timestamp
3. Track location (GeoIP)
4. Identify device type
5. Count unique visitors

### Question 3: What's the N+1 problem in redirect services?

**Answer:** When each redirect triggers multiple database queries (e.g., lookup QR, log analytics, update stats). Solution: Combine queries, use batch operations, or implement caching.

### Question 4: How would you scale a redirect service?

**Answer:**
1. **Vertical scaling:** Upgrade server hardware
2. **Horizontal scaling:** Add more servers behind load balancer
3. **Caching:** Use Redis for frequent codes
4. **Database optimization:** Indexes, replication
5. **CDN:** Cache redirects at edge

---

## 16.3 Scenario-Based Questions

### Scenario 1: QR Code Not Redirecting

**Problem:** Users report scanning a QR code but getting a 404 error.

**Analysis:**
1. Short code doesn't exist in database
2. QR code is inactive/expired
3. Wrong URL encoded in QR
4. Database connection issue

**Solution:**
1. Check database for short code
2. Verify active status
3. Test endpoint with curl
4. Check logs for errors

### Scenario 2: Slow Redirects

**Problem:** Redirects taking 2+ seconds.

**Analysis:**
1. Missing database index on short_code
2. No caching
3. Slow GeoIP lookup
4. Database connection pool exhausted

**Solution:**
1. Add database index
2. Implement Redis cache
3. Cache GeoIP results
4. Increase connection pool size

### Scenario 3: Destination URL Broken

**Problem:** Redirect works but user gets "site can't be reached".

**Analysis:**
1. Missing protocol (http://)
2. Domain doesn't exist
3. SSL certificate issue
4. URL has typos

**Solution:**
1. Validate URLs before storing
2. Auto-fix missing protocol
3. Check domain availability
4. Use HTTPS by default

---

## 16.4 Architecture Questions

### Question 1: Design a QR redirect service

**Answer:**

```
Components:
1. QR Generation Service
   - Generate short codes
   - Create QR images

2. Redirect Service
   - Look up codes
   - Log analytics
   - Redirect to destination

3. Analytics Service
   - Process scan events
   - Generate reports

4. Database
   - QR codes: {code, destination, stats}
   - Scan events: {qr_id, timestamp, location}

5. Cache
   - Redis for frequently accessed codes

Scale:
- Load balancer
- Multiple app servers
- Database replication
- CDN for QR images
```

### Question 2: How would you handle millions of scans per day?

**Answer:**

1. **Database:** Use sharding or partitioning
2. **Caching:** Redis cluster for hot codes
3. **Async:** Use async processing for analytics
4. **Batch:** Batch write scan events
5. **Monitoring:** Track performance metrics

---

## 16.5 Interview Tips

```
┌─────────────────────────────────────────────────────────────┐
│                  INTERVIEW TIPS                            │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  DO                                              │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  ✅ Explain concepts clearly                │ │   │
│  │  │  ✅ Use examples                             │ │   │
│  │  │  ✅ Draw diagrams                           │ │   │
│  │  │  ✅ Discuss trade-offs                       │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  DON'T                                            │   │
│  │  ┌──────────────────────────────────────────────┐ │   │
│  │  │  ❌ Give one-word answers                    │ │   │
│  │  │  ❌ Ignore scalability                       │ │   │
│  │  │  ❌ Forget about error handling              │ │   │
│  │  │  ❌ Overlook monitoring                      │ │   │
│  │  └──────────────────────────────────────────────┘ │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 16.6 Key Concepts to Know

| Concept | Why It Matters |
|---------|---------------|
| HTTP Status Codes | Redirect behavior |
| URL Shortening | Core functionality |
| Analytics Tracking | Value proposition |
| Caching | Performance |
| Scaling | Growth handling |
| Security | Protect users |

---

## 🔍 Knowledge Checkpoint

**Question 1:** How do you explain redirects to a non-technical person?

**Question 2:** What's the most important consideration for a redirect service?

**Question 3:** How would you design a system that handles 1M redirects/day?

---

## 📝 Section Summary

- **Beginner questions** test basic understanding
- **Intermediate questions** cover practical implementation
- **Scenario questions** assess problem-solving
- **Architecture questions** evaluate system design
- **Preparation** is key to interview success

---

---

# APPENDIX

## Quick Reference

### Status Codes
- **301**: Moved Permanently
- **302**: Found (Temporary)
- **307**: Temporary Redirect
- **308**: Permanent Redirect

### FastAPI Redirect
```python
return RedirectResponse(url="https://example.com", status_code=302)
```

### Route Parameter
```python
@app.get("/r/{short_code}")
async def redirect(short_code: str):
    # short_code extracted from URL
    pass
```

### Common Patterns
```python
# Lookup and redirect
qr = get_qr_by_code(db, short_code)
if not qr:
    raise HTTPException(404, "Not found")
return RedirectResponse(url=qr.destination, status_code=302)
```

---

## Glossary

| Term | Definition |
|------|------------|
| **Redirect** | Server response to go to another URL |
| **Short Code** | Unique identifier in a URL |
| **QR Code** | 2D barcode encoding a URL |
| **Analytics** | Tracking and analyzing user behavior |
| **Caching** | Storing data for faster access |
| **404** | Not Found status code |
| **302** | Temporary redirect status code |

---

## Resources

### Documentation
- [FastAPI Redirects](https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Tools
- **PostgreSQL**: Database
- **Redis**: Caching
- **GeoIP**: Location tracking

---

# END OF HANDBOOK

---

*"Build redirect services. Track every click. Master web request flow."*

---

**SQAnalytics - Smart QR Analytics Platform**

---

---

*This concludes the "HTTP Redirects & URL Routing for Modern Web Applications" handbook.*