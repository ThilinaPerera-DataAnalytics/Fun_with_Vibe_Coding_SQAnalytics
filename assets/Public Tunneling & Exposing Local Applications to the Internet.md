# Public Tunneling & Exposing Local Applications to the Internet

## A Practical Beginner Guide for Testing SQAnalytics, APIs, QR Platforms & Full Stack Applications from Real Devices

---

# Cover Page

<div style="text-align: center; padding: 40px 0;">

# Public Tunneling & Exposing Local Applications to the Internet

## A Practical Beginner Guide for Testing SQAnalytics, APIs, QR Platforms & Full Stack Applications from Real Devices

**Version 1.0**

---

### Learning Path

```mermaid
graph LR
    A[Local Development] --> B[Public Tunnel]
    B --> C[Internet Access]
    C --> D[Mobile Testing]
    D --> E[QR Scanning]
    E --> F[Production Deployment]
```

### Project Context: SQAnalytics

A Smart QR Analytics Platform built with:
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Enterprise-grade database
- **SQLAlchemy** - ORM for database interaction
- **ngrok** - Public tunneling
- **Cloudflare Tunnel** - Alternative tunneling

---

*"From Localhost to the World: Exposing Your Development Environment for Real-World Testing"*

</div>

---

# Learning Objectives

By completing this handbook, you will master:

### Fundamental Concepts
- **Localhost Limitations** - Why 127.0.0.1 is only for you
- **Network Fundamentals** - Localhost vs LAN vs Internet
- **Public Tunneling** - What it is and why it matters
- **Reverse Proxy Concepts** - How tunnels work

### Practical Skills
- **ngrok Installation** - Setting up tunneling
- **API Exposure** - Making FastAPI publicly accessible
- **Mobile Testing** - Testing from real devices
- **QR Scanning** - Testing full QR workflows
- **Cloudflare Tunnel** - Alternative tunneling solution

### Production Application
- **Pre-Deployment Validation** - Testing before launch
- **Security Considerations** - Safe tunneling practices
- **Transition to Production** - Moving from tunnel to cloud
- **Team Collaboration** - Sharing development environments

---

# Executive Summary

## The Problem Visualized

```mermaid
graph LR
    subgraph "Localhost Only"
        L[Laptop] -->|Can Access| A[FastAPI on localhost:8000]
        M[Mobile Phone] -->|Cannot Access| A
    end
```

## The Solution

```mermaid
graph LR
    subgraph "With Public Tunneling"
        L[Laptop] -->|Local App| T[ngrok Tunnel]
        T -->|Public URL| I[Internet]
        M[Mobile Phone] -->|Accesses| I
        I -->|Routes| L
    end
```

## Why This Matters for SQAnalytics

```mermaid
graph TD
    subgraph "QR Platform Testing"
        Q1[QR Code Printed] -->|Contains| URL[Localhost URL]
        URL -->|Phone Scans| F[Fails - Cannot Access]
        
        Q2[QR Code Printed] -->|Contains| T[Public Tunnel URL]
        T -->|Phone Scans| S[Success - Access API]
        S --> A[Analytics Captured]
        A --> R[Redirect to Destination]
    end
```

## The Complete Picture

```mermaid
graph TD
    subgraph "Development Environment"
        D[Developer Laptop] --> F[FastAPI :8000]
        F --> T[Public Tunnel]
    end
    
    subgraph "Internet"
        T --> P[Public URL]
    end
    
    subgraph "Testing Devices"
        M[Mobile Phone] --> P
        T[Tablet] --> P
        C[Other Computer] --> P
        QR[QR Scanner] --> P
    end
    
    P --> F
```

---

# Table of Contents

1. [Section 1: Why Localhost Cannot Be Reached From Other Devices](#section-1)
2. [Section 2: Localhost vs LAN vs Public Internet](#section-2)
3. [Section 3: What Is Public Tunneling?](#section-3)
4. [Section 4: How ngrok Works](#section-4)
5. [Section 5: Installing & Configuring ngrok](#section-5)
6. [Section 6: Testing FastAPI Through ngrok](#section-6)
7. [Section 7: QR Analytics Case Study](#section-7)
8. [Section 8: Cloudflare Tunnel](#section-8)
9. [Section 9: Tunnel Security Considerations](#section-9)
10. [Section 10: Common Developer Mistakes](#section-10)
11. [Section 11: Transition From Tunnel To Production](#section-11)
12. [Section 12: SQAnalytics Case Study](#section-12)
13. [Section 13: Hands-On Exercises](#section-13)
14. [Tunneling Roadmap](#roadmap)
15. [Tunneling Cheat Sheet](#cheat-sheet)
16. [Troubleshooting Guide](#troubleshooting)
17. [Interview Preparation Guide](#interview)

---

# Section 1: Why Localhost Cannot Be Reached From Other Devices

## The Simple Explanation

**Localhost** (127.0.0.1) is a special address that only your computer can access. When you run a server on localhost, it's only accessible from the same machine.

### The House Analogy

```mermaid
graph TD
    subgraph "Localhost = Your House"
        Y[You] -->|Inside House| Y2[Your Computer]
        Y2 -->|Can Access| Y3[Localhost Services]
        
        N[Neighbor] -->|Outside House| N2[Can't Access]
        N2 -->|No Access| Y3
    end
```

## The Technical Reality

```mermaid
graph LR
    subgraph "Your Computer"
        A[Application] --> B[localhost:8000]
        B --> C[127.0.0.1]
        C --> D[Loopback Interface]
    end
    
    subgraph "Loopback Interface"
        D --> E[Only Your Computer]
    end
```

## Common Misconceptions

```mermaid
graph TD
    subgraph "Misconceptions"
        M1["Running on localhost means everyone can access it"] -->|Reality| R1["Only your computer can access"]
        M2["localhost is just another website"] -->|Reality| R2["It's your own computer"]
        M3["I can test QR codes with localhost"] -->|Reality| R3["QR scans from phones will fail"]
    end
```

## Why QR Scans Fail

```mermaid
sequenceDiagram
    participant P as Phone
    participant Q as QR Code
    participant L as Localhost
    participant U as User
    
    U->>Q: Scan QR Code
    Q-->>P: Contains localhost URL
    P->>L: Try to access localhost
    L-->>P: Connection Refused
    P-->>U: Error Page
    Note over P,L: Phone can't access your computer's localhost
```

### The QR Flow Failure

```mermaid
graph TD
    subgraph "What QR Contains"
        URL["localhost:8000/redirect/abc123"]
    end
    
    subgraph "When Scanned"
        P[Phone] -->|Requests| URL
        URL -->|Cannot Reach| F[Failed]
        F -->|Shows| E[Error]
    end
```

---

## 🔍 Learning Checkpoint

1. What is localhost?
   - a) A website everyone can access
   - b) Your own computer's loopback address
   - c) A public server
   - d) A domain name

2. Can other devices access your localhost?
   - a) Yes, always
   - b) No, it's only accessible from your computer
   - c) Sometimes
   - d) Only with special permission

**[Answers: 1-b, 2-b]**

---

# Section 2: Localhost vs LAN vs Public Internet

## The Three Layers

```mermaid
graph TD
    subgraph "Network Layers"
        L1[Localhost] -->|"127.0.0.1"| A1[Only your computer]
        L2[LAN] -->|"192.168.x.x"| A2[Same network]
        L3[Internet] -->|"Public IP"| A3[Entire world]
    end
```

## Detailed Comparison

### 1. Localhost (127.0.0.1)

```mermaid
graph LR
    subgraph "Localhost"
        C[Your Computer] -->|Loopback| L[127.0.0.1]
        L -->|Only| C
    end
```

**Characteristics:**
- Only accessible from your machine
- Used for development
- No network required
- Fast, but isolated

### 2. LAN (Local Area Network)

```mermaid
graph LR
    subgraph "LAN"
        C1[Computer 1] -->|192.168.1.10| R[Router]
        C2[Computer 2] -->|192.168.1.20| R
        R -->|Network| C1
        R -->|Network| C2
    end
```

**Characteristics:**
- Same network (Wi-Fi/Ethernet)
- Private IP addresses (192.168.x.x)
- Devices on same network can communicate
- Not accessible from outside

### 3. Public Internet

```mermaid
graph LR
    subgraph "Internet"
        S[Server] -->|Public IP| I[Internet]
        I -->|Any Device| D1[Phone]
        I -->|Any Device| D2[Tablet]
        I -->|Any Device| D3[Computer]
    end
```

**Characteristics:**
- Public IP address
- Accessible from anywhere
- DNS resolution
- Hosted applications

## Network Address Types

| Address Type | Example | Scope | Access |
|--------------|---------|-------|--------|
| **Localhost** | `127.0.0.1` | Single device | Self only |
| **Private IP** | `192.168.1.10` | Local network | Same network |
| **Public IP** | `8.8.8.8` | Internet | Anywhere |
| **Domain** | `sqanalytics.com` | Internet | Anywhere |

## QR Testing Requirements

```mermaid
graph TD
    subgraph "QR Testing Environments"
        T1[Localhost] -->|"Fails"| R1[Phone can't access]
        T2[LAN] -->|"Works in office"| R2[Phone on same Wi-Fi]
        T3[Public Tunnel] -->|"Works anywhere"| R3[All devices]
        T4[Production] -->|"Works everywhere"| R4[All devices]
    end
```

## Practical Example

```python
# Different address types in FastAPI

# 1. Localhost only (default)
uvicorn.run(app, host="127.0.0.1", port=8000)
# Only accessible from your computer

# 2. LAN accessible
uvicorn.run(app, host="0.0.0.0", port=8000)
# Accessible from other devices on same network
# Use: http://192.168.1.10:8000

# 3. With tunneling
# Use ngrok to make it publicly accessible
ngrok http 8000
# Gives: https://abc123.ngrok.io
```

---

## 📊 Network Layer Summary

| Layer | Address | Who Can Access | Use Case |
|-------|---------|---------------|----------|
| **Localhost** | `127.0.0.1` | Only you | Development |
| **LAN** | `192.168.x.x` | Same network | Team testing |
| **Tunnel** | `https://abc.ngrok.io` | Anyone with URL | Public testing |
| **Production** | `https://domain.com` | Everyone | Live application |

---

# Section 3: What Is Public Tunneling?

## The Simple Explanation

**Public Tunneling** is like creating a secret passage from your local computer to the internet. It allows your local development server to be accessible from anywhere in the world.

### The Secret Tunnel Analogy

```mermaid
graph LR
    subgraph "Secret Tunnel"
        L[Local Computer] -->|Tunnel| T[Tunnel Service]
        T -->|Public URL| I[Internet]
        I -->|Access| D1[Phone]
        I -->|Access| D2[Tablet]
        I -->|Access| D3[World]
    end
```

## What Tunneling Solves

```mermaid
graph TD
    subgraph "Problems Solved"
        P1[QR scanning failure] --> S1[QR works from anywhere]
        P2[Can't share dev environment] --> S2[Share public URL]
        P3[Mobile testing impossible] --> S3[Test on real devices]
        P4[API testing difficult] --> S4[Test APIs from anywhere]
        P5[Client demos impossible] --> S5[Demonstrate work]
    end
```

## How It Works

```mermaid
sequenceDiagram
    participant L as Local Server
    participant T as Tunnel Service
    participant I as Internet
    participant D as Device
    
    Note over L,T: Connection Established
    L->>T: Open tunnel
    T-->>L: Public URL assigned
    
    Note over D,I: External Access
    D->>I: Request public URL
    I->>T: Forward request
    T->>L: Route to local server
    L-->>T: Response
    T-->>I: Forward response
    I-->>D: Response received
```

## Business Use Cases

### 1. API Testing

```mermaid
graph LR
    D[Developer] -->|Creates API| L[Local FastAPI]
    L -->|Tunnel| T[Public URL]
    C[Client] -->|Tests API| T
```

### 2. Mobile App Testing

```mermaid
graph LR
    A[App Developer] -->|Local Server| L[Local Backend]
    L -->|Tunnel| T[Public URL]
    M[Mobile App] -->|Connects| T
```

### 3. QR Platform Testing

```mermaid
graph LR
    Q[QR Code] -->|Scans| P[Phone]
    P -->|Redirects| T[Public URL]
    T -->|Routes| L[Local Server]
    L -->|Analytics| A[Captured]
```

### 4. Client Demos

```mermaid
graph LR
    D[Developer] -->|Local App| L[Local Server]
    L -->|Tunnel| T[Public URL]
    C[Client] -->|Views Demo| T
```

## Types of Tunneling Solutions

```mermaid
graph TD
    subgraph "Tunneling Tools"
        N[ngrok] -->|"Most Popular"| F1[Free + Paid]
        C[Cloudflare Tunnel] -->|"Enterprise Grade"| F2[Free + Paid]
        L[Local Tunnel] -->|"Open Source"| F3[Free]
        S[SSH Tunnel] -->|"Technical"| F4[Free]
    end
```

---

## 🔍 Tunneling Benefits

```mermaid
graph TD
    subgraph "Key Benefits"
        B1[Accessible] --> A1[From anywhere]
        B2[Shareable] --> A2[Send URL to anyone]
        B3[Testable] --> A3[Real devices]
        B4[Fast] --> A4[No deployment needed]
        B5[Secure] --> A5[Encrypted tunnels]
    end
```

---

# Section 4: How ngrok Works

## ngrok Architecture

```mermaid
graph TD
    subgraph "ngrok Components"
        C[Client] -->|Local App| A[Application]
        A -->|Process| P[ngrok Agent]
        P -->|Tunnel| N[ngrok Cloud]
        N -->|Public URL| I[Internet]
        I -->|Access| D[Devices]
    end
```

## The Communication Flow

```mermaid
sequenceDiagram
    participant A as Application
    participant N as ngrok Agent
    participant C as ngrok Cloud
    participant U as User
    
    A->>N: Start local server
    N->>C: Establish tunnel
    C-->>N: Assign public URL
    
    U->>C: Request public URL
    C->>N: Forward request
    N->>A: Route to app
    A-->>N: Response
    N-->>C: Forward response
    C-->>U: Return response
```

## ngrok Components Explained

### 1. Local Application

```python
# FastAPI running locally
uvicorn.run(app, host="127.0.0.1", port=8000)
```

### 2. ngrok Agent

```bash
# ngrok client running on your machine
ngrok http 8000
```

### 3. ngrok Cloud Service

```mermaid
graph LR
    subgraph "ngrok Cloud"
        E[Edge] -->|Routes| T[Tunnels]
        T -->|Manages| S[Sessions]
        S -->|Provides| U[URLs]
    end
```

### 4. Public URL

```
https://abc123.ngrok.io
```

## Request Flow Deep Dive

```mermaid
graph TD
    subgraph "Incoming Request"
        R[Request] -->|To Public URL| C[ngrok Cloud]
        C -->|Encrypted| T[Tunnel]
        T -->|To Local| N[ngrok Agent]
        N -->|To App| A[FastAPI]
    end
    
    subgraph "Response Flow"
        A -->|Response| N
        N -->|Encrypted| T
        T -->|To Cloud| C
        C -->|To Client| R2[Response]
    end
```

## ngrok Features

### Key Features

```mermaid
graph TD
    subgraph "ngrok Features"
        F1[HTTP/HTTPS Tunnels] --> U1[Web applications]
        F2[TCP Tunnels] --> U2[Database, SSH]
        F3[Web Interface] --> U3[Inspect requests]
        F4[Replay Requests] --> U4[Testing]
        F5[Basic Auth] --> U5[Security]
        F6[Reserved Domains] --> U6[Professional]
    end
```

### Feature Comparison

| Feature | Free Plan | Paid Plan |
|---------|-----------|-----------|
| **Tunnels** | 1 | Unlimited |
| **URL** | Random | Custom sub-domain |
| **TCP Tunnels** | Limited | Yes |
| **Web Interface** | Yes | Yes |
| **Request Inspection** | Yes | Yes |
| **Basic Auth** | No | Yes |
| **Reserved Domains** | No | Yes |

---

## 🎯 Why ngrok is Popular

1. **Simple Setup** - One command to start
2. **No Configuration** - Works out of box
3. **Developer Friendly** - Great for testing
4. **Free Tier** - Perfect for development
5. **Secure** - HTTPS by default

---

# Section 5: Installing & Configuring ngrok

## Installation Guide

### 1. Download ngrok

```mermaid
graph LR
    A[Visit ngrok.com] --> B[Download for your OS]
    B --> C[Extract/Install]
    C --> D[Ready to use]
```

### Step-by-Step Installation

#### macOS

```bash
# Download via Homebrew
brew install ngrok

# Or download manually
curl -O https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip
unzip ngrok-stable-darwin-amd64.zip
sudo mv ngrok /usr/local/bin
```

#### Windows

```bash
# Download the Windows version
# Extract ngrok.exe
# Move to a folder in PATH
```

#### Linux

```bash
# Download for Linux
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin
```

### 2. Authentication

```bash
# Get your auth token from ngrok.com/dashboard
ngrok config add-authtoken YOUR_AUTH_TOKEN

# Or set environment variable
export NGROK_AUTHTOKEN=YOUR_AUTH_TOKEN
```

### 3. Verify Installation

```bash
# Check if installed correctly
ngrok --version

# Test with a simple tunnel
ngrok http 80
```

## Creating Your First Tunnel

### Basic Tunnel

```bash
# Expose port 8000 to the internet
ngrok http 8000
```

**Output:**

```
Session Status                online
Account                       Your Account (Plan: Free)
Version                       3.0.0
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123.ngrok.io -> http://localhost:8000
Forwarding                    http://abc123.ngrok.io -> http://localhost:8000
```

### Advanced Options

```bash
# HTTPS only
ngrok http 8000 --scheme=https

# Specific domain
ngrok http 8000 --domain=myapp.ngrok.io

# Multiple ports
ngrok http 8000 --host-header=localhost:8000

# With basic auth
ngrok http 8000 --basic-auth="username:password"
```

## ngrok Web Interface

```mermaid
graph LR
    subgraph "ngrok Web Interface"
        I[localhost:4040] --> R[Request Inspector]
        R -->|Shows| H[Headers]
        R -->|Shows| B[Body]
        R -->|Shows| Q[Query Params]
        R -->|Allows| P[Replay]
    end
```

### Using the Web Interface

```bash
# Open web interface
open http://localhost:4040
```

**Features:**

1. **Request Inspector** - View all requests
2. **Replay** - Resend requests for testing
3. **Filters** - Filter by status, method, etc.
4. **Details** - View headers, body, response

## Config File Options

### ngrok.yml Configuration

```yaml
# ~/.ngrok2/ngrok.yml
version: "2"
authtoken: YOUR_AUTH_TOKEN

tunnels:
  webapp:
    proto: http
    addr: 8000
    sub-domain: myapp
    basic_auth: "username:password"
    schemes:
      - https
  
  api:
    proto: http
    addr: 8001
    sub-domain: api
    host_header: rewrite
  
  qr:
    proto: http
    addr: 8002
    domain: qr.ngrok.io
```

### Using Config File

```bash
# Start specific tunnel
ngrok start webapp

# Start all tunnels
ngrok start --all
```

## Tunnel Status Monitoring

```mermaid
graph TD
    subgraph "Tunnel Status"
        S1[Active] --> I1[Requests flowing]
        S2[Idle] --> I2[Waiting for requests]
        S3[Error] --> I3[Check logs]
        S4[Offline] --> I4[Restart tunnel]
    end
```

### Checking Status

```bash
# Check tunnel status
ngrok status

# View logs
ngrok logs

# Stop all tunnels
ngrok stop
```

---

## 🎯 Quick Start Commands

```bash
# 1. Install
brew install ngrok

# 2. Authenticate
ngrok config add-authtoken YOUR_TOKEN

# 3. Expose FastAPI
uvicorn main:app --reload
ngrok http 8000

# 4. Your app is now at:
# https://abc123.ngrok.io
```

---

# Section 6: Testing FastAPI Through ngrok

## FastAPI Setup

### Basic FastAPI Application

```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from datetime import datetime

app = FastAPI(title="SQAnalytics QR Platform")

@app.get("/")
async def home():
    return {
        "message": "SQAnalytics API",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/scan/{qr_id}")
async def scan_qr(qr_id: str, request: Request):
    """Handle QR scan"""
    # Track analytics
    analytics = {
        "qr_id": qr_id,
        "timestamp": datetime.utcnow().isoformat(),
        "user_agent": request.headers.get("user-agent"),
        "ip": request.client.host
    }
    
    # Store analytics
    print(f"Scan recorded: {analytics}")
    
    # Redirect to destination
    return RedirectResponse(f"https://example.com/{qr_id}")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    """Analytics dashboard"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SQAnalytics Dashboard</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            .card { border: 1px solid #ccc; padding: 20px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>SQAnalytics Dashboard</h1>
        <div class="card">
            <h3>QR Scans</h3>
            <p>Total scans today: 42</p>
        </div>
        <div class="card">
            <h3>Recent Scans</h3>
            <ul>
                <li>QR-123 - 10:00 AM</li>
                <li>QR-456 - 09:30 AM</li>
                <li>QR-789 - 09:00 AM</li>
            </ul>
        </div>
    </body>
    </html>
    """
    return html
```

## Running FastAPI with ngrok

### Step 1: Start FastAPI

```bash
# Terminal 1: Start FastAPI
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Output:
# INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Start ngrok

```bash
# Terminal 2: Start ngrok
ngrok http 8000

# Output:
# Forwarding                    https://abc123.ngrok.io -> http://localhost:8000
```

### Step 3: Test the API

```bash
# Test with curl
curl https://abc123.ngrok.io/

# Test QR scan
curl https://abc123.ngrok.io/scan/QR123

# Test health
curl https://abc123.ngrok.io/health
```

## Mobile Testing Workflow

```mermaid
graph TD
    subgraph "Mobile Testing"
        M[Mobile Phone] -->|Scan QR| P[Public URL]
        P -->|Request| T[ngrok Tunnel]
        T -->|Route| F[FastAPI]
        F -->|Process| A[Analytics]
        A -->|Redirect| D[Destination]
        D -->|Display| B[Browser]
    end
```

### Testing from Mobile

1. **Get Public URL**
```bash
# From ngrok output
https://abc123.ngrok.io
```

2. **Create QR Code**

```python
import qrcode

# Your public URL
public_url = "https://abc123.ngrok.io/scan/QR123"

qr = qrcode.QRCode(version=1)
qr.add_data(public_url)
qr.make(fit=True)
img = qr.make_image()
img.save("test_qr.png")
```

3. **Test on Phone**
- Open QR code on another device
- Scan with phone
- Verify analytics captured
- Confirm redirect works

## Debugging Through ngrok

### Request Inspection

```bash
# Open ngrok web interface
open http://localhost:4040
```

**What You Can See:**

```mermaid
graph TD
    subgraph "ngrok Inspection"
        I[localhost:4040] --> R[Request List]
        R --> D[Request Details]
        D --> H[Headers]
        D --> B[Body]
        D --> Q[Query Params]
        D --> R2[Response]
        R --> RP[Replay Request]
    end
```

### Example Debug Flow

```mermaid
sequenceDiagram
    participant P as Phone
    participant N as ngrok
    participant F as FastAPI
    participant D as Dashboard
    
    P->>N: Request /scan/QR123
    N->>N: Log Request
    N->>F: Forward Request
    F->>F: Process QR
    F->>D: Log Analytics
    F-->>N: Redirect Response
    N-->>P: Redirect
    
    Note over N: Check localhost:4040
    Note over N: View request details
    Note over N: Verify analytics logged
```

## Testing QR Code Scanning

### Complete QR Test Workflow

```python
import qrcode
import requests
from fastapi.testclient import TestClient

def test_qr_scan():
    """
    Test QR scanning through public tunnel
    """
    # Get public URL from ngrok
    public_url = "https://abc123.ngrok.io"
    qr_url = f"{public_url}/scan/TEST123"
    
    # Generate QR
    qr = qrcode.QRCode(version=1)
    qr.add_data(qr_url)
    qr.make(fit=True)
    img = qr.make_image()
    
    # Test scan
    response = requests.get(qr_url)
    
    # Verify
    assert response.status_code == 200
    print(f"QR scan tested: {qr_url}")
    print(f"Response: {response.url}")
```

---

## 🔍 Testing Checklist

- [ ] FastAPI running on localhost:8000
- [ ] ngrok tunnel active
- [ ] Public URL accessible
- [ ] QR code generated with public URL
- [ ] Phone can scan QR
- [ ] Analytics captured
- [ ] Redirect works
- [ ] Dashboard accessible

---

# Section 7: QR Analytics Case Study

## The Problem: Localhost QR Fails

```mermaid
graph TD
    subgraph "The Problem"
        D[Developer] -->|Creates QR| Q[QR Code]
        Q -->|Contains| L[localhost:8000]
        L -->|Scanned by| P[Phone]
        P -->|Cannot Access| F[Error]
        F -->|User sees| E["Connection Refused"]
    end
```

## The Solution: Public Tunnel QR

```mermaid
graph TD
    subgraph "The Solution"
        D[Developer] -->|Creates QR| Q[QR Code]
        Q -->|Contains| T[ngrok URL]
        T -->|Scanned by| P[Phone]
        P -->|Accesses| N[ngrok Tunnel]
        N -->|Routes to| A[FastAPI]
        A -->|Records| AN[Analytics]
        A -->|Redirects| R[Destination]
    end
```

## Complete Workflow

### Step 1: Start Services

```bash
# Terminal 1: Start FastAPI
uvicorn main:app --reload --port 8000

# Terminal 2: Start ngrok
ngrok http 8000
# Forwarding: https://abc123.ngrok.io -> localhost:8000
```

### Step 2: Generate QR with Public URL

```python
import qrcode
from PIL import Image

def generate_test_qr():
    # Public URL from ngrok
    public_url = "https://abc123.ngrok.io"
    scan_url = f"{public_url}/scan/QRTEST"
    
    # Generate QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(scan_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_test.png")
    print(f"QR Code generated: {scan_url}")
    return scan_url
```

### Step 3: Test Scan Flow

```mermaid
sequenceDiagram
    participant U as User
    participant Q as QR Code
    participant P as Phone
    participant N as ngrok
    participant F as FastAPI
    participant DB as Database
    
    U->>Q: Scan QR Code
    Q-->>P: Contains URL
    P->>N: Request /scan/QRTEST
    N->>N: Log Request
    N->>F: Forward Request
    F->>F: Validate QR
    F->>DB: Record Scan
    F-->>P: Redirect Response
    P->>U: Show Destination
```

### Step 4: Analytics Recording

```python
from fastapi import FastAPI, Request
from datetime import datetime
import json

app = FastAPI()

# In-memory analytics store (use database in production)
analytics_store = []

@app.get("/scan/{qr_id}")
async def handle_scan(qr_id: str, request: Request):
    """
    Handle QR scan with analytics
    """
    # Extract request data
    scan_data = {
        "qr_id": qr_id,
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.client.host,
        "user_agent": request.headers.get("user-agent"),
        "referer": request.headers.get("referer")
    }
    
    # Store analytics
    analytics_store.append(scan_data)
    print(f"Scan recorded: {scan_data}")
    
    # Get destination for QR
    destination = get_qr_destination(qr_id)
    
    # Return redirect
    return RedirectResponse(destination)

@app.get("/analytics")
async def get_analytics():
    """
    Get analytics summary
    """
    return {
        "total_scans": len(analytics_store),
        "recent_scans": analytics_store[-10:],  # Last 10 scans
        "unique_qrs": len(set(s["qr_id"] for s in analytics_store))
    }
```

### Step 5: Monitor in Real-time

```bash
# View ngrok request log
open http://localhost:4040

# View analytics endpoint
curl https://abc123.ngrok.io/analytics

# View FastAPI logs
# Terminal 1 shows each scan
```

## Before vs After Comparison

### Before (Localhost)

```mermaid
graph TD
    subgraph "Localhost QR Flow"
        Q[QR Code] -->|localhost:8000| P[Phone Scan]
        P -->|Connection Refused| E[Error]
        E -->|User fails| U[Frustration]
    end
```

### After (ngrok)

```mermaid
graph TD
    subgraph "ngrok QR Flow"
        Q[QR Code] -->|ngrok.io URL| P[Phone Scan]
        P -->|Works| A[Analytics Recorded]
        A -->|Success| S[Happy User]
    end
```

## Test Results Validation

```python
def validate_test_results():
    """
    Validate the test workflow
    """
    public_url = "https://abc123.ngrok.io"
    
    # 1. Check API health
    response = requests.get(f"{public_url}/health")
    print(f"Health: {response.status_code}")
    
    # 2. Test QR scan
    response = requests.get(f"{public_url}/scan/TEST123")
    print(f"Scan redirect: {response.status_code}")
    
    # 3. Check analytics
    response = requests.get(f"{public_url}/analytics")
    data = response.json()
    print(f"Total scans: {data['total_scans']}")
    
    # 4. Verify QR code is accessible
    qr_code_url = f"{public_url}/qr/TEST123"
    response = requests.get(qr_code_url)
    print(f"QR image: {response.status_code}")
```

---

## 📊 Test Success Metrics

| Metric | Target | Result |
|--------|--------|--------|
| **API Health** | 200 OK | ✓ |
| **QR Scan** | Redirect | ✓ |
| **Analytics** | Recorded | ✓ |
| **Mobile Access** | Works | ✓ |
| **Dashboard** | Accessible | ✓ |

---

# Section 8: Cloudflare Tunnel

## What is Cloudflare Tunnel?

**Cloudflare Tunnel** is a secure way to expose local servers to the internet without opening ports, using Cloudflare's global network.

```mermaid
graph LR
    subgraph "Cloudflare Tunnel"
        L[Local Server] -->|Cloudflared| T[Tunnel]
        T -->|Cloudflare Network| C[Cloudflare Edge]
        C -->|Public URL| I[Internet]
    end
```

## How Cloudflare Tunnel Works

```mermaid
sequenceDiagram
    participant L as Local Server
    participant C as Cloudflare
    participant U as User
    
    L->>C: Establish secure tunnel
    C-->>L: Tunnel established
    
    U->>C: Request public URL
    C->>L: Forward request
    L-->>C: Response
    C-->>U: Response
```

## Installation & Setup

### 1. Install Cloudflared

```bash
# macOS with Homebrew
brew install cloudflared

# Linux
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
sudo chmod +x /usr/local/bin/cloudflared

# Windows (with scoop)
scoop install cloudflared
```

### 2. Start a Tunnel

```bash
# Basic tunnel
cloudflared tunnel --url http://localhost:8000

# Output:
# https://random-name.trycloudflare.com
```

### 3. With Cloudflare Account

```bash
# Login to Cloudflare
cloudflared tunnel login

# Create a tunnel
cloudflared tunnel create my-tunnel

# Run tunnel
cloudflared tunnel run my-tunnel
```

## Cloudflare Tunnel vs ngrok

```mermaid
graph TD
    subgraph "Comparison"
        N[ngrok] -->|Pros| N1[Simple setup]
        N -->|Pros| N2[Web interface]
        N -->|Cons| N3[Free tier limited]
        
        C[Cloudflare Tunnel] -->|Pros| C1[Cloudflare network]
        C -->|Pros| C2[Custom domains]
        C -->|Pros| C3[No port forwarding]
        C -->|Cons| C4[More setup]
    end
```

### Detailed Comparison

| Feature | ngrok | Cloudflare Tunnel |
|---------|-------|-------------------|
| **Setup Complexity** | Simple | Moderate |
| **Free Tier** | Limited | Unlimited (basic) |
| **Custom Domains** | Paid | Free (with Cloudflare) |
| **Web Interface** | Yes | Limited |
| **Request Inspection** | Yes | Limited |
| **Global Network** | Good | Excellent |
| **Security** | Good | Excellent |

## Use Cases Comparison

### When to Use ngrok

```mermaid
graph TD
    subgraph "ngrok Use Cases"
        N1[Quick testing] --> U1[Fast setup]
        N2[API debugging] --> U2[Great tools]
        N3[Team sharing] --> U3[Easy sharing]
        N4[Prototyping] --> U4[Simple]
    end
```

### When to Use Cloudflare Tunnel

```mermaid
graph TD
    subgraph "Cloudflare Tunnel Use Cases"
        C1[Production-like] --> U1[More reliable]
        C2[Custom domains] --> U2[Professional]
        C3[High traffic] --> U3[Scalable]
        C4[Security] --> U4[Better protection]
    end
```

## SQAnalytics with Cloudflare

### FastAPI + Cloudflare Tunnel

```bash
# Start FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000

# Start Cloudflare Tunnel
cloudflared tunnel --url http://localhost:8000

# Output:
# https://random-name.trycloudflare.com
```

### Configuration File

```yaml
# ~/.cloudflared/config.yml
tunnel: my-tunnel
credentials-file: /path/to/credentials.json

ingress:
  - hostname: qr.sqanalytics.com
    service: http://localhost:8000
  - hostname: api.sqanalytics.com
    service: http://localhost:8001
  - service: http_status:404
```

---

## 🎯 Cloudflare Tunnel Benefits

1. **Global CDN** - Fast worldwide access
2. **DDoS Protection** - Built-in security
3. **Custom Domains** - Professional URLs
4. **No Port Forwarding** - More secure
5. **Free SSL** - Automatic HTTPS

---

# Section 9: Tunnel Security Considerations

## Security Risks

```mermaid
graph TD
    subgraph "Security Risks"
        R1[Exposed to Internet] --> I1[Anyone can access]
        R2[No Authentication] --> I2[Unauthorized access]
        R3[Data Exposure] --> I3[Sensitive data]
        R4[Brute Force] --> I4[Attacks]
    end
```

## Security Best Practices

### 1. Add Basic Authentication

```bash
# ngrok with basic auth
ngrok http 8000 --basic-auth="username:password"

# Access: https://username:password@abc123.ngrok.io
```

### 2. Use HTTPS Only

```bash
# Force HTTPS
ngrok http 8000 --scheme=https
```

### 3. Limit Tunnel Lifetime

```bash
# Tunnel expires after 1 hour
ngrok http 8000 --start-at=1h
```

### 4. Implement API Authentication

```python
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/secure")
async def secure_endpoint(credentials: HTTPBasicCredentials = Security(security)):
    if credentials.username != "admin" or credentials.password != "secret":
        raise HTTPException(status_code=401)
    return {"message": "Secure access"}
```

## Development vs Production Security

```mermaid
graph TD
    subgraph "Development"
        D1[ngrok with auth] --> A1[Good enough]
        D2[Short tunnels] --> A2[Limited exposure]
        D3[Test data only] --> A3[Low risk]
    end
    
    subgraph "Production"
        P1[Cloudflare Tunnel] --> S1[Better security]
        P2[Custom domain] --> S2[Professional]
        P3[WAF enabled] --> S3[Protected]
        P4[Rate limiting] --> S4[DDoS protected]
    end
```

## Secure Testing Guidelines

### Do's and Don'ts

| Do | Don't |
|----|-------|
| Use authentication | Expose without auth |
| Use HTTPS | Use HTTP |
| Test with dummy data | Use production data |
| Limit tunnel time | Leave tunnels running |
| Monitor access | Ignore logs |

### Security Checklist

```mermaid
graph TD
    subgraph "Security Checklist"
        C1[Add authentication] --> V1[✓ Basic auth or OAuth]
        C2[Use HTTPS] --> V2[✓ Encrypted traffic]
        C3[Limit access] --> V3[✓ IP whitelisting]
        C4[Monitor logs] --> V4[✓ Check suspicious activity]
        C5[Use test data] --> V5[✓ No sensitive data]
        C6[Set expiry] --> V6[✓ Auto-expire]
    end
```

## Implementing Rate Limiting

```python
from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

app = FastAPI()

# Rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

@app.get("/scan/{qr_id}")
@limiter.limit("10/minute")
async def scan_qr(request: Request, qr_id: str):
    # Rate limited to 10 requests per minute
    pass
```

---

## 🔍 Security Check

1. Add authentication to your tunnel
2. Use HTTPS
3. Limit tunnel lifetime
4. Implement API auth
5. Use test data only
6. Monitor access logs

---

# Section 10: Common Developer Mistakes

## Mistake 1: Using localhost in Production

### ❌ The Problem

```python
# QR code with localhost URL
qr.add_data("http://localhost:8000/scan/123")
```

### Symptoms
- QR fails when scanned
- Only works on developer's machine
- Confusion in production

### Impact
- Broken user experience
- Lost analytics data
- Bad impression

### ✅ The Solution

```python
# Dynamic URL based on environment
import os

def get_base_url():
    if os.getenv("ENVIRONMENT") == "production":
        return "https://sqanalytics.com"
    else:
        return os.getenv("PUBLIC_URL", "http://localhost:8000")

qr_url = f"{get_base_url()}/scan/123"
```

## Mistake 2: Hardcoding ngrok URLs

### ❌ The Problem

```python
# Hardcoded ngrok URL
NGROK_URL = "https://abc123.ngrok.io"

@app.get("/qr")
async def generate_qr():
    url = f"{NGROK_URL}/scan/123"
    # URL changes every ngrok session!
```

### Symptoms
- URLs break after ngrok restart
- Hard to maintain
- Works only temporarily

### ✅ The Solution

```python
import os

def get_public_url():
    # Get from environment variable
    return os.getenv("PUBLIC_URL", "https://abc123.ngrok.io")

@app.get("/qr")
async def generate_qr():
    base_url = get_public_url()
    return {"qr_url": f"{base_url}/scan/123"}
```

## Mistake 3: Ignoring Security

### ❌ The Problem

```bash
# No authentication
ngrok http 8000

# Everyone can access
```

### Symptoms
- Unauthorized access
- Data exposure
- API abuse

### ✅ The Solution

```bash
# With authentication
ngrok http 8000 --basic-auth="admin:secure_password"

# Or via config
ngrok start myapp --config=ngrok.yml
```

## Mistake 4: Testing Only on Desktop

### ❌ The Problem

```python
# Only test from browser on same machine
response = requests.get("http://localhost:8000/health")
```

### Symptoms
- Mobile issues not caught
- QR scanning fails
- Poor mobile experience

### ✅ The Solution

```python
# Test from multiple devices
public_url = "https://abc123.ngrok.io"

def test_all_devices():
    devices = [
        ("Desktop", "Mozilla/5.0 (Windows NT 10.0; ...)"),
        ("Mobile", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 ...)"),
        ("Tablet", "Mozilla/5.0 (iPad; CPU OS 14_0 ...)")
    ]
    
    for device, user_agent in devices:
        response = requests.get(
            f"{public_url}/health",
            headers={"User-Agent": user_agent}
        )
        print(f"{device}: {response.status_code}")
```

## Mistake 5: Not Testing Redirects

### ❌ The Problem

```python
@app.get("/scan/{qr_id}")
async def scan_qr(qr_id: str):
    # No redirect logic
    return {"status": "scanned"}
```

### Symptoms
- QR doesn't take user to destination
- Broken user flow
- No conversion tracking

### ✅ The Solution

```python
@app.get("/scan/{qr_id}")
async def scan_qr(qr_id: str):
    # Record analytics
    record_scan(qr_id)
    
    # Get destination
    destination = get_destination(qr_id)
    
    # Redirect user
    return RedirectResponse(destination)
```

## Troubleshooting Flowchart

```mermaid
graph TD
    A[Issue] --> B{Problem Type?}
    
    B -->|"URL Not Accessible"| C{Check:}
    C --> C1[Tunnel running?]
    C --> C2[Public URL correct?]
    C --> C3[Port correct?]
    C --> C4[Firewall blocking?]
    
    B -->|"QR Scan Fails"| D{Check:}
    D --> D1[QR has public URL?]
    D --> D2[Endpoint works?]
    D --> D3[Redirect happens?]
    
    B -->|"Security Issue"| E{Check:}
    E --> E1[Authentication set?]
    E --> E2[HTTPS enabled?]
    E --> E3[Rate limiting?]
    
    B -->|"Mobile Not Working"| F{Check:}
    F --> F1[URL accessible?]
    F --> F2[Mobile friendly?]
    F --> F3[Response correct?]
```

---

## 🔍 Common Mistake Checklist

- [ ] Using localhost in production
- [ ] Hardcoding ngrok URLs
- [ ] Ignoring security
- [ ] Testing only on desktop
- [ ] Not testing redirects
- [ ] No environment detection
- [ ] No error handling
- [ ] No monitoring

---

# Section 11: Transition From Tunnel To Production

## The Development Journey

```mermaid
graph LR
    A[Local Development] --> B[Public Tunnel]
    B --> C[Cloud Hosting]
    C --> D[Production Deployment]
```

## Environment Progression

### 1. Local Development

```mermaid
graph LR
    subgraph "Local Development"
        L[localhost:8000] -->|Only you| D[Developer]
    end
```

**Characteristics:**
- Fast development
- Local dependencies
- No internet required
- Only accessible locally

### 2. Public Tunnel Testing

```mermaid
graph LR
    subgraph "Tunnel Testing"
        T[ngrok URL] -->|Anyone with URL| D1[Team]
        T -->|Anyone with URL| D2[Client]
        T -->|Anyone with URL| D3[QA]
    end
```

**Characteristics:**
- External access
- Real device testing
- Client demos
- Temporary access

### 3. Cloud Hosting

```mermaid
graph LR
    subgraph "Cloud Hosting"
        H[Hosting Platform] -->|Public| W[Everyone]
    end
```

**Characteristics:**
- Always available
- Scalable
- Professional
- Production-ready

### 4. Production Deployment

```mermaid
graph LR
    subgraph "Production"
        P[Production URL] -->|Everyone| A[All Users]
        P -->|Backed by| S[Servers]
        P -->|Connected to| DB[Database]
    end
```

## Migration Path

### From Tunnel to Production

```mermaid
graph TD
    subgraph "Migration Steps"
        S1[Use tunnel for testing] --> S2[Validate in tunnel]
        S2 --> S3[Configure cloud hosting]
        S3 --> S4[Deploy to cloud]
        S4 --> S5[Update DNS]
        S5 --> S6[Production ready]
    end
```

### Code Configuration

```python
# Environment-based configuration
import os

class Config:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    
    # Development
    if ENVIRONMENT == "development":
        DATABASE_URL = "sqlite:///./dev.db"
        BASE_URL = "http://localhost:8000"
        DEBUG = True
    
    # Testing (ngrok)
    elif ENVIRONMENT == "testing":
        DATABASE_URL = "postgresql://localhost/test"
        BASE_URL = os.getenv("PUBLIC_URL", "https://abc123.ngrok.io")
        DEBUG = True
    
    # Production
    else:
        DATABASE_URL = os.getenv("DATABASE_URL")
        BASE_URL = os.getenv("BASE_URL", "https://sqanalytics.com")
        DEBUG = False
```

## Tunnel vs Production Checklist

| Aspect | Tunnel | Production |
|--------|--------|------------|
| **URL** | ngrok.io | Custom domain |
| **Authentication** | Optional | Required |
| **Database** | Local | Cloud |
| **Scalability** | None | Auto-scaling |
| **Monitoring** | Minimal | Full |
| **Security** | Basic | Enterprise |

## Deployment Decision Tree

```mermaid
graph TD
    Q[Ready for production?] -->|No| T[Continue tunnel testing]
    Q -->|Yes| P{Deployment Type?}
    
    P -->|Cloud| C[AWS/GCP/Azure]
    P -->|Platform| H[Heroku/Fly.io]
    P -->|Container| K[Kubernetes]
    
    C --> D[Deploy]
    H --> D
    K --> D
    
    D --> U[Update DNS]
    U --> L[Launch]
```

---

## 🚀 Production Deployment Checklist

- [ ] Custom domain configured
- [ ] SSL certificate installed
- [ ] Database in production
- [ ] Environment variables set
- [ ] Monitoring enabled
- [ ] Logging configured
- [ ] Backups scheduled
- [ ] Security implemented
- [ ] Rate limiting in place
- [ ] Analytics tracking

---

# Section 12: SQAnalytics Case Study

## Complete Workflow

### System Architecture

```mermaid
graph TD
    subgraph "SQAnalytics System"
        P[Phone] -->|Scan QR| Q[QR Code]
        Q -->|Public URL| T[ngrok Tunnel]
        T -->|Route| F[FastAPI]
        
        F -->|Process| A[Analytics Service]
        A -->|Store| DB[(PostgreSQL)]
        
        F -->|Redirect| D[Destination URL]
        D -->|Show| B[Browser]
    end
```

## Components Breakdown

### 1. QR Code Creation

```python
import qrcode
import os

class QRCodeService:
    def __init__(self):
        self.base_url = self.get_base_url()
    
    def get_base_url(self):
        """Get the appropriate base URL"""
        env = os.getenv("ENVIRONMENT", "development")
        
        if env == "development":
            return "http://localhost:8000"
        elif env == "testing":
            return os.getenv("PUBLIC_URL")
        else:
            return os.getenv("BASE_URL", "https://sqanalytics.com")
    
    def generate_qr(self, qr_id: str):
        """Generate QR code with tracking URL"""
        tracking_url = f"{self.base_url}/scan/{qr_id}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(tracking_url)
        qr.make(fit=True)
        
        return qr.make_image()
```

### 2. FastAPI Application

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from datetime import datetime
import json

app = FastAPI()

# Analytics storage (use database in production)
scan_analytics = []

@app.get("/scan/{qr_id}")
async def handle_scan(qr_id: str, request: Request):
    """
    Handle QR scan with full analytics tracking
    """
    try:
        # 1. Extract request data
        scan_data = {
            "qr_id": qr_id,
            "timestamp": datetime.utcnow().isoformat(),
            "ip": request.client.host,
            "user_agent": request.headers.get("user-agent"),
            "referer": request.headers.get("referer")
        }
        
        # 2. Enrich with user-agent data
        if scan_data["user_agent"]:
            from user_agents import parse
            ua = parse(scan_data["user_agent"])
            scan_data["browser"] = ua.browser.family
            scan_data["os"] = ua.os.family
            scan_data["device_type"] = 'Mobile' if ua.is_mobile else 'Tablet' if ua.is_tablet else 'Desktop'
        
        # 3. Store analytics
        scan_analytics.append(scan_data)
        print(f"Scan recorded: {json.dumps(scan_data, indent=2)}")
        
        # 4. Get destination
        destination = get_destination(qr_id)
        
        # 5. Return redirect
        return RedirectResponse(destination)
    
    except Exception as e:
        print(f"Error processing scan: {e}")
        raise HTTPException(status_code=500, detail="Scan processing failed")

@app.get("/analytics")
async def get_analytics():
    """
    Get analytics summary
    """
    if not scan_analytics:
        return {
            "total_scans": 0,
            "message": "No scans recorded yet"
        }
    
    # Calculate analytics
    total_scans = len(scan_analytics)
    unique_qrs = len(set(s["qr_id"] for s in scan_analytics))
    
    # Device breakdown
    devices = {}
    for scan in scan_analytics:
        device = scan.get("device_type", "Unknown")
        devices[device] = devices.get(device, 0) + 1
    
    # Browser breakdown
    browsers = {}
    for scan in scan_analytics:
        browser = scan.get("browser", "Unknown")
        browsers[browser] = browsers.get(browser, 0) + 1
    
    return {
        "total_scans": total_scans,
        "unique_qrs": unique_qrs,
        "device_breakdown": devices,
        "browser_breakdown": browsers,
        "recent_scans": scan_analytics[-5:]  # Last 5 scans
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }
```

### 3. Environment Setup

```bash
# Environment variables
export ENVIRONMENT=testing
export PUBLIC_URL=https://abc123.ngrok.io
export DATABASE_URL=postgresql://localhost/sqanalytics
```

### 4. Running the Application

```bash
# Terminal 1: Start FastAPI
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Start ngrok
ngrok http 8000
# Forwarding: https://abc123.ngrok.io -> http://localhost:8000

# Terminal 3: Test
curl https://abc123.ngrok.io/health
curl https://abc123.ngrok.io/scan/TEST123
curl https://abc123.ngrok.io/analytics
```

### 5. Testing QR Flow

```python
# Generate test QR with public URL
from qrcode_service import QRCodeService

service = QRCodeService()
qr_image = service.generate_qr("TEST123")
qr_image.save("test_qr.png")

print(f"QR Code generated for: {service.base_url}/scan/TEST123")
print("Test on your phone!")
```

### 6. Analytics Dashboard

```html
<!DOCTYPE html>
<html>
<head>
    <title>SQAnalytics Dashboard</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f5f5f5; }
        .dashboard { max-width: 1200px; margin: 0 auto; }
        .card { background: white; padding: 20px; margin: 10px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
        .stat { text-align: center; }
        .stat-number { font-size: 2em; font-weight: bold; color: #333; }
        .stat-label { color: #666; }
        .recent { max-height: 300px; overflow-y: auto; }
        .scan-item { padding: 10px; border-bottom: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>SQAnalytics Dashboard</h1>
        <div class="stats" id="stats">
            <div class="stat">
                <div class="stat-number" id="totalScans">0</div>
                <div class="stat-label">Total Scans</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="uniqueQrs">0</div>
                <div class="stat-label">Unique QR Codes</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="mobilePercent">0%</div>
                <div class="stat-label">Mobile Users</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="topBrowser">-</div>
                <div class="stat-label">Top Browser</div>
            </div>
        </div>
        
        <div class="card">
            <h2>Recent Scans</h2>
            <div class="recent" id="recentScans"></div>
        </div>
    </div>
    
    <script>
        function updateDashboard() {
            fetch('/analytics')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('totalScans').textContent = data.total_scans || 0;
                    document.getElementById('uniqueQrs').textContent = data.unique_qrs || 0;
                    
                    // Mobile percentage
                    const mobile = data.device_breakdown?.Mobile || 0;
                    const total = data.total_scans || 1;
                    document.getElementById('mobilePercent').textContent = 
                        Math.round((mobile / total) * 100) + '%';
                    
                    // Top browser
                    const browsers = data.browser_breakdown || {};
                    const top = Object.entries(browsers).sort((a,b) => b[1] - a[1])[0];
                    document.getElementById('topBrowser').textContent = top ? top[0] : '-';
                    
                    // Recent scans
                    const recent = document.getElementById('recentScans');
                    recent.innerHTML = (data.recent_scans || []).map(scan => `
                        <div class="scan-item">
                            <strong>${scan.qr_id}</strong>
                            <span>${new Date(scan.timestamp).toLocaleString()}</span>
                            <span>${scan.device_type || 'Unknown'}</span>
                            <span>${scan.browser || 'Unknown'}</span>
                        </div>
                    `).join('');
                });
        }
        
        updateDashboard();
        setInterval(updateDashboard, 5000); // Update every 5 seconds
    </script>
</body>
</html>
```

---

## 📊 Full Workflow Validation

```mermaid
sequenceDiagram
    participant D as Developer
    participant Q as QR Code
    participant P as Phone
    participant N as ngrok
    participant F as FastAPI
    participant DB as Database
    
    D->>Q: Generate QR with public URL
    Q-->>P: Contains URL
    
    P->>N: Request /scan/QR123
    N->>N: Log request
    N->>F: Forward request
    
    F->>F: Extract data
    F->>F: Parse user-agent
    F->>DB: Store analytics
    
    F->>P: Redirect to destination
    
    D->>F: View dashboard
    F-->>D: Show analytics
```

---

# Section 13: Hands-On Exercises

## Exercise 1: Install and Configure ngrok

### Objective
Install ngrok and expose a local web server.

### Instructions

```bash
# 1. Install ngrok
# macOS: brew install ngrok
# Linux: Download from ngrok.com
# Windows: Download from ngrok.com

# 2. Authenticate
ngrok config add-authtoken YOUR_TOKEN

# 3. Test with simple web server
python -m http.server 8000

# 4. Expose with ngrok
ngrok http 8000

# 5. Verify access
# Open the public URL in your browser
```

### Expected Output

```bash
Session Status                online
Account                       Your Account
Version                       3.0.0
Forwarding                    https://abc123.ngrok.io -> http://localhost:8000
```

### Learning Outcomes
- ngrok installation
- Authentication setup
- Basic tunnel creation
- Public URL generation

---

## Exercise 2: Expose FastAPI Through ngrok

### Objective
Expose a FastAPI application to the internet.

### Instructions

```python
# 1. Create FastAPI app
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from ngrok!"}

@app.get("/test")
async def test():
    return {"status": "working"}

# 2. Start FastAPI
# uvicorn main:app --reload --port 8000

# 3. Expose with ngrok
# ngrok http 8000

# 4. Test
# curl https://abc123.ngrok.io
# curl https://abc123.ngrok.io/test
```

### Expected Output

```python
# curl https://abc123.ngrok.io
{"message": "Hello from ngrok!"}

# curl https://abc123.ngrok.io/test
{"status": "working"}
```

### Learning Outcomes
- FastAPI setup
- Port exposure
- API testing
- ngrok integration

---

## Exercise 3: QR Code Testing Through Tunnel

### Objective
Test QR code scanning through a public tunnel.

### Instructions

```python
# 1. Setup FastAPI with QR handler
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import qrcode

app = FastAPI()

@app.get("/scan/{qr_id}")
async def scan_qr(qr_id: str, request: Request):
    # Log scan
    print(f"QR {qr_id} scanned from {request.client.host}")
    
    # Record analytics
    # ... your analytics code ...
    
    # Redirect to destination
    return RedirectResponse("https://example.com")

# 2. Start services
# uvicorn main:app --reload --port 8000
# ngrok http 8000

# 3. Generate QR with public URL
public_url = "https://abc123.ngrok.io"
qr_url = f"{public_url}/scan/TEST123"

qr = qrcode.QRCode(version=1)
qr.add_data(qr_url)
qr.make(fit=True)
img = qr.make_image()
img.save("test_qr.png")

print(f"QR generated: {qr_url}")
print("Scan with your phone!")

# 4. Check analytics
# Your endpoint should show scan data
```

### Expected Output

```bash
# When scanning QR
QR TEST123 scanned from 192.168.1.100
# Phone redirects to example.com
```

### Learning Outcomes
- QR generation with public URLs
- QR scanning workflow
- Analytics tracking
- Full system testing

---

## Mini Project 1: Public API Demo

### Objective
Create a public API demo accessible via ngrok.

### Requirements

```python
# 1. Build a simple API
# 2. Add endpoints for:
#    - GET /api/products
#    - GET /api/product/{id}
#    - POST /api/orders
# 3. Add authentication
# 4. Expose via ngrok
# 5. Share with team/client
```

### Expected Structure

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from datetime import datetime
import os

app = FastAPI()

# Authentication
security = HTTPBasic()

def verify_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "demo" or credentials.password != "demo123":
        raise HTTPException(status_code=401)
    return True

# Sample data
products = [
    {"id": 1, "name": "Product A", "price": 29.99},
    {"id": 2, "name": "Product B", "price": 49.99},
    {"id": 3, "name": "Product C", "price": 19.99}
]

@app.get("/")
async def root():
    return {
        "service": "Public API Demo",
        "version": "1.0.0",
        "endpoints": [
            "/api/products",
            "/api/product/{id}",
            "/api/orders"
        ]
    }

@app.get("/api/products")
async def get_products():
    return products

@app.get("/api/product/{id}")
async def get_product(id: int):
    product = next((p for p in products if p["id"] == id), None)
    if not product:
        raise HTTPException(status_code=404)
    return product

@app.post("/api/orders")
async def create_order(
    order: dict,
    auth: bool = Depends(verify_auth)
):
    return {
        "order_id": 123,
        "status": "created",
        "timestamp": datetime.utcnow().isoformat()
    }
```

### Usage

```bash
# Start the API
uvicorn main:app --reload --port 8000

# Expose with ngrok
ngrok http 8000

# Share URL with team
echo "https://abc123.ngrok.io/docs"  # FastAPI docs
```

---

## Mini Project 2: QR Redirect Service

### Objective
Build a QR redirect service with analytics.

### Requirements

```python
# 1. QR code creation endpoint
# 2. Redirect with analytics
# 3. Dashboard
# 4. Expose via public tunnel
```

### Expected Structure

```python
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from datetime import datetime
import qrcode
import json
import os

app = FastAPI()

# Analytics store (use database in production)
analytics = []

@app.post("/qr/create")
async def create_qr(data: dict):
    qr_id = data.get("qr_id", str(datetime.utcnow().timestamp()))
    destination = data.get("destination", "https://example.com")
    
    # Store mapping
    # In production, use database
    mapping[qr_id] = destination
    
    # Generate QR with public URL
    base_url = os.getenv("PUBLIC_URL", "http://localhost:8000")
    qr_url = f"{base_url}/scan/{qr_id}"
    
    qr = qrcode.QRCode(version=1)
    qr.add_data(qr_url)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f"qr_{qr_id}.png")
    
    return {
        "qr_id": qr_id,
        "qr_url": qr_url,
        "destination": destination,
        "qr_image": f"qr_{qr_id}.png"
    }

@app.get("/scan/{qr_id}")
async def handle_scan(qr_id: str, request: Request):
    # Record analytics
    analytics.append({
        "qr_id": qr_id,
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.client.host,
        "user_agent": request.headers.get("user-agent")
    })
    
    # Get destination
    destination = mapping.get(qr_id, "https://example.com")
    
    return RedirectResponse(destination)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>QR Dashboard</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            .scans { max-height: 400px; overflow-y: auto; }
        </style>
    </head>
    <body>
        <h1>QR Analytics Dashboard</h1>
        <div>
            <h2>Recent Scans</h2>
            <div class="scans" id="scans"></div>
        </div>
        <script>
            fetch('/analytics')
                .then(r => r.json())
                .then(data => {
                    const scans = document.getElementById('scans');
                    scans.innerHTML = data.map(scan => `
                        <div>${scan.qr_id} - ${new Date(scan.timestamp).toLocaleString()}</div>
                    `).join('');
                });
        </script>
    </body>
    </html>
    """
    return html

@app.get("/analytics")
async def get_analytics():
    return analytics
```

### Testing

```bash
# Start service
uvicorn main:app --reload --port 8000

# Expose via ngrok
ngrok http 8000

# Create QR
curl -X POST https://abc123.ngrok.io/qr/create \
  -H "Content-Type: application/json" \
  -d '{"qr_id": "BOOK123", "destination": "https://example.com/book"}'

# Test scan
# Open QR in phone
# View dashboard
```

---

## Exercise Solutions

### Common Solution Patterns

```python
# Pattern 1: Environment detection
def get_base_url():
    """Detect environment and return appropriate URL"""
    env = os.getenv("ENVIRONMENT", "development")
    
    if env == "production":
        return os.getenv("BASE_URL", "https://sqanalytics.com")
    elif env == "testing":
        return os.getenv("PUBLIC_URL", "http://localhost:8000")
    else:
        return "http://localhost:8000"

# Pattern 2: QR generation with environment
def generate_qr_with_environment(qr_id: str):
    """Generate QR with environment-aware URL"""
    base_url = get_base_url()
    qr_url = f"{base_url}/scan/{qr_id}"
    
    qr = qrcode.QRCode(version=1)
    qr.add_data(qr_url)
    qr.make(fit=True)
    return qr.make_image()

# Pattern 3: ngrok URL detection
def is_ngrok_url(url: str) -> bool:
    """Check if URL is an ngrok tunnel"""
    return 'ngrok.io' in url or 'trycloudflare.com' in url
```

### Learning Outcomes Checklist

- [ ] Can install and configure ngrok
- [ ] Can expose FastAPI applications
- [ ] Can test from mobile devices
- [ ] Can generate QR codes with public URLs
- [ ] Can capture analytics
- [ ] Can build dashboards
- [ ] Understand security considerations
- [ ] Can transition to production

---

# Tunneling Roadmap

## Learning Progression

```mermaid
graph TD
    A[Localhost Basics] --> B[LAN Access]
    B --> C[ngrok Setup]
    C --> D[API Exposure]
    D --> E[Mobile Testing]
    E --> F[QR Integration]
    F --> G[Cloudflare Tunnel]
    G --> H[Production Deployment]
```

## Skill Progression

| Level | Skills | Tools |
|-------|--------|-------|
| **Beginner** | Localhost, basic networking | Local computer |
| **Intermediate** | ngrok, LAN access | ngrok, FastAPI |
| **Advanced** | Mobile testing, QR integration | ngrok, QR libraries |
| **Expert** | Cloudflare, production deployment | Cloudflare, hosting |

---

# Tunneling Cheat Sheet

## Quick Reference

### Common Commands

```bash
# ngrok installation
brew install ngrok  # macOS
# Download from ngrok.com for other OS

# Authentication
ngrok config add-authtoken YOUR_TOKEN

# Expose HTTP server
ngrok http 8000

# Expose with basic auth
ngrok http 8000 --basic-auth="user:pass"

# Use custom sub-domain
ngrok http 8000 --sub-domain=myapp

# Expose multiple ports
ngrok http 8000 --host-header=localhost:8000

# Check status
ngrok status

# View logs
ngrok logs

# Stop tunnels
ngrok stop
```

### Cloudflare Commands

```bash
# Install cloudflared
brew install cloudflared  # macOS
# Download from cloudflare.com for other OS

# Start tunnel
cloudflared tunnel --url http://localhost:8000

# Login
cloudflared tunnel login

# Create tunnel
cloudflared tunnel create my-tunnel

# Run tunnel
cloudflared tunnel run my-tunnel
```

### FastAPI Configuration

```python
# Development
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# LAN Access
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Environment Variables

```bash
# Development
export ENVIRONMENT=development
export BASE_URL=http://localhost:8000

# Testing
export ENVIRONMENT=testing
export PUBLIC_URL=https://abc123.ngrok.io

# Production
export ENVIRONMENT=production
export BASE_URL=https://sqanalytics.com
```

## Network Address Reference

| Address | Purpose | Access |
|---------|---------|--------|
| `127.0.0.1` | Localhost | Only your computer |
| `0.0.0.0` | All interfaces | LAN + local |
| `192.168.x.x` | Private IP | Same network |
| `https://abc123.ngrok.io` | Public tunnel | Anyone |
| `https://domain.com` | Production | Everyone |

---

# Troubleshooting Guide

## Issue 1: Tunnel Offline

### Symptoms
- URL returns "Connection refused"
- ngrok shows "Offline"
- Tunnel not accessible

### Root Causes
- ngrok not running
- Port not correct
- Firewall blocking
- Network issues

### Solutions

```bash
# Check ngrok status
ngrok status

# Restart ngrok
ngrok stop
ngrok http 8000

# Check FastAPI is running
curl http://localhost:8000

# Check port
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows
```

## Issue 2: URL Not Reachable

### Symptoms
- Cannot access public URL
- Timeout errors
- "This site can't be reached"

### Root Causes
- Wrong URL
- Tunnel expired
- Network issues
- DNS issues

### Solutions

```bash
# Check URL from ngrok output
# Forwarding: https://abc123.ngrok.io

# Test with curl
curl -v https://abc123.ngrok.io

# Check if URL works locally
curl http://localhost:8000

# Try different browser
# Sometimes browser cache issues
```

## Issue 3: Mobile Connection Failures

### Symptoms
- Phone can't connect
- WiFi vs Cellular issues
- Timeout on mobile

### Root Causes
- Phone on different network
- Firewall blocking
- DNS resolution issues

### Solutions

```bash
# Ensure ngrok is running
# Try on phone using cellular data (not WiFi)
# Check if QR code has correct URL

# Test URL from phone browser
# Simply type public URL in phone browser

# If using LAN, ensure phone on same network
# For LAN: use 192.168.x.x address
```

## Issue 4: Authentication Errors

### Symptoms
- 401 Unauthorized
- Login prompt
- Access denied

### Root Causes
- Wrong credentials
- Auth not configured
- Browser caching

### Solutions

```bash
# For basic auth
ngrok http 8000 --basic-auth="user:pass"

# Access with credentials
# https://user:pass@abc123.ngrok.io

# Clear browser cache
# or use incognito mode

# Check auth middleware
# In FastAPI app
```

## Issue 5: QR Code Issues

### Symptoms
- QR not scanning
- Wrong URL
- Connection refused

### Root Causes
- QR has localhost URL
- QR has wrong URL
- QR too small

### Solutions

```python
# Ensure QR has public URL
public_url = "https://abc123.ngrok.io"
qr.add_data(public_url + "/scan/123")

# Generate with proper QR settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Test QR scanning on multiple devices
```

## Troubleshooting Flowchart

```mermaid
graph TD
    A[Issue] --> B{Problem Type?}
    
    B -->|"Can't access URL"| C{Check:}
    C --> C1[ngrok running?]
    C --> C2[Port correct?]
    C --> C3[URL correct?]
    C --> C4[Firewall?]
    
    B -->|"Mobile not working"| D{Check:}
    D --> D1[URL accessible?]
    D --> D2[Phone connected?]
    D --> D3[QR correct?]
    
    B -->|"Auth issues"| E{Check:}
    E --> E1[Credentials correct?]
    E --> E2[Auth configured?]
    E --> E3[Cache cleared?]
```

---

# Interview Preparation Guide

## Beginner Questions

### Q1: What is localhost?
**Answer:** Localhost (127.0.0.1) is the loopback address that only your computer can access. It's used for local development and testing.

### Q2: Why can't other devices access localhost?
**Answer:** Localhost is a loopback address that routes back to the same machine. Other devices on the network use different IP addresses and cannot access your localhost.

### Q3: What is a public tunnel?
**Answer:** A public tunnel creates a secure connection between your local server and the internet, making your local development server accessible from anywhere.

### Q4: What is ngrok used for?
**Answer:** ngrok creates secure public URLs to local web servers, enabling testing of APIs, webhooks, and mobile applications without deploying to production.

### Q5: How do you expose a FastAPI app with ngrok?
**Answer:** 
1. Run FastAPI: `uvicorn main:app --reload --port 8000`
2. Run ngrok: `ngrok http 8000`
3. Access the public URL

### Q6: What's the difference between localhost and 0.0.0.0?
**Answer:** `127.0.0.1` (localhost) only allows connections from the same machine. `0.0.0.0` binds to all available network interfaces, allowing connections from other devices on the network.

### Q7: What are common uses for ngrok?
**Answer:** 
- Testing webhooks
- Mobile app testing
- Client demos
- QR code testing
- API testing

### Q8: How does ngrok work?
**Answer:** ngrok creates a secure tunnel from your local machine to ngrok's cloud service, which provides a public URL that forwards requests to your local server.

### Q9: What's a LAN address?
**Answer:** A LAN (Local Area Network) address is a private IP address assigned to devices on the same network, allowing communication between devices on that network.

### Q10: What is the difference between ngrok and Cloudflare Tunnel?
**Answer:** ngrok is simpler with great debugging tools; Cloudflare Tunnel offers better performance, custom domains, and integration with Cloudflare's network but has a steeper learning curve.

## Intermediate Questions

### Q11: How do you add authentication to ngrok?
**Answer:** Use `--basic-auth="username:password"` when starting ngrok: `ngrok http 8000 --basic-auth="admin:secret"`

### Q12: How do you test QR codes with local development?
**Answer:** Use ngrok to expose your local server with a public URL, then generate QR codes containing the ngrok URL instead of localhost.

### Q13: How do you handle environment-specific URLs?
**Answer:** Use environment variables:
```python
base_url = os.getenv("PUBLIC_URL", "http://localhost:8000")
```

### Q14: What are the security risks of public tunnels?
**Answer:** Public tunnels expose your local development to the internet, risking unauthorized access, data exposure, and potential attacks.

### Q15: How do you secure an ngrok tunnel?
**Answer:** 
1. Add basic authentication
2. Use HTTPS
3. Limit tunnel lifetime
4. Monitor access logs

### Q16: How do you transition from tunnel to production?
**Answer:** 
1. Validate with tunnel
2. Configure cloud hosting
3. Deploy to cloud
4. Update DNS
5. Launch production

### Q17: What's the difference between ngrok free and paid plans?
**Answer:** Paid plans offer custom sub-domains, more tunnels, and better performance. Free tier has a random sub-domain and limits.

### Q18: How do you test API webhooks locally?
**Answer:** Use ngrok to expose your local API endpoint with a public URL that webhook services can send requests to.

### Q19: What is the ngrok web interface used for?
**Answer:** The web interface (localhost:4040) allows inspecting requests, replaying requests, and debugging tunnels.

### Q20: How do you handle multiple tunnels?
**Answer:** Use ngrok's config file to define multiple tunnels and start them with `ngrok start --all`.

## Scenario-Based Questions

### Q21: Your QR codes are failing when scanned from phones - why?
**Answer:** The QR likely contains `localhost` instead of a public URL. Use ngrok to get a public URL and regenerate QR codes.

### Q22: How would you handle a team of developers needing to test the same API?
**Answer:** Each developer can run their own ngrok tunnel with their own URL, or use a shared environment with a single public URL.

### Q23: What would you do if ngrok gave you an authentication token error?
**Answer:** Check that the token is correct and added to the config: `ngrok config add-authtoken YOUR_TOKEN`

### Q24: How do you test a mobile app connecting to a local backend?
**Answer:** 
1. Run the backend locally
2. Expose it with ngrok
3. Update the app to use the public URL
4. Test on real device

### Q25: What's your strategy for testing QR platforms locally?
**Answer:** 
1. Run FastAPI locally
2. Expose via ngrok
3. Generate QR with public URL
4. Test on multiple devices
5. Capture analytics
6. Validate redirects

## Answer Key Summary

### Beginner Level
- Understand localhost limitations
- Know basic ngrok commands
- Understand network types
- Know tunnel use cases

### Intermediate Level
- Can secure tunnels
- Handle environment configs
- Transition to production
- Use advanced features

### Scenario Level
- Troubleshoot issues
- Test QR platforms
- Handle team workflows
- Scale solutions

---

**End of Handbook**

---

*"Public tunneling bridges the gap between local development and real-world testing. It's the essential tool that transforms your development environment into a shareable, testable, and production-ready preview of your application."*