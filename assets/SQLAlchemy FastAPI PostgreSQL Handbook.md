# SQLAlchemy for FastAPI & PostgreSQL
## A Practical Beginner Guide for Building SQAnalytics

---

# Cover Page

<div style="text-align: center; padding: 40px 0;">

# SQLAlchemy for FastAPI & PostgreSQL

## A Practical Beginner Guide for Building SQAnalytics

**Version 1.0**

---

### Learning Path

```mermaid
graph LR
    A[Frontend] --> B[FastAPI]
    B --> C[SQLAlchemy]
    C --> D[PostgreSQL]
```

### Project Context: SQAnalytics

A Smart QR Analytics Platform built with:
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Enterprise-grade database
- **SQLAlchemy** - ORM for database interaction
- **Supabase** - PostgreSQL hosting

---

*"From Zero SQLAlchemy to Production-Ready in One Guide"*

</div>

---

# Learning Objectives

By completing this handbook, you will understand:

### Fundamental Concepts
- **What SQLAlchemy is** - The Python ORM ecosystem
- **Why ORMs exist** - The problem they solve
- **Database abstraction** - Working with databases using Python

### Technical Skills
- **Creating database engines** - Connecting to PostgreSQL
- **Managing sessions** - The unit of work pattern
- **Building models** - Mapping Python classes to tables
- **Writing CRUD operations** - Create, Read, Update, Delete
- **Querying data** - Filtering, sorting, and retrieving

### Integration
- **FastAPI integration** - Dependency injection for database sessions
- **Production patterns** - Session management and error handling
- **Project structure** - Organizing code for real-world applications

---

# Executive Summary

## The SQAnalytics Architecture

```mermaid
graph TD
    U[User] --> F[FastAPI]
    F --> S[SQLAlchemy]
    S --> P[PostgreSQL]
    
    subgraph "Request Flow"
        U -->|HTTP Request| F
        F -->|ORM Operations| S
        S -->|SQL Queries| P
        P -->|Results| S
        S -->|Python Objects| F
        F -->|HTTP Response| U
    end
```

### How It All Connects

| Layer | Component | Responsibility |
|-------|-----------|----------------|
| **User** | Browser/Client | Sends HTTP requests |
| **FastAPI** | API Routes | Handles requests, uses ORM |
| **SQLAlchemy** | ORM Layer | Maps Python to SQL |
| **PostgreSQL** | Database | Stores and retrieves data |

### The ORM Layer Explained

```mermaid
graph LR
    subgraph "Python Application"
        M[SQLAlchemy Models]
        S[SQLAlchemy Session]
        Q[Query Builder]
    end
    
    subgraph "Database Layer"
        T[Database Tables]
        R[SQL Statements]
        D[Raw Data]
    end
    
    M -->|Maps| T
    S -->|Manages| R
    Q -->|Generates| R
```

**Key Insight**: SQLAlchemy acts as a translator between your Python code and PostgreSQL, converting Python objects to SQL queries and vice versa.

---

# Table of Contents

1. [Section 1: What is SQLAlchemy?](#section-1)
2. [Section 2: Why ORMs Exist](#section-2)
3. [Section 3: SQLAlchemy Architecture](#section-3)
4. [Section 4: Understanding Engines](#section-4)
5. [Section 5: Understanding Sessions](#section-5)
6. [Section 6: Building Models](#section-6)
7. [Section 7: CRUD Operations](#section-7)
8. [Section 8: Querying Data](#section-8)
9. [Section 9: FastAPI Integration](#section-9)
10. [Section 10: SQAnalytics Case Study](#section-10)
11. [Section 11: Common Mistakes](#section-11)
12. [Section 12: Hands-On Exercises](#section-12)
13. [Section 13: Production Checklist](#section-13)
14. [SQLAlchemy Cheat Sheet](#cheat-sheet)
15. [SQLAlchemy Roadmap](#roadmap)
16. [Knowledge Check](#knowledge-check)

---

# Section 1: What is SQLAlchemy?

## The Simple Explanation

**SQLAlchemy** is a Python library that helps you talk to databases using Python code instead of writing SQL by hand.

```mermaid
graph LR
    A[Your Python Code] --> B[SQLAlchemy]
    B --> C[PostgreSQL]
    C --> B
    B --> A
```

## The Real-World Analogy

### The Library Analogy

Imagine you're a librarian (your Python code) who needs to organize books (database records). Without SQLAlchemy, you'd have to:

1. Memorize the exact location of every book
2. Write detailed instructions in a special language (SQL)
3. Constantly check if your instructions are correct

**With SQLAlchemy**, you get:

1. A **card catalog system** that tracks all books
2. A **helpful assistant** who speaks your language
3. **Automatic updates** when books are moved

## Why SQLAlchemy Exists

```mermaid
graph TD
    subgraph "Problems Solved by SQLAlchemy"
        P1[Writing Raw SQL] --> S1[Pythonic Interface]
        P2[Database Differences] --> S2[Unified API]
        P3[Manual Security] --> S3[Built-in Protection]
        P4[Siloed Code] --> S4[Reusable Models]
    end
```

## SQAnalytics Example

```python
# Without SQLAlchemy (Raw SQL)
import psycopg2
conn = psycopg2.connect("dbname=sqanalytics user=admin")
cursor = conn.cursor()
cursor.execute("SELECT * FROM qr_codes WHERE id = %s", (1,))
row = cursor.fetchone()
print(f"QR Code: {row[1]}")  # What is row[1] again?

# With SQLAlchemy
from sqlalchemy.orm import Session
qr_code = session.get(QRCode, 1)
print(f"QR Code: {qr_code.title}")  # Clear and Pythonic!
```

### The Difference at a Glance

| Aspect | Raw SQL | SQLAlchemy |
|--------|---------|------------|
| **Code Style** | Strings | Python objects |
| **Type Safety** | Manual | Automatic |
| **Portability** | Database-specific | Database-agnostic |
| **Maintainability** | Difficult | Easy |
| **Security** | Manual handling | Built-in protection |

---

## 🔍 Learning Checkpoint

**Test Your Understanding**

1. SQLAlchemy is primarily used for:
   - a) Web development
   - b) Database interaction in Python
   - c) Frontend frameworks
   - d) Data visualization

2. What problem does SQLAlchemy solve?
   - a) Writing complex SQL queries
   - b) Bridge between Python and databases
   - c) Managing web servers
   - d) UI development

**[Answers: 1-b, 2-b]**

---

# Section 2: Why ORMs Exist

## Understanding the Problem

### The Raw SQL Reality

```python
# The messy reality of raw SQL in Python
def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # No validation, error-prone
    sql = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(sql)
    
    # Manual mapping
    row = cursor.fetchone()
    user = {
        'id': row[0],
        'name': row[1],
        'email': row[2],
        'created_at': row[3]
    }
    return user
```

### The ORM Alternative

```python
# Clean, Pythonic ORM approach
def get_user_by_id(user_id):
    with Session() as session:
        user = session.get(User, user_id)
        return user
```

## ORM Benefits Visualized

```mermaid
graph TD
    subgraph "WITH ORM"
        O1[Write Python Code] --> O2[SQLAlchemy Generates SQL]
        O2 --> O3[Automatic Result Mapping]
        O3 --> O4[Get Python Objects]
    end
    
    subgraph "WITHOUT ORM"
        W1[Write SQL Strings] --> W2[Execute with Driver]
        W2 --> W3[Parse Results Manually]
        W3 --> W4[Create Dictionaries/Objects]
    end
```

## Comparison Table

| Criterion | Raw SQL | SQLAlchemy ORM |
|-----------|---------|----------------|
| **Learning Curve** | Low for basic queries | Moderate |
| **Productivity** | Low (manual work) | High (automated) |
| **Database Agnostic** | No | Yes (largely) |
| **Query Safety** | Manual | Built-in |
| **Code Maintainability** | Poor | Excellent |
| **Performance** | Can be optimized | Good (with tweaking) |
| **Testing** | Difficult | Easy (models are Python) |

## Why ORMs for SQAnalytics?

```mermaid
graph TD
    subgraph "SQAnalytics Requirements"
        R1[Complex Data Models] --> O1[ORM handles relations]
        R2[Fast Development] --> O2[Write less code]
        R3[Multiple Developers] --> O3[Clear, consistent patterns]
        R4[Future Changes] --> O4[Easy to modify models]
    end
```

---

## 📊 Knowledge Recap

- **ORMs** (Object-Relational Mappers) convert between Python objects and database tables
- **Without ORM**: You write raw SQL strings and manually map results
- **With ORM**: You work with Python objects, and SQLAlchemy handles the rest
- **Key Benefit**: Focus on business logic, not database plumbing

---

# Section 3: SQLAlchemy Architecture

## The Big Picture

```mermaid
graph TD
    subgraph "Your Application"
        F[FastAPI Application]
        M[SQLAlchemy Models]
    end
    
    subgraph "SQLAlchemy Core"
        E[Engine] -->|Connection Pool| P[PostgreSQL]
        S[Session] -->|Unit of Work| E
        Q[Query] -->|Builds SQL| S
        M2[Declarative Base] -->|Defines Tables| E
    end
    
    F -->|Uses| M
    M -->|Inherits from| M2
    F -->|Creates| S
    S -->|Executes| Q
```

## Component Breakdown

### 1. Engine
- **Role**: Database connection manager
- **Function**: Creates connections to PostgreSQL
- **Lifecycle**: Created once per application

```python
from sqlalchemy import create_engine
engine = create_engine("postgresql://user:pass@localhost/db")
```

### 2. Session
- **Role**: Unit of work manager
- **Function**: Manages all database operations
- **Lifecycle**: Created per request

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

### 3. Model
- **Role**: Table definition
- **Function**: Maps Python class to database table
- **Lifecycle**: Defined once per table

```python
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class QRCode(Base):
    __tablename__ = "qr_codes"
    id = Column(Integer, primary_key=True)
```

### 4. Query
- **Role**: Data retrieval
- **Function**: Builds SQL SELECT statements
- **Lifecycle**: Created per query

```python
qr_codes = session.query(QRCode).filter(QRCode.status == "active")
```

## Request Lifecycle

```mermaid
sequenceDiagram
    participant F as FastAPI Route
    participant S as Session
    participant E as Engine
    participant P as PostgreSQL
    
    F->>S: 1. Create Session
    S->>E: 2. Get Connection
    E->>P: 3. Connect to DB
    F->>S: 4. Query Data
    S->>E: 5. Build SQL
    E->>P: 6. Execute Query
    P-->>E: 7. Return Results
    E-->>S: 8. Map Results
    S-->>F: 9. Return Objects
    F->>S: 10. Commit
    S->>E: 11. Commit Transaction
    S->>F: 12. Close Session
```

## Component Responsibilities

| Component | Responsibility | Created By |
|-----------|---------------|------------|
| **Engine** | Connection pooling, database driver | Application |
| **Session** | Unit of work, transactions | Per request |
| **Model** | Table schema, relationships | Development |
| **Query** | Data retrieval, filtering | Per query |

---

## 🎯 Key Insight

The **Session** is the most important component for daily work. It's your gateway to all database operations.

---

# Section 4: Understanding Engines

## What is an Engine?

The Engine is SQLAlchemy's **connection manager**. It handles:
- Creating database connections
- Managing connection pooling
- Translating SQLAlchemy to database-specific SQL

## Creating an Engine

### Basic Engine

```python
from sqlalchemy import create_engine

# PostgreSQL connection string
DATABASE_URL = "postgresql://user:password@localhost:5432/sqanalytics"
engine = create_engine(DATABASE_URL)
```

### Engine with Configuration

```python
engine = create_engine(
    DATABASE_URL,
    pool_size=10,           # Maximum connections in pool
    max_overflow=20,        # Extra connections if needed
    pool_pre_ping=True,     # Check connection before using
    echo=False              # Log SQL (True for debugging)
)
```

## Connection String Format

```mermaid
graph LR
    subgraph "postgresql://user:password@host:port/database"
        A[postgresql://] --> B[user]
        B --> C[:password]
        C --> D[@host]
        D --> E[:port]
        E --> F[/database]
    end
```

### Example Connection Strings

| Environment | Connection String |
|-------------|-------------------|
| Local | `postgresql://admin:pass@localhost:5432/sqanalytics` |
| Supabase | `postgresql://postgres:pass@db.example.supabase.co:5432/postgres` |
| Production | `postgresql://app_user:secure@prod-db:5432/app_db` |

## Engine Creation Flow

```mermaid
graph TD
    A[Create Engine] --> B{Configuration?}
    B -->|Yes| C[Apply Settings]
    B -->|No| D[Use Defaults]
    C --> E[Initialize Connection Pool]
    D --> E
    E --> F[Ready for Sessions]
```

## Engine Methods

```python
# Check engine status
print(engine.url)           # Connection details
print(engine.pool.status()) # Pool statistics

# Execute raw SQL
with engine.connect() as conn:
    result = conn.execute("SELECT 1")
    
# Create tables
Base.metadata.create_all(engine)
```

## Troubleshooting Engines

### Connection Issues

```python
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        conn.execute("SELECT 1")
except Exception as e:
    print(f"Connection failed: {e}")
    # Check:
    # - Database is running
    # - Credentials are correct
    # - Network accessibility
```

---

## 🔧 Best Practices

1. **Create engine once** - Reuse across application
2. **Use environment variables** - Don't hardcode credentials
3. **Set appropriate pool sizes** - Match your database capacity
4. **Enable connection checking** - Use `pool_pre_ping=True`

---

# Section 5: Understanding Sessions

## What is a Session?

A Session represents a **unit of work** - a temporary workspace where all changes are tracked before being saved to the database.

## Session Lifecycle

```mermaid
graph TD
    S[Start] --> A[Create Session]
    A --> B[Work with Data]
    B --> C{Save Changes?}
    C -->|Yes| D[Commit]
    C -->|No| E[Rollback]
    D --> F[Close Session]
    E --> F
    F --> G[End]
```

## Creating Sessions

### Basic Session

```python
from sqlalchemy.orm import sessionmaker

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create session
session = SessionLocal()
```

### Session Context Manager

```python
# Recommended pattern
with SessionLocal() as session:
    # Work with database
    qr_code = session.get(QRCode, 1)
    session.commit()
    # Session automatically closes
```

## The Unit of Work Pattern

```mermaid
graph TD
    subgraph "Session Workspace"
        A[Add Object] --> T[Track Changes]
        U[Update Object] --> T
        D[Delete Object] --> T
        T --> C[Commit All]
        C --> DB[(Database)]
    end
```

## Session Operations

### Common Methods

```python
# Add objects
session.add(qr_code)
session.add_all([qr1, qr2, qr3])

# Query objects
qr = session.query(QRCode).filter_by(short_code="abc123").first()

# Get object by ID
qr = session.get(QRCode, 1)

# Save changes
session.commit()

# Revert changes
session.rollback()

# Remove object
session.delete(qr_code)
```

## Session State Diagram

```mermaid
graph LR
    T[Transient] -->|add| P[Pending]
    P -->|flush| F[Flushed]
    F -->|commit| D[Detached]
    P -->|rollback| T
    D -->|merge| P
```

### State Meanings

| State | Description | Example |
|-------|-------------|---------|
| **Transient** | Not associated with session | `qr = QRCode()` |
| **Pending** | Added to session, not saved | `session.add(qr)` |
| **Flushed** | SQL generated, not committed | Query sees it |
| **Detached** | Saved, session closed | `session.commit(); session.close()` |

## Common Mistakes

### ❌ Session Leak

```python
# BAD: Session not closed
session = SessionLocal()
qr = session.query(QRCode).first()
# Session remains open - bad for resources!
```

### ✅ Proper Session Management

```python
# GOOD: Using context manager
with SessionLocal() as session:
    qr = session.query(QRCode).first()
    session.commit()
# Session auto-closed
```

---

## 🎯 Session Best Practices

1. **Always close sessions** - Use context managers
2. **Keep sessions short** - Open, work, close
3. **One session per request** - Don't share across requests
4. **Always commit or rollback** - No half-baked transactions
5. **Use dependency injection** - Let FastAPI manage sessions

---

# Section 6: Building Models

## What are Models?

Models are Python classes that map to database tables. SQLAlchemy handles all the conversion between Python objects and database rows.

## Model Structure

```mermaid
graph TD
    subgraph "Model Components"
        C[Class Definition] --> T[__tablename__]
        C --> A[Attributes]
        C --> R[Relationships]
        A --> A1[Columns]
        A --> A2[Data Types]
        A --> A3[Constraints]
    end
```

## Creating the Base

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

# Create declarative base
Base = declarative_base()

# All models will inherit from Base
```

## QRCode Model for SQAnalytics

```python
class QRCode(Base):
    __tablename__ = "qr_codes"
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Business Fields
    short_code = Column(String(50), unique=True, nullable=False, index=True)
    title = Column(String(200), nullable=False)
    destination_url = Column(String(500), nullable=False)
    
    # Status & Tracking
    status = Column(String(20), default="active")
    scan_count = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

## Table Mapping Visual

```mermaid
graph LR
    subgraph "Python Class"
        P1[id: int]
        P2[short_code: str]
        P3[title: str]
        P4[destination_url: str]
        P5[status: str]
        P6[scan_count: int]
        P7[created_at: datetime]
    end
    
    subgraph "Database Table"
        T1[id INTEGER]
        T2[short_code VARCHAR(50)]
        T3[title VARCHAR(200)]
        T4[destination_url VARCHAR(500)]
        T5[status VARCHAR(20)]
        T6[scan_count INTEGER]
        T7[created_at TIMESTAMP]
    end
    
    P1 --> T1
    P2 --> T2
    P3 --> T3
    P4 --> T4
    P5 --> T5
    P6 --> T6
    P7 --> T7
```

## Common SQLAlchemy Types

| Python Type | SQLAlchemy Type | PostgreSQL Type |
|-------------|----------------|-----------------|
| `int` | `Integer` | INTEGER |
| `str` | `String(50)` | VARCHAR(50) |
| `str` | `Text` | TEXT |
| `bool` | `Boolean` | BOOLEAN |
| `datetime` | `DateTime` | TIMESTAMP |
| `date` | `Date` | DATE |
| `float` | `Float` | FLOAT |
| `dict` | `JSON` | JSON |

## Model Examples

### Simple Models

```python
# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

# Analytics model
class ScanAnalytics(Base):
    __tablename__ = "scan_analytics"
    id = Column(Integer, primary_key=True)
    qr_code_id = Column(Integer, nullable=False)
    scanned_at = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45))
    user_agent = Column(String(200))
```

### Relationship Models

```python
# Models with relationships
class QRCode(Base):
    __tablename__ = "qr_codes"
    id = Column(Integer, primary_key=True)
    # ... existing fields ...
    
    # One-to-many relationship
    scans = relationship("ScanAnalytics", back_populates="qr_code")

class ScanAnalytics(Base):
    __tablename__ = "scan_analytics"
    id = Column(Integer, primary_key=True)
    qr_code_id = Column(Integer, ForeignKey("qr_codes.id"))
    
    # Many-to-one relationship
    qr_code = relationship("QRCode", back_populates="scans")
```

## Creating Tables

```python
# Create all tables
Base.metadata.create_all(engine)

# Create specific table
QRCode.__table__.create(engine, checkfirst=True)
```

---

## 🔍 Model Design Tips

1. **Choose meaningful field names** - Use business terms
2. **Add indexes** - For frequently queried fields
3. **Use constraints** - `nullable`, `unique`, `default`
4. **Include timestamps** - `created_at`, `updated_at`
5. **Document your models** - Use docstrings

---

# Section 7: CRUD Operations

## CRUD Flow Overview

```mermaid
graph TD
    subgraph "CRUD Operations"
        C[CREATE] -->|Add new record| DB[(Database)]
        R[READ] -->|Retrieve record| DB
        U[UPDATE] -->|Modify record| DB
        D[DELETE] -->|Remove record| DB
    end
```

## CREATE Operations

### Creating a QR Code

```python
from datetime import datetime

def create_qr_code(session, short_code, title, destination_url):
    # Create new QR code object
    new_qr = QRCode(
        short_code=short_code,
        title=title,
        destination_url=destination_url,
        status="active",
        scan_count=0,
        created_at=datetime.utcnow()
    )
    
    # Add to session and commit
    session.add(new_qr)
    session.commit()
    session.refresh(new_qr)  # Get generated ID
    
    return new_qr

# Usage
qr = create_qr_code(session, "SQ001", "Home Page", "https://example.com")
print(f"Created QR with ID: {qr.id}")
```

### Batch Create

```python
def create_multiple_qr_codes(session, qr_data_list):
    qr_codes = []
    for data in qr_data_list:
        qr = QRCode(**data)
        qr_codes.append(qr)
    
    session.add_all(qr_codes)
    session.commit()
    return qr_codes
```

## READ Operations

### Basic Reads

```python
# Get all QR codes
def get_all_qr_codes(session):
    return session.query(QRCode).all()

# Get by ID
def get_qr_by_id(session, qr_id):
    return session.get(QRCode, qr_id)

# Get by short_code
def get_qr_by_short_code(session, short_code):
    return session.query(QRCode).filter(
        QRCode.short_code == short_code
    ).first()
```

### Advanced Reads

```python
# Get active QR codes
def get_active_qr_codes(session):
    return session.query(QRCode).filter(
        QRCode.is_active == True
    ).all()

# Get recent QR codes
def get_recent_qr_codes(session, limit=10):
    return session.query(QRCode).order_by(
        QRCode.created_at.desc()
    ).limit(limit).all()
```

## UPDATE Operations

### Basic Update

```python
def update_destination_url(session, qr_id, new_url):
    # Get the QR code
    qr = session.get(QRCode, qr_id)
    if not qr:
        raise ValueError("QR Code not found")
    
    # Update fields
    qr.destination_url = new_url
    qr.updated_at = datetime.utcnow()
    
    # Save changes
    session.commit()
    return qr
```

### Increment Scan Count

```python
def increment_scan_count(session, qr_id):
    qr = session.get(QRCode, qr_id)
    if not qr:
        raise ValueError("QR Code not found")
    
    # Increment and commit
    qr.scan_count += 1
    session.commit()
    return qr
```

### Bulk Update

```python
def deactivate_old_qr_codes(session, days_old=30):
    cutoff_date = datetime.utcnow() - timedelta(days=days_old)
    
    # Update multiple records
    count = session.query(QRCode).filter(
        QRCode.created_at < cutoff_date,
        QRCode.is_active == True
    ).update({"is_active": False})
    
    session.commit()
    return count
```

## DELETE Operations

### Soft Delete (Recommended)

```python
def soft_delete_qr_code(session, qr_id):
    qr = session.get(QRCode, qr_id)
    if not qr:
        raise ValueError("QR Code not found")
    
    qr.is_active = False
    qr.status = "deleted"
    session.commit()
    return qr
```

### Hard Delete

```python
def hard_delete_qr_code(session, qr_id):
    qr = session.get(QRCode, qr_id)
    if not qr:
        raise ValueError("QR Code not found")
    
    session.delete(qr)
    session.commit()
    return True
```

## CRUD Operation Flow Diagram

```mermaid
sequenceDiagram
    participant A as Application
    participant S as Session
    participant DB as Database
    
    Note over A,S: CREATE
    A->>S: add object
    S->>DB: INSERT
    DB-->>S: OK
    S-->>A: Object with ID
    
    Note over A,S: READ
    A->>S: query()
    S->>DB: SELECT
    DB-->>S: Results
    S-->>A: Object(s)
    
    Note over A,S: UPDATE
    A->>S: modify object
    S->>DB: UPDATE
    DB-->>S: OK
    S-->>A: Updated object
    
    Note over A,S: DELETE
    A->>S: delete object
    S->>DB: DELETE
    DB-->>S: OK
    S-->>A: Deleted
```

---

## 📝 CRUD Summary

| Operation | Method | SQL Equivalent |
|-----------|--------|----------------|
| **CREATE** | `session.add(obj)` | `INSERT` |
| **READ** | `session.query(Model)` | `SELECT` |
| **UPDATE** | `modify obj` | `UPDATE` |
| **DELETE** | `session.delete(obj)` | `DELETE` |

---

# Section 8: Querying Data

## Query Building

```mermaid
graph TD
    Q[Query] --> F[Filter]
    F --> O[Order By]
    O --> L[Limit]
    L --> R[Result]
    
    R --> A[all - all results]
    R --> O1[one - exactly one]
    R --> F1[first - first result]
    R --> C[count - number of records]
    R --> E[exists - boolean]
```

## Basic Queries

### Getting Results

```python
# All results
qr_codes = session.query(QRCode).all()

# First result
qr_code = session.query(QRCode).first()

# Count records
count = session.query(QRCode).count()

# Check existence
exists = session.query(QRCode).filter(
    QRCode.short_code == "TEST"
).first() is not None
```

## Filtering

### Basic Filters

```python
# Equality
session.query(QRCode).filter(QRCode.status == "active")

# Inequality
session.query(QRCode).filter(QRCode.status != "inactive")

# Multiple conditions (AND)
session.query(QRCode).filter(
    QRCode.status == "active",
    QRCode.scan_count > 0
)

# OR conditions
from sqlalchemy import or_
session.query(QRCode).filter(
    or_(
        QRCode.status == "active",
        QRCode.status == "pending"
    )
)

# LIKE patterns
session.query(QRCode).filter(
    QRCode.title.like("%home%")
)

# IN clause
session.query(QRCode).filter(
    QRCode.status.in_(["active", "pending"])
)

# NOT IN clause
session.query(QRCode).filter(
    ~QRCode.status.in_(["deleted", "inactive"])
)
```

## Sorting

```python
# Ascending
session.query(QRCode).order_by(QRCode.created_at)

# Descending
session.query(QRCode).order_by(QRCode.created_at.desc())

# Multiple sorts
session.query(QRCode).order_by(
    QRCode.status,
    QRCode.scan_count.desc()
)
```

## Limiting Results

```python
# Limit and offset
session.query(QRCode).limit(10).offset(20)  # Pagination

# Top N results
top_scanned = session.query(QRCode).order_by(
    QRCode.scan_count.desc()
).limit(5).all()
```

## Complex Queries

### Combined Example

```python
def get_active_recent_qr_codes(session, limit=10):
    return session.query(QRCode).filter(
        QRCode.is_active == True
    ).order_by(
        QRCode.created_at.desc()
    ).limit(limit).all()

def search_qr_codes(session, search_term):
    return session.query(QRCode).filter(
        or_(
            QRCode.title.ilike(f"%{search_term}%"),
            QRCode.short_code.ilike(f"%{search_term}%")
        )
    ).all()
```

## Query Result Visual

```mermaid
graph LR
    subgraph "Database"
        T[Table: qr_codes] --> S[SELECT * FROM qr_codes WHERE status='active']
    end
    
    subgraph "Query Result"
        S --> R1[Row 1]
        S --> R2[Row 2]
        S --> R3[Row 3]
        R1 --> O1[QRCode Object 1]
        R2 --> O2[QRCode Object 2]
        R3 --> O3[QRCode Object 3]
    end
```

## Performance Tips

```python
# Use first() instead of all() when you only need one
qr = session.query(QRCode).filter_by(id=1).first()  # Good
qr = session.query(QRCode).filter_by(id=1)[0]  # Bad (loads all)

# Use count() for large datasets
total = session.query(QRCode).count()  # Good
total = len(session.query(QRCode).all())  # Bad (loads all)

# Use exists() for existence checks
exists = session.query(QRCode).filter_by(id=1).first() is not None
```

---

## 🎯 Query Best Practices

1. **Be specific** - Filter to only what you need
2. **Use indexes** - Put indexes on filtered columns
3. **Limit results** - Don't load large datasets
4. **Use appropriate methods** - `first()`, `count()`, `exists()`
5. **Order properly** - Use indexes for sorting

---

# Section 9: FastAPI Integration

## Architecture Overview

```mermaid
graph TD
    subgraph "FastAPI Application"
        A[API Endpoint] --> D[Database Dependency]
        D --> S[Session]
        A --> M[Model Operations]
    end
    
    subgraph "SQLAlchemy"
        M --> S
        S --> E[Engine]
    end
    
    subgraph "Database"
        E --> P[PostgreSQL]
    end
```

## Project Structure

```
sqanalytics/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py      # Engine & Session setup
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   └── routers/         # API routes
│       ├── __init__.py
│       └── qr_codes.py
├── .env                 # Environment variables
└── requirements.txt
```

## Database Setup

### database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
import os

# Load environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/sqanalytics"
)

# Create engine
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency to get database session
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Models

### models.py

```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class QRCode(Base):
    __tablename__ = "qr_codes"
    
    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(50), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    destination_url = Column(String(500), nullable=False)
    status = Column(String(20), default="active")
    scan_count = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default