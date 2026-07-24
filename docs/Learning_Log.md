# SQAnalytics Learning Log

This document records the major concepts, technologies, and engineering decisions learned throughout the development of SQAnalytics.

---

# Entry 001

## Topic

Git & GitHub

### What I Learned

- Git repository fundamentals
- Local and remote repositories
- Branching basics
- Commit workflow
- GitHub synchronization

### Outcome

Successfully established the project repository and version control workflow.

---

# Entry 002

## Topic

FastAPI

### What I Learned

- Project structure
- API routing
- Request and response models
- Dependency Injection
- Swagger UI
- OpenAPI documentation

### Outcome

Built the first REST API backend for SQAnalytics.

---

# Entry 003

## Topic

PostgreSQL & SQLAlchemy

### What I Learned

- SQLAlchemy ORM
- Database sessions
- Models
- CRUD operations
- Relationships
- PostgreSQL integration
- Supabase cloud database

### Outcome

Connected FastAPI to a production PostgreSQL database hosted on Supabase.

---

# Entry 004

## Topic

QR Code Generation

### What I Learned

- QR generation using qrcode
- Pillow image processing
- PNG generation
- Logo embedding
- Error correction levels
- Custom QR branding

### Outcome

Implemented automatic branded QR code generation.

---

# Entry 005

## Topic

QR Redirect Engine

### What I Learned

- HTTP redirects
- Dynamic route parameters
- Redirect responses
- QR lookup workflow
- Permanent redirect architecture

### Outcome

Implemented the QR redirect engine for production use.

---

# Entry 006

## Topic

Analytics Event Logging

### What I Learned

- Scan event tracking
- Browser detection
- Operating System detection
- Device type detection
- User-Agent parsing
- Analytics database design

### Outcome

Implemented automatic scan analytics recording for every QR interaction.

---

# Entry 007

## Topic

Production Deployment

### What I Learned

- Render deployment
- Supabase cloud database
- Cloudflare DNS
- Custom domains
- HTTPS
- Environment variables

### Outcome

Successfully deployed the backend into a production environment.

---

# Entry 008

## Topic

Human-Friendly QR URLs

### What I Learned

- URL slug normalization
- SEO-friendly URLs
- Backward compatibility
- Clean URL design
- Redirect URL generation
- Database schema evolution

### Outcome

Implemented descriptive QR URLs while maintaining compatibility with all previously generated QR codes.

Example

```
Old

https://love-bar.kndb.stream/r/19fba1ff
```

```
New

https://love-bar.kndb.stream/r/19fba1ff-where-words-meet-music
```

Both URL formats remain fully supported.

---

# Entry 009

## Topic

Database Design Evolution

### What I Learned

- Schema versioning
- Incremental database migrations
- PostgreSQL default values
- Automatic timestamps
- Production database maintenance

### Outcome

The database now evolves through versioned migration scripts while PostgreSQL automatically manages record timestamps.

---

# Current Learning Stage

Current Stable Release

**SQAnalytics Backend v1.2.0**

Current Focus

- Production hardening
- Backend refinement
- Code quality improvements

Next Learning Goals

- GeoIP integration
- Visitor session tracking
- Returning visitor analytics
- Next.js frontend development
- Authentication
- Dashboard development