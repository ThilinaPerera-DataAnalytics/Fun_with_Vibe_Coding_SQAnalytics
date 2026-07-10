# CRUD Architecture & Database Access Design for Modern Backend Applications

## A Practical Beginner Guide for Building SQAnalytics with FastAPI, PostgreSQL, SQLAlchemy & Supabase

---

# COVER PAGE

---

**CRUD ARCHITECTURE & DATABASE ACCESS DESIGN FOR MODERN BACKEND APPLICATIONS**

*A Practical Beginner Guide for Building SQAnalytics with FastAPI, PostgreSQL, SQLAlchemy & Supabase*

---

**Senior Backend Architecture Handbook | Version 1.0**

---

*"Design maintainable APIs. Build scalable backends. Master the data layer."*

---

---

# TABLE OF CONTENTS

---

**SECTION 1** — What Is CRUD? ............................................... 7

**SECTION 2** — Why CRUD Layers Exist ..................................... 13

**SECTION 3** — CRUD Architecture Fundamentals ....................... 19

**SECTION 4** — Create Operations .......................................... 27

**SECTION 5** — Read Operations ............................................. 35

**SECTION 6** — Update Operations .......................................... 43

**SECTION 7** — Delete Operations ........................................... 51

**SECTION 8** — SQLAlchemy CRUD Patterns ............................. 59

**SECTION 9** — FastAPI + CRUD Integration ............................. 69

**SECTION 10** — Common Developer Mistakes ........................... 77

**SECTION 11** — SQAnalytics Case Study .................................. 87

**SECTION 12** — Hands-On Exercises ....................................... 99

**SECTION 13** — CRUD Roadmap ........................................... 111

**SECTION 14** — CRUD Cheat Sheet ........................................ 117

**SECTION 15** — Troubleshooting Guide .................................. 125

**SECTION 16** — Interview Preparation Guide .......................... 133

---

---

# SECTION 1

## WHAT IS CRUD?

---

### 📖 Learning Objectives

- Understand the four fundamental operations of data persistence
- Recognize CRUD in real-world applications
- Connect CRUD to the SQAnalytics platform

---

## 1.1 The Four Operations

**CRUD** stands for:

| Letter | Operation | Meaning |
|--------|-----------|---------|
| **C** | **Create** | Insert new data into the system |
| **R** | **Read** | Retrieve existing data from the system |
| **U** | **Update** | Modify existing data in the system |
| **D** | **Delete** | Remove data from the system |

> 💡 **Core Insight:** Every application that stores and manages data revolves around these four operations. Whether you're building Instagram, a banking app, or SQAnalytics, you're essentially performing CRUD.

---

## 1.2 The CRUD Flow

```
┌──────────────┐
│    USER      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    API       │  ← The interface (FastAPI endpoints)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    CRUD      │  ← Data operations layer
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  DATABASE    │  ← PostgreSQL
└──────────────┘
```

---

## 1.3 Real-World CRUD Examples

### 📱 Social Media Platform

| Action | CRUD | Example |
|--------|------|---------|
| Post a photo | **Create** | INSERT INTO posts |
| View feed | **Read** | SELECT * FROM posts |
| Edit caption | **Update** | UPDATE posts SET caption |
| Delete post | **Delete** | DELETE FROM posts |

### 🏦 Banking Application

| Action | CRUD | Example |
|--------|------|---------|
| Open account | **Create** | INSERT INTO accounts |
| Check balance | **Read** | SELECT balance FROM accounts |
| Deposit money | **Update** | UPDATE accounts SET balance |
| Close account | **Delete** | DELETE FROM accounts |

---

## 1.4 SQAnalytics CRUD Examples

**SQAnalytics** (Smart QR Analytics Platform) manages QR codes and scan events:

### QR Code Operations

```python
# CREATE - Generate a new QR code
create_qr(link="https://example.com", name="Product Page")

# READ - Retrieve QR code details
get_qr(qr_id=123)

# UPDATE - Change QR code properties
update_qr(qr_id=123, name="Updated Product")

# DELETE - Remove QR code
delete_qr(qr_id=123)
```

### Scan Event Operations

```python
# CREATE - Record a new scan
create_scan_event(qr_id=123, location="New York")

# READ - Get scan analytics
get_scan_stats(qr_id=123)

# UPDATE - Mark scan as processed
update_scan_event(event_id=456, processed=True)

# DELETE - Remove scan data (for compliance)
delete_scan_event(event_id=456)
```

---

## 1.5 CRUD in Everyday Life

Think of a to-do list application:

```
┌──────────────────────────────────────────────┐
│                                              │
│  ✅ Buy groceries        [Edit] [Delete]    │
│  ✅ Call mom             [Edit] [Delete]    │
│  ❌ Finish project       [Edit] [Delete]    │
│                                              │
│      [ + Add New Task ]                      │
│                                              │
└──────────────────────────────────────────────┘

CREATE → Add new task
READ   → View all tasks
UPDATE → Edit task title
DELETE → Remove completed task
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What does CRUD stand for?

**Question 2:** Which operation would you use to retrieve a user's profile?

**Question 3:** In SQAnalytics, what operation records a new QR code scan?

---

## 📝 Section Summary

- **CRUD** is the foundation of all data-driven applications
- Every application manages data through **Create, Read, Update, Delete**
- **SQAnalytics** uses CRUD for QR codes and scan events
- The flow is: **User → API → CRUD → Database**

---

---

# SECTION 2

## WHY CRUD LAYERS EXIST

---

### 📖 Learning Objectives

- Understand the problems CRUD layers solve
- Recognize the importance of separation of concerns
- Identify maintainability and reusability benefits

---

## 2.1 The Problem: Spaghetti Code

### ❌ Bad Architecture

```
┌──────────────┐
│     API      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     SQL      │  ← Raw SQL everywhere
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     SQL      │  ← Duplicate code across endpoints
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     SQL      │  ← Hard to maintain, test, and change
└──────────────┘
```

### 💀 The Symptoms

| Symptom | Impact |
|---------|--------|
| Same SQL in 20+ endpoints | Maintenance nightmare |
| Database changes break everything | High risk of bugs |
| No separation of concerns | Code is impossible to test |
| Business logic mixed with SQL | Can't reuse functionality |

---

## 2.2 The Solution: CRUD Layers

### ✅ Good Architecture

```
┌──────────────┐
│     API      │  ← Handles HTTP requests/responses
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  CRUD Layer  │  ← Data operations in one place
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  DATABASE    │  ← The actual data storage
└──────────────┘
```

---

## 2.3 Benefits of CRUD Layers

### 🎯 Separation of Concerns

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   API Layer      │  CRUD Layer     │  Database Layer      │
│────────────────────────────────────────────────────────────│
│   Validation     │  Data access    │  Storage             │
│   Authentication │  Query building │  Indexing            │
│   Serialization  │  Error handling │  Relationships       │
│   Routing        │  Transactions   │  Performance         │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Each layer has ONE responsibility.**

### 🔄 Reusability

```python
# ❌ Without CRUD Layer - Duplicated code
@app.get("/users/{user_id}")
def get_user(user_id):
    with db_session() as session:
        result = session.execute("SELECT * FROM users WHERE id = ?", user_id)
        return result

@app.get("/users/{user_id}/profile")
def get_profile(user_id):
    with db_session() as session:  # DUPLICATED
        result = session.execute("SELECT * FROM users WHERE id = ?", user_id)  # DUPLICATED
        return result

# ✅ With CRUD Layer - Reusable
@app.get("/users/{user_id}")
def get_user(user_id):
    return crud.get_user(user_id)  # Single source of truth

@app.get("/users/{user_id}/profile")
def get_profile(user_id):
    user = crud.get_user(user_id)  # REUSED
    return build_profile(user)
```

### 🛠️ Maintainability

**Without CRUD Layer:**
```
Change database schema → Update 50 endpoints → ✅ Done
Change column name    → Update 50 endpoints → ❌ Miss one → 💥 Bug
```

**With CRUD Layer:**
```
Change database schema → Update 5 CRUD functions → ✅ Done
Change column name    → Update 5 CRUD functions → ✅ All updated
```

---

## 2.4 CRUD Layers in SQAnalytics

### Before CRUD Layers (😱)

```python
# Each endpoint writes raw SQL
@app.post("/qrs")
def create_qr_endpoint(link, name):
    with db_session() as session:
        result = session.execute(
            "INSERT INTO qrs (link, name) VALUES (?, ?)",
            link, name
        )
        return {"id": result.lastrowid}

@app.post("/qrs/bulk")
def create_qr_bulk_endpoint(qrs):
    with db_session() as session:
        for qr in qrs:
            session.execute(
                "INSERT INTO qrs (link, name) VALUES (?, ?)",
                qr.link, qr.name
            )
        return {"count": len(qrs)}
```

### After CRUD Layers (😊)

```python
# Single CRUD function used by all endpoints
def create_qr(link: str, name: str):
    with db_session() as session:
        result = session.execute(
            "INSERT INTO qrs (link, name) VALUES (?, ?)",
            link, name
        )
        return result.lastrowid

# Clean, reusable endpoints
@app.post("/qrs")
def create_qr_endpoint(link, name):
    return crud.create_qr(link, name)

@app.post("/qrs/bulk")
def create_qr_bulk_endpoint(qrs):
    return [crud.create_qr(qr.link, qr.name) for qr in qrs]
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What problem does a CRUD layer solve?

**Question 2:** Why is separation of concerns important?

**Question 3:** How does a CRUD layer improve maintainability?

---

## 📝 Section Summary

- **Without CRUD layers**, code becomes repetitive and unmaintainable
- **With CRUD layers**, code is organized, reusable, and testable
- **Separation of concerns** means each layer has one job
- **SQAnalytics** benefits from clean data operations

---

---

# SECTION 3

## CRUD ARCHITECTURE FUNDAMENTALS

---

### 📖 Learning Objectives

- Understand the layered architecture of modern applications
- Identify the responsibilities of each layer
- Visualize how layers interact

---

## 3.1 The Four-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                    │
│                    (Frontend / Client)                      │
│                  React, Vue, Mobile App                     │
└───────────────────────────┬─────────────────────────────────┘
                            │ HTTP / API Calls
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                       API LAYER                            │
│                    (FastAPI Endpoints)                     │
│          Routing • Validation • Authentication             │
└───────────────────────────┬─────────────────────────────────┘
                            │ Calls CRUD Functions
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      CRUD LAYER                            │
│               (Data Access / Repository)                    │
│          Business Logic • Data Operations                  │
└───────────────────────────┬─────────────────────────────────┘
                            │ SQL / Queries
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     DATABASE LAYER                         │
│                      (PostgreSQL)                          │
│               Storage • Indexing • Relations               │
└─────────────────────────────────────────────────────────────┘
```

---

## 3.2 Layer Responsibilities

### 🎨 Presentation Layer (Client)

| Responsibility | Example |
|----------------|---------|
| User Interface | Web app, mobile app, API client |
| User Interaction | Click, type, swipe |
| Data Display | Show QR codes, analytics charts |
| User Input | QR code form, scan filters |

### 🔌 API Layer (FastAPI)

| Responsibility | Example |
|----------------|---------|
| Route Handling | `@app.get("/qrs/{id}")` |
| Request Validation | Pydantic schemas |
| Authentication | JWT, API keys |
| Response Formatting | JSON serialization |
| Error Handling | HTTP status codes |

### ⚙️ CRUD Layer (Data Access)

| Responsibility | Example |
|----------------|---------|
| Data Operations | Create, Read, Update, Delete |
| Business Logic | Validate QR code link |
| Query Building | Build SQL statements |
| Transaction Management | Multiple operations in one transaction |
| Error Management | Database exceptions |

### 🗄️ Database Layer (PostgreSQL)

| Responsibility | Example |
|----------------|---------|
| Data Storage | Tables: qrs, scan_events |
| Indexing | Speed up queries |
| Relations | Foreign keys |
| Data Integrity | Constraints, triggers |
| Performance | Query optimization |

---

## 3.3 Dependency Flow

### ✅ Correct Direction

```
┌──────────────┐
│  PRESENTATION│
└──────┬───────┘
       │ (depends on)
       ▼
┌──────────────┐
│     API      │
└──────┬───────┘
       │ (depends on)
       ▼
┌──────────────┐
│    CRUD      │
└──────┬───────┘
       │ (depends on)
       ▼
┌──────────────┐
│  DATABASE    │
└──────────────┘
```

### ❌ Wrong Direction

```
┌──────────────┐
│  PRESENTATION│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  DATABASE    │  ← API bypasses CRUD layer
└──────────────┘
```

> ⚠️ **Warning:** Bypassing layers creates tight coupling and breaks separation of concerns.

---

## 3.4 SQAnalytics Architecture Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                          PRESENTATION LAYER                        │
│                         React Frontend                             │
│                     Dashboard • Analytics • Admin                  │
└────────────────────────────────┬────────────────────────────────────┘
                                 │ HTTP/REST
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                            API LAYER                               │
│                        FastAPI Router                              │
│                                                                     │
│  /api/qrs          │  /api/scans          │  /api/analytics       │
│  ┌───────────────┐ │  ┌───────────────┐ │  ┌───────────────┐     │
│  │ GET /qrs      │ │  │ GET /scans    │ │  │ GET /stats    │     │
│  │ POST /qrs     │ │  │ POST /scans   │ │  │ GET /trends   │     │
│  │ GET /qrs/{id} │ │  │ GET /scans/{ }│ │  │               │     │
│  │ PUT /qrs/{id} │ │  │               │ │  │               │     │
│  │ DELETE /qrs/{id}│ │               │ │  │               │     │
│  └───────────────┘ │  └───────────────┘ │  └───────────────┘     │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                            CRUD LAYER                              │
│                      SQLAlchemy ORM                                │
│                                                                     │
│  qr_crud.py         │  scan_crud.py       │  analytics_crud.py    │
│  ┌───────────────┐ │  ┌───────────────┐ │  ┌───────────────┐     │
│  │ create_qr()   │ │  │ create_scan() │ │  │ get_stats()   │     │
│  │ get_qr()      │ │  │ get_scan()    │ │  │ get_trends()  │     │
│  │ get_qrs()     │ │  │ get_scans()   │ │  │               │     │
│  │ update_qr()   │ │  │ update_scan() │ │  │               │     │
│  │ delete_qr()   │ │  │ delete_scan() │ │  │               │     │
│  └───────────────┘ │  └───────────────┘ │  └───────────────┘     │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          DATABASE LAYER                            │
│                           PostgreSQL                               │
│                                                                     │
│  ┌─────────────────────┐       ┌─────────────────────────────┐    │
│  │       qrs           │       │     scan_events             │    │
│  │─────────────────────│       │─────────────────────────────│    │
│  │ id (PK)            │───┐   │ id (PK)                    │    │
│  │ link               │   │   │ qr_id (FK) ────────────────┘    │
│  │ name               │   └── │ scan_time                   │    │
│  │ created_at         │       │ location                    │    │
│  │ updated_at         │       │ device_type                 │    │
│  │ active             │       │ created_at                  │    │
│  └─────────────────────┘       └─────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3.5 Data Flow Example: Creating a QR Code

```
┌──────────────────┐
│    USER          │
│ Clicks "Create QR"│
└────────┬─────────┘
         │ POST /api/qrs
         ▼
┌──────────────────┐
│   API LAYER      │
│ Validates input  │
│ Checks auth      │
└────────┬─────────┘
         │ create_qr(link, name)
         ▼
┌──────────────────┐
│   CRUD LAYER     │
│ Builds query     │
│ Inserts data     │
└────────┬─────────┘
         │ INSERT INTO qrs
         ▼
┌──────────────────┐
│  DATABASE LAYER  │
│ Saves record     │
│ Returns ID       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   RESPONSE       │
│ {"id": 123}      │
└──────────────────┘
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** Name the four layers in a CRUD architecture.

**Question 2:** What is the responsibility of the API layer?

**Question 3:** Which layer should never directly access the database?

---

## 📝 Section Summary

- **Four layers:** Presentation, API, CRUD, Database
- **Each layer** has a specific responsibility
- **Dependencies flow downward** from presentation to database
- **SQAnalytics** uses a clean layered architecture

---

---

# SECTION 4

## CREATE OPERATIONS

---

### 📖 Learning Objectives

- Understand how to create new records
- Implement validation flows
- Build CRUD create functions
- Handle database insertion

---

## 4.1 The Create Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     CREATE OPERATION FLOW                  │
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│  │  REQUEST │───▶│VALIDATION│───▶│   CRUD   │            │
│  │  DATA    │    │   PASS   │    │  CREATE  │            │
│  └──────────┘    └──────────┘    └────┬─────┘            │
│                                        │                   │
│                                        ▼                   │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│  │ RESPONSE │◀───│   DATA   │◀───│ DATABASE │            │
│  │   BACK   │    │   ID     │    │  INSERT  │            │
│  └──────────┘    └──────────┘    └──────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4.2 Create Operation Components

### 📥 Input Validation

```python
from pydantic import BaseModel, HttpUrl

class QRCreate(BaseModel):
    link: HttpUrl  # Validates URL format
    name: str      # Required field
    
    @validator('name')
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()
```

### ⚙️ CRUD Create Function

```python
from sqlalchemy.orm import Session
from app.models import QRCode
from app.schemas import QRCreate

def create_qr(db: Session, qr_data: QRCreate):
    """
    Create a new QR code in the database.
    
    Args:
        db: Database session
        qr_data: Validated QR code data
        
    Returns:
        QRCode: The created QR code object
    """
    # Create database object
    db_qr = QRCode(
        link=str(qr_data.link),  # Convert URL to string
        name=qr_data.name
    )
    
    # Add to session and commit
    db.add(db_qr)
    db.commit()
    db.refresh(db_qr)  # Refresh with DB-generated data (id, created_at)
    
    return db_qr
```

### 🚀 API Endpoint

```python
from fastapi import FastAPI, Depends, HTTPException
from app.database import get_db
from app.crud import create_qr
from app.schemas import QRCreate, QRResponse

app = FastAPI()

@app.post("/api/qrs", response_model=QRResponse)
def create_qr_endpoint(
    qr_data: QRCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new QR code.
    """
    try:
        db_qr = create_qr(db, qr_data)
        return db_qr
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

## 4.3 Validation Flow in Detail

```
┌─────────────────────────────────────────────────────────────┐
│                     VALIDATION FLOW                         │
│                                                             │
│  ┌──────────────┐                                         │
│  │   RAW INPUT  │   {"link": "not-a-url", "name": ""}     │
│  └──────┬───────┘                                         │
│         │                                                  │
│         ▼                                                  │
│  ┌──────────────┐                                         │
│  │  PYDANTIC   │   Validates types and formats            │
│  │  VALIDATOR  │   ❌ "not-a-url" → Invalid URL          │
│  └──────┬───────┘   ❌ "" → Name cannot be empty          │
│         │                                                  │
│         ▼                                                  │
│  ┌──────────────┐                                         │
│  │   CUSTOM    │   Business logic validation              │
│  │  VALIDATION │   ✅ Link is valid, name is good        │
│  └──────┬───────┘                                         │
│         │                                                  │
│         ▼                                                  │
│  ┌──────────────┐                                         │
│  │  DATABASE   │   Constraint validation                 │
│  │  VALIDATION │   ✅ Unique link, valid foreign keys    │
│  └──────────────┘                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4.4 Create with Dependencies

### Adding Related Data

```python
def create_qr_with_scans(
    db: Session,
    qr_data: QRCreate,
    scan_data: list[ScanCreate]
):
    """
    Create a QR code with initial scan records.
    """
    # 1. Create the QR code
    db_qr = create_qr(db, qr_data)
    
    # 2. Create related scans
    for scan in scan_data:
        db_scan = ScanEvent(
            qr_id=db_qr.id,
            location=scan.location,
            device_type=scan.device_type
        )
        db.add(db_scan)
    
    db.commit()
    return db_qr
```

---

## 4.5 SQAnalytics: Create QR Code

### Complete Implementation

```python
# app/crud/qr_crud.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import QRCode
from app.schemas import QRCreate, QRUpdate

def create_qr(db: Session, qr_data: QRCreate) -> QRCode:
    """
    Create a new QR code.
    
    Handles:
    - Data validation
    - Database insertion
    - Error handling
    - ID generation
    """
    try:
        # Check if link already exists
        existing = db.query(QRCode).filter(
            QRCode.link == str(qr_data.link)
        ).first()
        
        if existing:
            raise ValueError("QR code with this link already exists")
        
        # Create new QR code
        db_qr = QRCode(
            link=str(qr_data.link),
            name=qr_data.name,
            active=True  # Default value
        )
        
        db.add(db_qr)
        db.commit()
        db.refresh(db_qr)
        
        return db_qr
        
    except IntegrityError:
        db.rollback()
        raise ValueError("Database integrity error")
    except Exception as e:
        db.rollback()
        raise ValueError(f"Failed to create QR code: {str(e)}")
```

### API Endpoint

```python
# app/api/qr_endpoints.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.qr_crud import create_qr
from app.schemas import QRCreate, QRResponse

router = APIRouter(prefix="/api/qrs", tags=["QR Codes"])

@router.post("/", response_model=QRResponse, status_code=status.HTTP_201_CREATED)
async def create_new_qr(
    qr_data: QRCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new QR code.
    
    - **link**: Valid URL to encode
    - **name**: Human-readable name for the QR code
    """
    try:
        db_qr = create_qr(db, qr_data)
        return db_qr
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )
```

---

## 4.6 Testing Create Operations

```python
# tests/test_qr_crud.py

def test_create_qr_success(db_session):
    """Test successful QR code creation."""
    qr_data = QRCreate(
        link="https://example.com",
        name="Test QR"
    )
    
    result = create_qr(db_session, qr_data)
    
    assert result.id is not None
    assert result.link == "https://example.com"
    assert result.name == "Test QR"
    assert result.active is True

def test_create_qr_duplicate_link(db_session):
    """Test duplicate link prevention."""
    qr_data = QRCreate(
        link="https://example.com",
        name="First QR"
    )
    create_qr(db_session, qr_data)  # First creation
    
    # Second creation with same link
    duplicate_data = QRCreate(
        link="https://example.com",
        name="Duplicate QR"
    )
    
    with pytest.raises(ValueError, match="already exists"):
        create_qr(db_session, duplicate_data)
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What are the steps in a create operation?

**Question 2:** Why is validation important before creating records?

**Question 3:** What happens after `db.commit()` in SQLAlchemy?

---

## 📝 Section Summary

- **Create operations** insert new data into the database
- **Validation** happens at multiple levels
- **CRUD functions** handle database interaction
- **API endpoints** expose create functionality
- **Error handling** is critical for user experience

---

---

# SECTION 5

## READ OPERATIONS

---

### 📖 Learning Objectives

- Retrieve single and multiple records
- Implement filtering and sorting
- Build flexible read operations
- Optimize database queries

---

## 5.1 The Read Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      READ OPERATION FLOW                   │
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│  │  REQUEST │───▶│  FILTER  │───▶│   CRUD   │            │
│  │  PARAMS  │    │  BUILD   │    │   READ   │            │
│  └──────────┘    └──────────┘    └────┬─────┘            │
│                                        │                   │
│                                        ▼                   │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│  │ RESPONSE │◀───│   DATA   │◀───│ DATABASE │            │
│  │   BACK   │    │  RESULTS │    │  SELECT  │            │
│  └──────────┘    └──────────┘    └──────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 5.2 Two Types of Read Operations

### 📄 Get Single Record

```python
def get_qr(db: Session, qr_id: int) -> QRCode | None:
    """
    Retrieve a single QR code by ID.
    
    Returns:
        QRCode object or None if not found
    """
    return db.query(QRCode).filter(QRCode.id == qr_id).first()
```

### 📚 Get Multiple Records

```python
def get_qrs(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    active_only: bool = True
) -> list[QRCode]:
    """
    Retrieve multiple QR codes with pagination.
    """
    query = db.query(QRCode)
    
    if active_only:
        query = query.filter(QRCode.active == True)
    
    return query.offset(skip).limit(limit).all()
```

---

## 5.3 Advanced Filtering

### Filter by Multiple Criteria

```python
from typing import Optional
from datetime import datetime

def filter_qrs(
    db: Session,
    name_contains: Optional[str] = None,
    created_after: Optional[datetime] = None,
    active: Optional[bool] = None,
    skip: int = 0,
    limit: int = 100
) -> list[QRCode]:
    """
    Filter QR codes with multiple criteria.
    """
    query = db.query(QRCode)
    
    # Apply filters dynamically
    if name_contains:
        query = query.filter(QRCode.name.contains(name_contains))
    
    if created_after:
        query = query.filter(QRCode.created_at >= created_after)
    
    if active is not None:
        query = query.filter(QRCode.active == active)
    
    return query.offset(skip).limit(limit).all()
```

---

## 5.4 Read Operation Patterns

### Pattern 1: Find or Create

```python
def get_or_create_qr(db: Session, link: str) -> QRCode:
    """
    Get existing QR code or create new one.
    """
    qr = db.query(QRCode).filter(QRCode.link == link).first()
    
    if qr is None:
        qr = QRCode(link=link, name=f"Auto: {link}")
        db.add(qr)
        db.commit()
        db.refresh(qr)
    
    return qr
```

### Pattern 2: Find by Alternate Key

```python
def get_qr_by_link(db: Session, link: str) -> QRCode | None:
    """
    Find QR code by its link (alternate key).
    """
    return db.query(QRCode).filter(QRCode.link == link).first()
```

### Pattern 3: Count Records

```python
def count_qrs(db: Session, active_only: bool = True) -> int:
    """
    Count total QR codes.
    """
    query = db.query(QRCode)
    
    if active_only:
        query = query.filter(QRCode.active == True)
    
    return query.count()
```

---

## 5.5 API Endpoints for Reading

### Get Single QR

```python
from fastapi import HTTPException, status

@router.get("/{qr_id}", response_model=QRResponse)
async def get_qr_by_id(
    qr_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a QR code by its ID.
    """
    db_qr = get_qr(db, qr_id)
    
    if db_qr is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code with id {qr_id} not found"
        )
    
    return db_qr
```

### Get All QRs with Filters

```python
@router.get("/", response_model=list[QRResponse])
async def get_all_qrs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    name_contains: Optional[str] = Query(None),
    active_only: bool = Query(True),
    db: Session = Depends(get_db)
):
    """
    Get all QR codes with pagination and filtering.
    """
    qrs = filter_qrs(
        db,
        name_contains=name_contains,
        active=active_only,
        skip=skip,
        limit=limit
    )
    return qrs
```

---

## 5.6 Relationship Loading

### Eager Loading

```python
from sqlalchemy.orm import joinedload

def get_qr_with_scans(db: Session, qr_id: int) -> QRCode | None:
    """
    Retrieve QR code with its scan events pre-loaded.
    """
    return db.query(QRCode).options(
        joinedload(QRCode.scan_events)
    ).filter(QRCode.id == qr_id).first()
```

### Nested Response

```python
class QRWithScansResponse(QRResponse):
    scan_events: list[ScanEventResponse] = []

@router.get("/{qr_id}/with-scans", response_model=QRWithScansResponse)
async def get_qr_with_scans_endpoint(
    qr_id: int,
    db: Session = Depends(get_db)
):
    """
    Get QR code with all its scan events.
    """
    db_qr = get_qr_with_scans(db, qr_id)
    
    if db_qr is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code with id {qr_id} not found"
        )
    
    return db_qr
```

---

## 5.7 Performance Optimization

### Query Optimization Tips

```python
# ❌ Bad: N+1 Problem
def get_qrs_with_scans_bad(db: Session):
    qrs = get_qrs(db)
    for qr in qrs:
        scans = get_scans_by_qr(db, qr.id)  # N+1 queries!
    return qrs

# ✅ Good: Eager Loading
def get_qrs_with_scans_good(db: Session):
    return db.query(QRCode).options(
        joinedload(QRCode.scan_events)
    ).all()
```

### Use Specific Columns

```python
def get_qr_basic_info(db: Session):
    """Only get needed columns instead of full objects."""
    return db.query(
        QRCode.id,
        QRCode.name,
        QRCode.created_at
    ).all()
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What's the difference between `first()` and `all()`?

**Question 2:** How do you implement pagination?

**Question 3:** What is the N+1 query problem?

---

## 📝 Section Summary

- **Read operations** retrieve data from the database
- **Two types:** single record and multiple records
- **Filters** narrow down results
- **Pagination** manages large result sets
- **Eager loading** prevents N+1 query issues

---

---

# SECTION 6

## UPDATE OPERATIONS

---

### 📖 Learning Objectives

- Update existing records
- Implement partial updates
- Maintain data integrity during updates
- Handle concurrent updates

---

## 6.1 The Update Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     UPDATE OPERATION FLOW                  │
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│  │  REQUEST │───▶│  FIND    │───▶│  UPDATE  │            │
│  │  DATA    │    │  RECORD  │    │  FIELDS  │            │
│  └──────────┘    └────┬─────┘    └────┬─────┘            │
│                        │               │                   │
│                        ▼               ▼                   │
│                    ┌──────────────────────┐                │
│                    │   DATABASE UPDATE    │                │
│                    │     `UPDATE SET`     │                │
│                    └──────────────────────┘                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6.2 Full Update vs Partial Update

### 🔄 Full Update (PUT)

```python
def update_qr_full(
    db: Session,
    qr_id: int,
    qr_data: QRUpdate
) -> QRCode | None:
    """
    Full update: All fields must be provided.
    """
    db_qr = get_qr(db, qr_id)
    
    if db_qr is None:
        return None
    
    # Update all fields
    db_qr.link = str(qr_data.link)
    db_qr.name = qr_data.name
    db_qr.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_qr)
    
    return db_qr
```

### 🎯 Partial Update (PATCH)

```python
def update_qr_partial(
    db: Session,
    qr_id: int,
    qr_data: QRUpdatePartial
) -> QRCode | None:
    """
    Partial update: Only update provided fields.
    """
    db_qr = get_qr(db, qr_id)
    
    if db_qr is None:
        return None
    
    # Only update fields that were provided
    update_data = qr_data.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        if field == 'link':
            setattr(db_qr, field, str(value))
        else:
            setattr(db_qr, field, value)
    
    db_qr.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_qr)
    
    return db_qr
```

---

## 6.3 Update Schemas

### Full Update Schema

```python
from pydantic import BaseModel, HttpUrl

class QRUpdate(BaseModel):
    """All fields required for update."""
    link: HttpUrl
    name: str
    
    @validator('name')
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()
```

### Partial Update Schema

```python
from pydantic import BaseModel, HttpUrl, Optional

class QRUpdatePartial(BaseModel):
    """All fields optional for partial update."""
    link: Optional[HttpUrl] = None
    name: Optional[str] = None
    
    @validator('name')
    def name_not_empty(cls, v):
        if v is not None and not v.strip():
            raise ValueError('Name cannot be empty')
        return v
```

---

## 6.4 Data Integrity During Updates

### 🔐 Concurrent Updates

```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import StaleDataError

def update_qr_safe(
    db: Session,
    qr_id: int,
    qr_data: QRUpdatePartial,
    expected_version: int
) -> QRCode | None:
    """
    Safe update with optimistic locking.
    """
    db_qr = get_qr(db, qr_id)
    
    if db_qr is None:
        return None
    
    # Check version to prevent concurrent updates
    if db_qr.version != expected_version:
        raise StaleDataError(
            "Record was modified by another user"
        )
    
    # Update fields
    update_data = qr_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_qr, field, value)
    
    # Increment version
    db_qr.version += 1
    db_qr.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_qr)
    
    return db_qr
```

### ✅ Validation During Updates

```python
def update_qr_with_validation(
    db: Session,
    qr_id: int,
    qr_data: QRUpdatePartial
) -> QRCode | None:
    """
    Validate updates before applying.
    """
    db_qr = get_qr(db, qr_id)
    
    if db_qr is None:
        return None
    
    # Validate link uniqueness (if link is being changed)
    if qr_data.link is not None:
        existing = db.query(QRCode).filter(
            QRCode.link == str(qr_data.link),
            QRCode.id != qr_id  # Exclude current record
        ).first()
        
        if existing:
            raise ValueError("Link already in use")
    
    # Apply updates
    update_data = qr_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_qr, field, value)
    
    db_qr.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_qr)
    
    return db_qr
```

---

## 6.5 SQAnalytics: Update QR Code

### Complete Implementation

```python
# app/crud/qr_crud.py

def update_qr(
    db: Session,
    qr_id: int,
    qr_data: QRUpdatePartial
) -> QRCode:
    """
    Update a QR code.
    
    Features:
    - Partial updates
    - Validation
    - Concurrent update protection
    - Business rule enforcement
    """
    # Find the QR code
    db_qr = db.query(QRCode).filter(QRCode.id == qr_id).first()
    
    if not db_qr:
        raise ValueError(f"QR code {qr_id} not found")
    
    # Business rule: Active QR codes can't be modified
    if db_qr.active and qr_data.name is not None:
        # Allow updates to active QRs, but log it
        # This is a business rule specific to SQAnalytics
        pass
    
    # Check link uniqueness
    if qr_data.link is not None:
        existing = db.query(QRCode).filter(
            QRCode.link == str(qr_data.link),
            QRCode.id != qr_id
        ).first()
        
        if existing:
            raise ValueError(f"Link {qr_data.link} already in use")
    
    # Apply updates
    update_data = qr_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        if field == 'link':
            setattr(db_qr, field, str(value))
        else:
            setattr(db_qr, field, value)
    
    db_qr.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_qr)
    
    return db_qr
```

### API Endpoint

```python
# app/api/qr_endpoints.py

@router.patch("/{qr_id}", response_model=QRResponse)
async def update_qr_endpoint(
    qr_id: int,
    qr_data: QRUpdatePartial,
    db: Session = Depends(get_db)
):
    """
    Update a QR code.
    
    - Partial updates: Only send fields to change
    - Validates link uniqueness
    - Automatically updates `updated_at`
    """
    try:
        db_qr = update_qr(db, qr_id, qr_data)
        return db_qr
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
```

---

## 6.6 Batch Updates

```python
def batch_update_qrs(
    db: Session,
    qr_ids: list[int],
    qr_data: QRUpdatePartial
) -> dict:
    """
    Update multiple QR codes with the same data.
    
    Returns:
        Dict with success and failure counts
    """
    successful = []
    failed = []
    
    for qr_id in qr_ids:
        try:
            updated = update_qr(db, qr_id, qr_data)
            successful.append(qr_id)
        except ValueError as e:
            failed.append({"id": qr_id, "error": str(e)})
    
    return {
        "successful": successful,
        "failed": failed,
        "total_processed": len(qr_ids),
        "success_count": len(successful),
        "failure_count": len(failed)
    }
```

---

## 6.7 Update Checklist

| Step | Action | Why |
|------|--------|-----|
| 1 | Find record | Verify it exists |
| 2 | Validate data | Ensure data quality |
| 3 | Check permissions | Security |
| 4 | Apply updates | Modify fields |
| 5 | Handle conflicts | Concurrent updates |
| 6 | Save changes | Persist to database |
| 7 | Return updated | Confirm success |

---

## 🔍 Knowledge Checkpoint

**Question 1:** What's the difference between PUT and PATCH?

**Question 2:** Why should you validate link uniqueness during updates?

**Question 3:** How do you handle concurrent updates?

---

## 📝 Section Summary

- **Full updates (PUT)** require all fields
- **Partial updates (PATCH)** only change provided fields
- **Validation** maintains data integrity
- **Concurrency handling** prevents lost updates
- **Batch updates** handle multiple records

---

---

# SECTION 7

## DELETE OPERATIONS

---

### 📖 Learning Objectives

- Understand hard vs soft deletion
- Implement deletion strategies
- Handle foreign key constraints
- Manage business implications of deletion

---

## 7.1 Deletion Strategies

```
┌─────────────────────────────────────────────────────────────┐
│                   DELETION STRATEGIES                      │
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐               │
│  │   HARD DELETE   │    │   SOFT DELETE   │               │
│  │─────────────────│    │─────────────────│               │
│  │ Permanently     │    │ Mark as deleted │               │
│  │ remove data     │    │ Keep record     │               │
│  │                 │    │                 │               │
│  │ Irreversible    │    │ Reversible      │               │
│  │ No recovery     │    │ Can restore     │               │
│  │                 │    │                 │               │
│  │ Free space      │    │ Data retained   │               │
│  │ Improve perf    │    │ Historical data │               │
│  └─────────────────┘    └─────────────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7.2 Hard Delete (Permanent)

### Implementation

```python
def delete_qr_hard(db: Session, qr_id: int) -> bool:
    """
    Permanently delete a QR code.
    
    Warning: This operation cannot be undone!
    """
    db_qr = db.query(QRCode).filter(QRCode.id == qr_id).first()
    
    if db_qr is None:
        return False
    
    # Check for dependent records
    if db_qr.scan_events:
        # Option 1: Cascade delete
        for scan in db_qr.scan_events:
            db.delete(scan)
        
        # Option 2: Prevent deletion
        # raise ValueError("Cannot delete QR with existing scans")
    
    db.delete(db_qr)
    db.commit()
    
    return True
```

### Considerations

| Aspect | Impact |
|--------|--------|
| **Recovery** | ❌ Impossible without backups |
| **Space** | ✅ Frees storage |
| **Performance** | ✅ Improves query performance |
| **Audit** | ❌ Loses historical data |
| **Referential Integrity** | ⚠️ Must handle foreign keys |

---

## 7.3 Soft Delete (Reversible)

### Model with Soft Delete

```python
from sqlalchemy import Boolean, DateTime
from datetime import datetime

class QRCode(Base):
    __tablename__ = "qrs"
    
    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Soft delete fields
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, default=False)
```

### Soft Delete Implementation

```python
def delete_qr_soft(db: Session, qr_id: int) -> bool:
    """
    Soft delete a QR code.
    
    Mark as deleted but keep data for recovery.
    """
    db_qr = db.query(QRCode).filter(QRCode.id == qr_id).first()
    
    if db_qr is None:
        return False
    
    # Mark as deleted
    db_qr.is_deleted = True
    db_qr.deleted_at = datetime.utcnow()
    
    db.commit()
    
    return True

def restore_qr(db: Session, qr_id: int) -> bool:
    """
    Restore a soft-deleted QR code.
    """
    db_qr = db.query(QRCode).filter(QRCode.id == qr_id).first()
    
    if db_qr is None:
        return False
    
    # Restore from deletion
    db_qr.is_deleted = False
    db_qr.deleted_at = None
    
    db.commit()
    
    return True
```

### Query with Soft Deletes

```python
def get_active_qrs(db: Session):
    """Only get non-deleted QR codes."""
    return db.query(QRCode).filter(QRCode.is_deleted == False).all()

def get_all_qrs_include_deleted(db: Session):
    """Get all QR codes including soft-deleted ones."""
    return db.query(QRCode).all()

def get_deleted_qrs(db: Session):
    """Get only soft-deleted QR codes."""
    return db.query(QRCode).filter(QRCode.is_deleted == True).all()
```

---

## 7.4 Deletion with Cascading

### Database-Level Cascade

```python
class ScanEvent(Base):
    __tablename__ = "scan_events"
    
    id = Column(Integer, primary_key=True)
    qr_id = Column(Integer, ForeignKey("qrs.id", ondelete="CASCADE"))
    location = Column(String)
    scan_time = Column(DateTime, default=datetime.utcnow)
    
    # This relationship will cascade deletes
    qr = relationship("QRCode", back_populates="scan_events")
```

### Application-Level Cascade

```python
def delete_qr_with_cascade(db: Session, qr_id: int):
    """
    Delete QR code and all its scan events.
    """
    # Find QR code
    db_qr = db.query(QRCode).filter(QRCode.id == qr_id).first()
    
    if not db_qr:
        return False
    
    # Delete scan events manually
    db.query(ScanEvent).filter(ScanEvent.qr_id == qr_id).delete()
    
    # Delete QR code
    db.delete(db_qr)
    db.commit()
    
    return True
```

---

## 7.5 SQAnalytics: Delete Scenarios

### Scenario 1: Delete Unused QR

```python
def delete_qr_if_no_scans(db: Session, qr_id: int) -> dict:
    """
    Delete QR code only if it has no scan events.
    """
    db_qr = get_qr(db, qr_id)
    
    if not db_qr:
        return {"success": False, "message": "QR not found"}
    
    if db_qr.scan_events:
        return {
            "success": False,
            "message": "Cannot delete QR with scan events",
            "scan_count": len(db_qr.scan_events)
        }
    
    db.delete(db_qr)
    db.commit()
    
    return {"success": True, "message": "QR deleted"}
```

### Scenario 2: Archive Before Delete

```python
def archive_and_delete_qr(
    db: Session,
    qr_id: int
) -> dict:
    """
    Archive QR data before deletion.
    """
    db_qr = get_qr(db, qr_id)
    
    if not db_qr:
        return {"success": False, "message": "QR not found"}
    
    # 1. Archive data
    archive_data = {
        "qr": db_qr.__dict__,
        "scans": [s.__dict__ for s in db_qr.scan_events],
        "deleted_at": datetime.utcnow().isoformat()
    }
    
    # 2. Save archive (e.g., to another table or file)
    # archive.save_archive("qr_delete", qr_id, archive_data)
    
    # 3. Delete from main table
    db.delete(db_qr)
    db.commit()
    
    return {
        "success": True,
        "message": "QR archived and deleted",
        "archived_data": archive_data
    }
```

### Scenario 3: Bulk Soft Delete

```python
def bulk_soft_delete_qrs(
    db: Session,
    qr_ids: list[int]
) -> dict:
    """
    Soft delete multiple QR codes.
    """
    successful = []
    failed = []
    
    for qr_id in qr_ids:
        try:
            delete_qr_soft(db, qr_id)
            successful.append(qr_id)
        except Exception as e:
            failed.append({"id": qr_id, "error": str(e)})
    
    db.commit()
    
    return {
        "successful": successful,
        "failed": failed,
        "total": len(qr_ids)
    }
```

---

## 7.6 API Endpoints

```python
# Hard Delete
@router.delete("/{qr_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qr_hard_endpoint(
    qr_id: int,
    db: Session = Depends(get_db)
):
    """
    Permanently delete a QR code.
    
    Warning: This cannot be undone!
    """
    success = delete_qr_hard(db, qr_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code {qr_id} not found"
        )
    
    return None  # 204 No Content

# Soft Delete
@router.patch("/{qr_id}/soft-delete", response_model=QRResponse)
async def soft_delete_qr_endpoint(
    qr_id: int,
    db: Session = Depends(get_db)
):
    """
    Soft delete a QR code (can be restored).
    """
    success = delete_qr_soft(db, qr_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code {qr_id} not found"
        )
    
    return get_qr(db, qr_id)

# Restore
@router.patch("/{qr_id}/restore", response_model=QRResponse)
async def restore_qr_endpoint(
    qr_id: int,
    db: Session = Depends(get_db)
):
    """
    Restore a soft-deleted QR code.
    """
    success = restore_qr(db, qr_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code {qr_id} not found"
        )
    
    return get_qr(db, qr_id)
```

---

## 7.7 Deletion Best Practices

### ✅ DO

| Practice | Why |
|----------|-----|
| **Use soft deletes** | Recoverable, historical data |
| **Log deletions** | Audit trail |
| **Check dependencies** | Prevent broken relationships |
| **Confirm with user** | Prevent accidental deletions |
| **Batch operations** | Efficient bulk operations |

### ❌ DON'T

| Practice | Why |
|----------|-----|
| **Hard delete by default** | No recovery possible |
| **Delete without confirmation** | User errors |
| **Ignore cascade effects** | Data integrity issues |
| **Skip audit logging** | No accountability |

---

## 🔍 Knowledge Checkpoint

**Question 1:** What's the difference between hard and soft delete?

**Question 2:** When would you use hard delete instead of soft delete?

**Question 3:** Why is audit logging important for deletions?

---

## 📝 Section Summary

- **Hard delete** permanently removes data
- **Soft delete** marks data as deleted but retains it
- **Cascading** handles related records
- **Audit logging** provides accountability
- **Restoration** possible with soft delete

---

---

# SECTION 8

## SQLALCHEMY CRUD PATTERNS

---

### 📖 Learning Objectives

- Understand SQLAlchemy ORM patterns
- Implement CRUD with SQLAlchemy
- Manage sessions and transactions
- Build query-based operations

---

## 8.1 SQLAlchemy Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   SQLALCHEMY ARCHITECTURE                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  APPLICATION CODE                    │   │
│  └─────────────────────────┬───────────────────────────┘   │
│                            │                                │
│  ┌─────────────────────────▼───────────────────────────┐   │
│  │                    SQLALCHEMY ORM                    │   │
│  │                                                     │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │   │
│  │  │   Models     │  │   Session    │  │  Query   │  │   │
│  │  │  (Classes)   │  │  (Unit of    │  │  Builder │  │   │
│  │  │              │  │   Work)      │  │          │  │   │
│  │  └──────────────┘  └──────────────┘  └──────────┘  │   │
│  └─────────────────────────┬───────────────────────────┘   │
│                            │                                │
│  ┌─────────────────────────▼───────────────────────────┐   │
│  │                   CORE SQLALCHEMY                   │   │
│  │      (Connection Pooling, Engine, Dialect)          │   │
│  └─────────────────────────┬───────────────────────────┘   │
│                            │                                │
│  ┌─────────────────────────▼───────────────────────────┐   │
│  │                 POSTGRESQL DATABASE                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 8.2 SQLAlchemy Models

### QR Code Model

```python
# app/models.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class QRCode(Base):
    __tablename__ = "qrs"
    
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)
    
    # Relationships
    scan_events = relationship("ScanEvent", back_populates="qr", cascade="all, delete-orphan")

class ScanEvent(Base):
    __tablename__ = "scan_events"
    
    id = Column(Integer, primary_key=True, index=True)
    qr_id = Column(Integer, ForeignKey("qrs.id"), nullable=False)
    location = Column(String)
    device_type = Column(String)
    scan_time = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    qr = relationship("QRCode", back_populates="scan_events")
```

---

## 8.3 Session Management

### Session Dependency

```python
# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

DATABASE_URL = "postgresql://user:password@localhost/sqanalytics"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency to provide database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_db_context():
    """
    Context manager for database sessions.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Using Session

```python
# Using dependency (FastAPI)
@app.get("/qrs")
def get_qrs(db: Session = Depends(get_db)):
    return get_all_qrs(db)

# Using context manager
with get_db_context() as db:
    qr = create_qr(db, qr_data)
```

---

## 8.4 CRUD Patterns with SQLAlchemy

### CREATE Pattern

```python
def create_qr(db: Session, link: str, name: str) -> QRCode:
    """
    Create pattern with SQLAlchemy.
    """
    # 1. Create instance
    db_qr = QRCode(
        link=link,
        name=name
    )
    
    # 2. Add to session
    db.add(db_qr)
    
    # 3. Commit
    db.commit()
    
    # 4. Refresh with DB data
    db.refresh(db_qr)
    
    return db_qr
```

### READ Patterns

```python
# Get by ID
def get_qr(db: Session, qr_id: int) -> QRCode | None:
    return db.query(QRCode).filter(QRCode.id == qr_id).first()

# Get with filter
def get_qr_by_link(db: Session, link: str) -> QRCode | None:
    return db.query(QRCode).filter(QRCode.link == link).first()

# Get all with filters
def get_qrs(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    active_only: bool = True
) -> list[QRCode]:
    query = db.query(QRCode)
    
    if active_only:
        query = query.filter(QRCode.active == True)
    
    return query.offset(skip).limit(limit).all()

# Count
def count_qrs(db: Session) -> int:
    return db.query(QRCode).count()
```

### UPDATE Pattern

```python
def update_qr(
    db: Session,
    qr_id: int,
    link: str | None = None,
    name: str | None = None
) -> QRCode | None:
    """
    Update pattern with SQLAlchemy.
    """
    # 1. Find record
    db_qr = db.query(QRCode).filter(QRCode.id == qr_id).first()
    
    if not db_qr:
        return None
    
    # 2. Update fields
    if link is not None:
        db_qr.link = link
    if name is not None:
        db_qr.name = name
    
    # 3. Commit
    db.commit()
    
    # 4. Refresh
    db.refresh(db_qr)
    
    return db_qr
```

### DELETE Pattern

```python
def delete_qr(db: Session, qr_id: int) -> bool:
    """
    Delete pattern with SQLAlchemy.
    """
    # 1. Find record
    db_qr = db.query(QRCode).filter(QRCode.id == qr_id).first()
    
    if not db_qr:
        return False
    
    # 2. Delete
    db.delete(db_qr)
    
    # 3. Commit
    db.commit()
    
    return True
```

---

## 8.5 Advanced Query Patterns

### Query with Joins

```python
def get_qr_with_scans(db: Session, qr_id: int) -> QRCode | None:
    """
    Get QR code with scan events using join.
    """
    return db.query(QRCode).options(
        joinedload(QRCode.scan_events)
    ).filter(QRCode.id == qr_id).first()
```

### Query with Aggregations

```python
from sqlalchemy import func

def get_scan_stats(db: Session, qr_id: int) -> dict:
    """
    Get scan statistics for a QR code.
    """
    result = db.query(
        func.count(ScanEvent.id).label('total_scans'),
        func.count(ScanEvent.location.distinct()).label('unique_locations'),
        func.count(ScanEvent.device_type.distinct()).label('unique_devices')
    ).filter(ScanEvent.qr_id == qr_id).first()
    
    return {
        'total_scans': result.total_scans or 0,
        'unique_locations': result.unique_locations or 0,
        'unique_devices': result.unique_devices or 0
    }
```

### Query with Group By

```python
def get_scans_by_location(db: Session, qr_id: int) -> list[dict]:
    """
    Group scans by location.
    """
    results = db.query(
        ScanEvent.location,
        func.count(ScanEvent.id).label('scan_count')
    ).filter(ScanEvent.qr_id == qr_id).group_by(
        ScanEvent.location
    ).all()
    
    return [
        {'location': r.location, 'count': r.scan_count}
        for r in results
    ]
```

---

## 8.6 Transaction Management

### Single Transaction

```python
def create_qr_with_scans_transaction(
    db: Session,
    qr_data: dict,
    scan_data_list: list[dict]
) -> QRCode:
    """
    Multiple operations in one transaction.
    """
    try:
        # 1. Create QR code
        db_qr = QRCode(**qr_data)
        db.add(db_qr)
        db.flush()  # Get ID without committing
        
        # 2. Create scan events
        for scan_data in scan_data_list:
            db_scan = ScanEvent(
                qr_id=db_qr.id,
                **scan_data
            )
            db.add(db_scan)
        
        # 3. Commit all together
        db.commit()
        db.refresh(db_qr)
        
        return db_qr
    
    except Exception as e:
        db.rollback()
        raise ValueError(f"Transaction failed: {str(e)}")
```

### Nested Transactions (Savepoints)

```python
def complex_operation(db: Session):
    """
    Using savepoints for nested transactions.
    """
    # Outer transaction
    try:
        qr = create_qr(db, link="https://test.com", name="Test")
        
        # Savepoint
        try:
            # This might fail
            update_qr(db, qr.id, name="New Name")
        except Exception:
            # Rollback to savepoint, keep QR creation
            db.rollback()
            # Continue with other operations...
        
        db.commit()
        
    except Exception:
        db.rollback()
        raise
```

---

## 8.7 Performance Tips

### 🚀 Optimization Techniques

```python
# Bulk operations
def bulk_create_qrs(db: Session, qr_list: list[dict]) -> list[QRCode]:
    """
    Bulk insert for better performance.
    """
    db.bulk_insert_mappings(QRCode, qr_list)
    db.commit()
    
    # Need to query them back
    return db.query(QRCode).filter(
        QRCode.link.in_([q['link'] for q in qr_list])
    ).all()

# Batch operations
def batch_update_qrs(db: Session, updates: list[dict]):
    """
    Batch updates in one session.
    """
    for update in updates:
        db.query(QRCode).filter(QRCode.id == update['id']).update(
            {QRCode.name: update['name']}
        )
    db.commit()
```

### 📊 Query Optimization

```python
# Use selectinload for relationships
from sqlalchemy.orm import selectinload

def get_qrs_efficient(db: Session):
    """Use selectinload to avoid N+1."""
    return db.query(QRCode).options(
        selectinload(QRCode.scan_events)
    ).all()

# Use only needed columns
def get_qr_names(db: Session):
    """Only select needed columns."""
    return db.query(QRCode.id, QRCode.name).all()
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** What is the purpose of SQLAlchemy Session?

**Question 2:** How do you handle transactions in SQLAlchemy?

**Question 3:** What's the difference between `joinedload` and `selectinload`?

---

## 📝 Section Summary

- **SQLAlchemy** provides ORM for database interaction
- **Session** manages unit of work
- **Query builder** constructs SQL queries
- **Transactions** ensure data consistency
- **Optimization** improves performance

---

---

# SECTION 9

## FASTAPI + CRUD INTEGRATION

---

### 📖 Learning Objectives

- Integrate CRUD functions with FastAPI endpoints
- Handle request/response cycles
- Implement dependency injection
- Build complete API endpoints

---

## 9.1 The Integration Flow

```
┌─────────────────────────────────────────────────────────────┐
│               FASTAPI + CRUD INTEGRATION FLOW              │
│                                                             │
│  ┌──────────────┐                                         │
│  │   CLIENT     │   HTTP Request                          │
│  └──────┬───────┘   POST /api/qrs                         │
│         │           Body: {"link": "...", "name": "..."}   │
│         ▼                                                  │
│  ┌──────────────────────────────────────────────┐         │
│  │          FASTAPI APPLICATION                │         │
│  │                                              │         │
│  │  1. Route: @app.post("/api/qrs")            │         │
│  │  2. Validate: Pydantic schema               │         │
│  │  3. Get DB: Depends(get_db)                 │         │
│  │  4. Call CRUD: create_qr(db, data)          │         │
│  │  5. Return: QRResponse                      │         │
│  └──────────────┬───────────────────────────────┘         │
│                 │                                          │
│                 ▼                                          │
│  ┌──────────────────────────────────────────────┐         │
│  │          CRUD FUNCTION                       │         │
│  │                                              │         │
│  │  create_qr(db, qr_data):                     │         │
│  │    1. Build SQLAlchemy object               │         │
│  │    2. Execute operation                     │         │
│  │    3. Return result                         │         │
│  └──────────────┬───────────────────────────────┘         │
│                 │                                          │
│                 ▼                                          │
│  ┌──────────────────────────────────────────────┐         │
│  │          POSTGRESQL DATABASE                 │         │
│  │                                              │         │
│  │  INSERT INTO qrs (link, name) ...            │         │
│  └──────────────┬───────────────────────────────┘         │
│                 │                                          │
│                 ▼                                          │
│  ┌──────────────┐                                         │
│  │   RESPONSE   │   {"id": 123, "link": "...", ...}      │
│  └──────────────┘                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 9.2 Complete API Setup

### Project Structure

```
sqanalytics-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py           # Database setup
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic schemas
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── qr_crud.py
│   │   └── scan_crud.py
│   └── api/
│       ├── __init__.py
│       ├── qr_endpoints.py
│       └── scan_endpoints.py
└── requirements.txt
```

### FastAPI Application

```python
# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import qr_endpoints, scan_endpoints

app = FastAPI(
    title="SQAnalytics API",
    description="Smart QR Analytics Platform",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(qr_endpoints.router)
app.include_router(scan_endpoints.router)

@app.get("/")
async def root():
    return {"message": "SQAnalytics API"}
```

---

## 9.3 Complete CRUD + API Example

### Schemas (Pydantic)

```python
# app/schemas.py

from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from typing import Optional

class QRBase(BaseModel):
    link: HttpUrl
    name: str = Field(..., min_length=1, max_length=100)

class QRCreate(QRBase):
    pass

class QRUpdate(BaseModel):
    link: Optional[HttpUrl] = None
    name: Optional[str] = Field(None, min_length=1, max_length=100)

class QRResponse(QRBase):
    id: int
    active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
```

### CRUD Functions

```python
# app/crud/qr_crud.py

from sqlalchemy.orm import Session
from app.models import QRCode
from app.schemas import QRCreate, QRUpdate
from datetime import datetime

def create_qr(db: Session, qr_data: QRCreate) -> QRCode:
    db_qr = QRCode(
        link=str(qr_data.link),
        name=qr_data.name
    )
    db.add(db_qr)
    db.commit()
    db.refresh(db_qr)
    return db_qr

def get_qr(db: Session, qr_id: int) -> QRCode | None:
    return db.query(QRCode).filter(QRCode.id == qr_id).first()

def get_qrs(db: Session, skip: int = 0, limit: int = 100) -> list[QRCode]:
    return db.query(QRCode).offset(skip).limit(limit).all()

def update_qr(db: Session, qr_id: int, qr_data: QRUpdate) -> QRCode | None:
    db_qr = get_qr(db, qr_id)
    if not db_qr:
        return None
    
    if qr_data.link is not None:
        db_qr.link = str(qr_data.link)
    if qr_data.name is not None:
        db_qr.name = qr_data.name
    
    db_qr.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_qr)
    return db_qr

def delete_qr(db: Session, qr_id: int) -> bool:
    db_qr = get_qr(db, qr_id)
    if not db_qr:
        return False
    
    db.delete(db_qr)
    db.commit()
    return True
```

### API Endpoints

```python
# app/api/qr_endpoints.py

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.crud.qr_crud import (
    create_qr, get_qr, get_qrs, update_qr, delete_qr
)
from app.schemas import QRCreate, QRUpdate, QRResponse

router = APIRouter(prefix="/api/qrs", tags=["QR Codes"])

@router.post("/", response_model=QRResponse, status_code=status.HTTP_201_CREATED)
async def create_qr_endpoint(
    qr_data: QRCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new QR code.
    """
    try:
        return create_qr(db, qr_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=List[QRResponse])
async def get_all_qrs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """
    Get all QR codes with pagination.
    """
    return get_qrs(db, skip=skip, limit=limit)

@router.get("/{qr_id}", response_model=QRResponse)
async def get_qr_by_id(
    qr_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a QR code by ID.
    """
    db_qr = get_qr(db, qr_id)
    
    if not db_qr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code {qr_id} not found"
        )
    
    return db_qr

@router.patch("/{qr_id}", response_model=QRResponse)
async def update_qr_endpoint(
    qr_id: int,
    qr_data: QRUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a QR code.
    """
    db_qr = update_qr(db, qr_id, qr_data)
    
    if not db_qr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code {qr_id} not found"
        )
    
    return db_qr

@router.delete("/{qr_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_qr_endpoint(
    qr_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a QR code.
    """
    success = delete_qr(db, qr_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code {qr_id} not found"
        )
```

---

## 9.4 Dependency Injection

### Custom Dependencies

```python
# app/dependencies.py

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.qr_crud import get_qr
from app.models import QRCode

async def get_qr_or_404(
    qr_id: int,
    db: Session = Depends(get_db)
) -> QRCode:
    """
    Dependency to get QR code or raise 404.
    """
    db_qr = get_qr(db, qr_id)
    if not db_qr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"QR code {qr_id} not found"
        )
    return db_qr

# Using the dependency
@router.get("/{qr_id}/scans")
async def get_qr_scans(
    qr: QRCode = Depends(get_qr_or_404),
    db: Session = Depends(get_db)
):
    return qr.scan_events
```

---

## 9.5 Error Handling

### Global Exception Handler

```python
# app/main.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": "Database integrity error",
            "message": str(exc.orig)
        }
    )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )
```

---

## 🔍 Knowledge Checkpoint

**Question 1:** How does FastAPI integrate with CRUD functions?

**Question 2:** What is the purpose of Pydantic schemas?

**Question 3:** How do you handle errors in FastAPI?

---

## 📝 Section Summary

- **FastAPI endpoints** call CRUD functions
- **Pydantic schemas** validate input/output
- **Dependency injection** provides database sessions
- **Error handling** ensures proper HTTP responses
- **Clean architecture** separates concerns

---

---

# SECTION 10

## COMMON DEVELOPER MISTAKES

---

### 📖 Learning Objectives

- Identify common CRUD mistakes
- Understand their impact
- Implement solutions and best practices
- Write maintainable code

---

## 10.1 Mistake: Writing SQL in Endpoints

### ❌ The Problem

```python
@app.get("/qrs")
def get_qrs(db: Session = Depends(get_db)):
    # ❌ Raw SQL in API endpoint
    result = db.execute("SELECT * FROM qrs WHERE active = true")
    return result.fetchall()

@app.get("/qrs/{qr_id}")
def get_qr(qr_id: int, db: Session = Depends(get_db)):
    # ❌ More raw SQL
    result = db.execute("SELECT * FROM qrs WHERE id = ?", qr_id)
    return result.fetchone()
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Duplicate SQL everywhere | Maintenance nightmare |
| Database changes break many files | High risk |
| No abstraction | Can't reuse logic |

### ✅ Solution

```python
# CRUD layer
def get_active_qrs(db: Session):
    return db.query(QRCode).filter(QRCode.active == True).all()

def get_qr_by_id(db: Session, qr_id: int):
    return db.query(QRCode).filter(QRCode.id == qr_id).first()

# Endpoints
@app.get("/qrs")
def get_qrs(db: Session = Depends(get_db)):
    return get_active_qrs(db)

@app.get("/qrs/{qr_id}")
def get_qr(qr_id: int, db: Session = Depends(get_db)):
    return get_qr_by_id(db, qr_id)
```

---

## 10.2 Mistake: Duplicate Database Code

### ❌ The Problem

```python
# Endpoint 1
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).filter(User.active == True).all()

# Endpoint 2
@app.get("/admin/users")
def get_admin_users(db: Session = Depends(get_db)):
    return db.query(User).filter(User.active == True).all()

# Endpoint 3
@app.get("/users/export")
def export_users(db: Session = Depends(get_db)):
    users = db.query(User).filter(User.active == True).all()
    return export_to_csv(users)
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Same query in 3+ places | Duplication |
| Fixing requires updating all | Time-consuming |
| Risk of inconsistency | Bug-prone |

### ✅ Solution

```python
# CRUD layer - Single source of truth
def get_active_users(db: Session):
    return db.query(User).filter(User.active == True).all()

# All endpoints use the same function
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return get_active_users(db)

@app.get("/admin/users")
def get_admin_users(db: Session = Depends(get_db)):
    return get_active_users(db)

@app.get("/users/export")
def export_users(db: Session = Depends(get_db)):
    users = get_active_users(db)
    return export_to_csv(users)
```

---

## 10.3 Mistake: Poor Function Naming

### ❌ The Problem

```python
def do_stuff(db, x, y):
    # What does this do?
    pass

def update(db, data):
    # Update what?
    pass

def get(db, id):
    # Get what?
    pass
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Unclear purpose | Confusion |
| Hidden side effects | Bugs |
| Hard to maintain | Slow development |

### ✅ Solution

```python
# Clear, descriptive names
def get_qr_by_id(db: Session, qr_id: int) -> QRCode | None:
    """Get a QR code by its ID."""
    pass

def get_active_qrs_by_user(db: Session, user_id: int) -> list[QRCode]:
    """Get all active QR codes for a specific user."""
    pass

def deactivate_expired_qrs(db: Session) -> int:
    """Deactivate QR codes that have expired. Returns count affected."""
    pass
```

---

## 10.4 Mistake: Missing Error Handling

### ❌ The Problem

```python
@app.post("/qrs")
def create_qr(qr_data: QRCreate, db: Session = Depends(get_db)):
    # ❌ No error handling
    db_qr = QRCode(link=qr_data.link, name=qr_data.name)
    db.add(db_qr)
    db.commit()
    return db_qr
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Database errors crash API | Poor UX |
| No user feedback | Confusion |
| Corrupted data possible | Data integrity issues |

### ✅ Solution

```python
@app.post("/qrs", response_model=QRResponse)
def create_qr(qr_data: QRCreate, db: Session = Depends(get_db)):
    try:
        db_qr = QRCode(link=qr_data.link, name=qr_data.name)
        db.add(db_qr)
        db.commit()
        db.refresh(db_qr)
        return db_qr
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="QR code with this link already exists"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )
```

---

## 10.5 Mistake: Mixing Business Logic with CRUD

### ❌ The Problem

```python
def create_qr(db: Session, link: str, name: str, user_id: int):
    # ❌ Business logic in CRUD layer
    if user_id not in allowed_users:
        raise ValueError("User not authorized")
    
    if len(name) > 100:
        raise ValueError("Name too long")
    
    # Business rule: Premium users have special links
    user = get_user(db, user_id)
    if user.is_premium:
        link = f"/premium/{link}"
    
    db_qr = QRCode(link=link, name=name)
    db.add(db_qr)
    db.commit()
    return db_qr
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| CRUD layer knows about users | Coupling |
| Business rules scattered | Hard to change |
| Can't reuse CRUD for different contexts | Limited flexibility |

### ✅ Solution

```python
# CRUD layer - Pure data operations
def create_qr(db: Session, link: str, name: str) -> QRCode:
    """Pure data operation with no business logic."""
    db_qr = QRCode(link=link, name=name)
    db.add(db_qr)
    db.commit()
    db.refresh(db_qr)
    return db_qr

# Service layer - Business logic
def create_qr_with_business_rules(
    db: Session, 
    link: str, 
    name: str, 
    user_id: int
) -> QRCode:
    """Business logic layer."""
    # Validate permissions
    if not is_authorized(user_id):
        raise PermissionError("User not authorized")
    
    # Apply business rules
    if len(name) > 100:
        raise ValueError("Name too long")
    
    user = get_user(db, user_id)
    if user.is_premium:
        link = f"/premium/{link}"
    
    # Pure CRUD operation
    return create_qr(db, link, name)
```

---

## 10.6 Mistake: Not Using Database Transactions

### ❌ The Problem

```python
def transfer_scans(db: Session, from_qr: int, to_qr: int):
    # ❌ No transaction
    scans = get_scans_by_qr(db, from_qr)
    
    for scan in scans:
        # Update one by one
        scan.qr_id = to_qr
        db.commit()  # ❌ Commits for each record!
    
    # If something fails, partial updates committed
```

### 🔴 Symptoms

| Symptom | Impact |
|---------|--------|
| Partial updates | Data inconsistency |
| No rollback | Corrupted data |
| Performance issues | Multiple round trips |

### ✅ Solution

```python
def transfer_scans(db: Session, from_qr: int, to_qr: int):
    try:
        # ✅ Single transaction
        db.query(ScanEvent).filter(
            ScanEvent.qr_id == from_qr
        ).update({ScanEvent.qr_id: to_qr})
        
        db.commit()
        return {"success": True}
    
    except Exception:
        db.rollback()
        raise ValueError("Transfer failed")
```

---

## 10.7 Common Mistakes Summary

| # | Mistake | Solution |
|---|---------|----------|
| 1 | SQL in endpoints | Use CRUD layer |
| 2 | Duplicate database code | Abstract to CRUD functions |
| 3 | Poor function naming | Clear, descriptive names |
| 4 | Missing error handling | Try/except with rollback |
| 5 | Mixing business logic | Separate service layer |
| 6 | No transactions | Single commit per operation |
| 7 | N+1 queries | Use eager loading |
| 8 | Ignoring pagination | Implement skip/limit |
| 9 | Hardcoding values | Use environment variables |
| 10 | No validation | Use Pydantic schemas |

---

## 🔍 Knowledge Checkpoint

**Question 1:** Why should you avoid writing SQL in endpoints?

**Question 2:** How does the service layer differ from CRUD layer?

**Question 3:** What happens if you don't use transactions?

---

## 📝 Section Summary

- **Write SQL in CRUD layer**, not endpoints
- **One function = one responsibility**
- **Use clear function names**
- **Always handle errors and rollback on failure**
- **Separate business logic from data operations**

---

---

# SECTION 11

## SQANALYTICS CASE STUDY

---

### 📖 Learning Objectives

- Apply CRUD principles to real project
- Design complete QR code management
- Build scan event tracking
- Understand design decisions

---

## 11.1 SQAnalytics Overview

**SQAnalytics** is a Smart QR Analytics Platform that:

1. Generates QR codes for links
2. Tracks when QR codes are scanned
3. Provides analytics about scan patterns

### Data Model

```
┌─────────────────────────────────────────────────────────────┐
│                      DATA MODEL                            │
│                                                             │
│  ┌─────────────────────┐       ┌─────────────────────────┐ │
│  │       QRCode        │       │      ScanEvent          │ │
│  │─────────────────────│       │─────────────────────────│ │
│  │ id (PK)            │───┐   │ id (PK)                │ │
│  │ link (unique)      │   │   │ qr_id (FK) ────────────┘ │
│  │ name               │   └── │ location                │ │
│  │ active             │       │ device_type             │ │
│  │ created_at         │       │ scan_time              │ │
│  │ updated_at         │       │ created_at              │ │
│  │ is_deleted         │       │                         │ │
│  │ deleted_at         │       │                         │ │
│  └─────────────────────┘       └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 11.2 QR Code CRUD Implementation

### CREATE QR Code

```python
# app/crud/qr_crud.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import QRCode
from app.schemas import QRCreate
from datetime import datetime

def create_qr(db: Session, qr_data: QRCreate) -> QRCode:
    """
    Create a new QR code.
    
    Design Decisions:
    - Validate link uniqueness
    - Set default values (active=True)
    - Handle duplicate link errors
    - Return complete object with DB-generated fields
    """
    # Check for existing link
    existing = db.query(QRCode).filter(
        QRCode.link == str(qr_data.link)
    ).first()
    
    if existing:
        raise ValueError(f"Link {qr_data.link} already exists")
    
    # Create new QR code
    db_qr = QRCode(
        link=str(qr_data.link),
        name=qr_data.name,
        active=True,  # Default: active on creation
        is_deleted=False
    )
    
    try:
        db.add(db_qr)
        db.commit()
        db.refresh(db_qr)
        return db_qr
    except IntegrityError:
        db.rollback()
        raise ValueError("Database integrity error")
```

### READ QR Code

```python
def get_qr(db: Session, qr_id: int) -> QRCode | None:
    """
    Get a QR code by ID.
    
    Design Decisions:
    - Exclude soft-deleted records
    - Return None if not found
    - Used for all read operations
    """
    return db.query(QRCode).filter(
        QRCode.id == qr_id,
        QRCode.is_deleted == False
    ).first()

def get_qrs(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    active_only: bool = True,
    search: str | None = None
) -> list[QRCode]:
    """
    Get QR codes with filters.
    
    Design Decisions:
    - Pagination (skip/limit)
    - Optional filtering
    - Exclude soft-deleted
    """
    query = db.query(QRCode).filter(QRCode.is_deleted == False)
    
    if active_only:
        query = query.filter(QRCode.active == True)
    
    if search:
        query = query.filter(QRCode.name.contains(search))
    
    return query.offset(skip).limit(limit).all()

def get_qr_stats(db: Session) -> dict:
    """
    Get QR code statistics.
    
    Design Decisions:
    - Single query for all stats
    - Return dict with meaningful keys
    """
    from sqlalchemy import func
    
    total = db.query(QRCode).filter(QRCode.is_deleted == False).count()
    active = db.query(QRCode).filter(
        QRCode.active == True,
        QRCode.is_deleted == False
    ).count()
    
    return {
        "total": total,
        "active": active,
        "inactive": total - active
    }
```

### UPDATE QR Code

```python
def update_qr(
    db: Session,
    qr_id: int,
    qr_data: QRUpdate
) -> QRCode | None:
    """
    Update a QR code.
    
    Design Decisions:
    - Partial updates via exclude_unset
    - Update timestamp automatically
    - Validate link uniqueness
    - Return updated object
    """
    db_qr = get_qr(db, qr_id)
    
    if not db_qr:
        return None
    
    update_data = qr_data.dict(exclude_unset=True)
    
    # Validate link uniqueness if changing
    if 'link' in update_data:
        existing = db.query(QRCode).filter(
            QRCode.link == str(update_data['link']),
            QRCode.id != qr_id,
            QRCode.is_deleted == False
        ).first()
        
        if existing:
            raise ValueError("Link already in use")
    
    # Apply updates
    for field, value in update_data.items():
        setattr(db_qr, field, value)
    
    # Update timestamp
    db_qr.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_qr)
    return db_qr
```

### DELETE QR Code

```python
def delete_qr(db: Session, qr_id: int) -> bool:
    """
    Soft delete a QR code.
    
    Design Decisions:
    - Soft delete (reversible)
    - Check for active scans
    - Log deletion time
    """
    db_qr = get_qr(db, qr_id)
    
    if not db_qr:
        return False
    
    # Check for recent scans (business rule)
    recent_scans = db.query(ScanEvent).filter(
        ScanEvent.qr_id == qr_id,
        ScanEvent.scan_time > datetime.utcnow() - timedelta(days=30)
    ).count()
    
    if recent_scans > 0:
        raise ValueError("Cannot delete QR with scans in the last 30 days")
    
    # Soft delete
    db_qr.is_deleted = True
    db_qr.deleted_at = datetime.utcnow()
    
    db.commit()
    return True

def restore_qr(db: Session, qr_id: int) -> QRCode | None:
    """
    Restore a soft-deleted QR code.
    
    Design Decisions:
    - Check if restore is allowed
    - Clear deletion timestamps
    """
    db_qr = db.query(QRCode).filter(
        QRCode.id == qr_id,
        QRCode.is_deleted == True
    ).first()
    
    if not db_qr:
        return None
    
    # Check if link is now in use by another QR
    existing = db.query(QRCode).filter(
        QRCode.link == db_qr.link,
        QRCode.id != qr_id,
        QRCode.is_deleted == False
    ).first()
    
    if existing:
        raise ValueError("Link is now in use by another QR code")
    
    # Restore
    db_qr.is_deleted = False
    db_qr.deleted_at = None
    db_qr.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_qr)
    return db_qr
```

---

## 11.3 Scan Event CRUD Implementation

### CREATE Scan Event

```python
# app/crud/scan_crud.py

def create_scan_event(
    db: Session,
    qr_id: int,
    location: str | None = None,
    device_type: str | None = None
) -> ScanEvent:
    """
    Record a QR code scan.
    
    Design Decisions:
    - Validate QR code exists
    - Auto-fill scan_time
    - Increment scan count (optional optimization)
    """
    # Verify QR exists
    qr = get_qr(db, qr_id)
    if not qr:
        raise ValueError(f"QR code {qr_id} not found")
    
    # Create scan event
    db_scan = ScanEvent(
        qr_id=qr_id,
        location=location,
        device_type=device_type,
        scan_time=datetime.utcnow()
    )
    
    db.add(db_scan)
    db.commit()
    db.refresh(db_scan)
    
    # Optional: Update QR scan count (if denormalized)
    # qr.scan_count = db.query(ScanEvent).filter(ScanEvent.qr_id == qr_id).count()
    # db.commit()
    
    return db_scan
```

### READ Scan Events

```python
def get_scans_by_qr(
    db: Session,
    qr_id: int,
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    limit: int = 100
) -> list[ScanEvent]:
    """
    Get scan events for a QR code.
    
    Design Decisions:
    - Date range filtering
    - Most recent first
    - Limit for performance
    """
    query = db.query(ScanEvent).filter(ScanEvent.qr_id == qr_id)
    
    if start_date:
        query = query.filter(ScanEvent.scan_time >= start_date)
    
    if end_date:
        query = query.filter(ScanEvent.scan_time <= end_date)
    
    return query.order_by(ScanEvent.scan_time.desc()).limit(limit).all()

def get_scan_analytics(
    db: Session,
    qr_id: int,
    period: str = "day"
) -> dict:
    """
    Get analytics for a QR code.
    
    Design Decisions:
    - Group by time period
    - Return structured analytics
    - Single query for performance
    """
    from sqlalchemy import func
    
    # Determine grouping
    if period == "day":
        group_by = func.date_trunc('day', ScanEvent.scan_time)
    elif period == "hour":
        group_by = func.date_trunc('hour', ScanEvent.scan_time)
    else:
        group_by = func.date_trunc('month', ScanEvent.scan_time)
    
    # Query analytics
    results = db.query(
        group_by.label('period'),
        func.count(ScanEvent.id).label('count')
    ).filter(ScanEvent.qr_id == qr_id).group_by(
        group_by
    ).order_by(group_by).all()
    
    return {
        "period": period,
        "data": [
            {"period": r.period, "count": r.count}
            for r in results
        ],
        "total": sum(r.count for r in results)
    }

def get_scans_by_location(
    db: Session,
    qr_id: int
) -> list[dict]:
    """
    Get scan counts by location.
    
    Design Decisions:
    - Group by location
    - Sort by popularity
    - Include location names
    """
    results = db.query(
        ScanEvent.location,
        func.count(ScanEvent.id).label('count')
    ).filter(
        ScanEvent.qr_id == qr_id,
        ScanEvent.location.isnot(None)
    ).group_by(
        ScanEvent.location
    ).order_by(
        func.count(ScanEvent.id).desc()
    ).limit(10).all()
    
    return [
        {"location": r.location, "count": r.count}
        for r in results
    ]
```

---

## 11.4 Complete API Endpoints

### QR Code Endpoints

```python
# app/api/qr_endpoints.py

@router.post("/", response_model=QRResponse)
async def create_qr_endpoint(
    qr_data: QRCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_qr(db, qr_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[QRResponse])
async def get_all_qrs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    active_only: bool = Query(True),
    search: str | None = Query(None),
    db: Session = Depends(get_db)
):
    return get_qrs(db, skip=skip, limit=limit, active_only=active_only, search=search)

@router.get("/stats", response_model=QRStatsResponse)
async def get_qr_stats_endpoint(
    db: Session = Depends(get_db)
):
    return get_qr_stats(db)

@router.get("/{qr_id}", response_model=QRResponse)
async def get_qr_endpoint(
    qr_id: int,
    db: Session = Depends(get_db)
):
    db_qr = get_qr(db, qr_id)
    if not db_qr:
        raise HTTPException(status_code=404, detail=f"QR {qr_id} not found")
    return db_qr

@router.patch("/{qr_id}", response_model=QRResponse)
async def update_qr_endpoint(
    qr_id: int,
    qr_data: QRUpdate,
    db: Session = Depends(get_db)
):
    try:
        db_qr = update_qr(db, qr_id, qr_data)
        if not db_qr:
            raise HTTPException(status_code=404, detail=f"QR {qr_id} not found")
        return db_qr
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{qr_id}", status_code=204)
async def delete_qr_endpoint(
    qr_id: int,
    db: Session = Depends(get_db)
):
    try:
        success = delete_qr(db, qr_id)
        if not success:
            raise HTTPException(status_code=404, detail=f"QR {qr_id} not found")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### Scan Event Endpoints

```python
# app/api/scan_endpoints.py

@router.post("/", response_model=ScanEventResponse)
async def create_scan_endpoint(
    scan_data: ScanCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_scan_event(
            db,
            qr_id=scan_data.qr_id,
            location=scan_data.location,
            device_type=scan_data.device_type
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/qr/{qr_id}", response_model=list[ScanEventResponse])
async def get_scans_by_qr_endpoint(
    qr_id: int,
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    return get_scans_by_qr(db, qr_id, limit=limit)

@router.get("/analytics/{qr_id}",