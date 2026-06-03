# LinkedIn Profile ETL Pipeline

## Overview

This project extracts LinkedIn profile information using Apify, stores the raw response for auditing and debugging, transforms the data, and loads structured profile information into a destination table in Neon PostgreSQL.

The ETL pipeline follows the pattern:

```text
Source Table
    ↓
Read LinkedIn URL
    ↓
Apify LinkedIn Scraper
    ↓
Raw JSON Response
    ↓
Extracted Data Table
    ↓
Transformation Layer
    ↓
Destination Table
```

---

## Features

* LinkedIn profile scraping using Apify
* Raw JSON storage for auditing
* ETL architecture (Extract, Transform, Load)
* PostgreSQL (NeonDB) integration
* SQLAlchemy ORM
* Environment-based configuration
* Structured destination table
* Skills extraction
* Certifications extraction
* First Name and Last Name extraction
* Headline extraction
* About section extraction

---

## Technology Stack

| Component       | Technology      |
| --------------- | --------------- |
| Language        | Python 3.11+    |
| Database        | Neon PostgreSQL |
| ORM             | SQLAlchemy      |
| Scraper         | Apify           |
| Configuration   | Python Dotenv   |
| Version Control | Git             |

---

## Project Structure

```text
linkedin_etl/

├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── config.py
├── db.py
├── models.py.py
├── apify_client_service.py
├── extractor.py
├── elt
├── test.py

```

---

## Database Schema

### Source Table

Stores LinkedIn profile URLs waiting to be processed.

```sql
CREATE TABLE source (
    id SERIAL PRIMARY KEY,
    linkedin_url TEXT,
    status VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

### Extracted Data Table

Stores raw API responses and extracted information.

```sql
CREATE TABLE extracted_data (
    id SERIAL PRIMARY KEY,
    source_id INTEGER,
    linkedin_id TEXT,
    raw_response JSONB,
    first_name TEXT,
    last_name TEXT,
    headline TEXT,
    about TEXT,
    skills JSONB,
    certifications JSONB,
    status VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

### Destination Table

Stores cleaned profile information.

```sql
CREATE TABLE destination (
    id SERIAL PRIMARY KEY,
    linkedin_id TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT,
    headline TEXT,
    about TEXT,
    skills TEXT,
    certifications TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/linkedin-etl.git
cd linkedin-etl
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
APIFY_TOKEN=your_apify_token

DATABASE_URL=postgresql://user:password@host/database?sslmode=require
```

---

## Configure Apify

This project uses:

Actor:

```text
harvestapi/linkedin-profile-scraper
```

Input Example:

```json
{
  "profileScraperMode": "Profile details no email ($4 per 1k)",
  "queries": [
    "https://www.linkedin.com/in/example"
  ]
}
```

---

## Add Source URLs

```sql
INSERT INTO source(linkedin_url,status)
VALUES
('https://www.linkedin.com/in/example','PENDING');
```

---

## Test Scraper

```bash
python test.py
```

Expected output:

```text
Scraping LinkedIn Profile...
Records Found: 1
```

---

## Run ETL Pipeline

```bash
python etl.py
```

Pipeline Steps:

1. Read pending LinkedIn URLs
2. Call Apify Actor
3. Store raw response
4. Extract required fields
5. Load transformed data into destination table
6. Update source status

---

## Extracted Fields

| Field          | Description                |
| -------------- | -------------------------- |
| linkedin_id    | LinkedIn Public Identifier |
| first_name     | First Name                 |
| last_name      | Last Name                  |
| headline       | Profile Headline           |
| about          | About Section              |
| skills         | Skills List                |
| certifications | Certifications List        |

---

## Git Workflow

Initial Commit:

```bash
git add .
git commit -m "Initial project setup"
```

Database Models:

```bash
git commit -m "Add SQLAlchemy models"
```

Apify Integration:

```bash
git commit -m "Integrate HarvestAPI LinkedIn scraper"
```

Extraction Logic:

```bash
git commit -m "Add LinkedIn profile extraction logic"
```

ETL Pipeline:

```bash
git commit -m "Implement ETL pipeline"
```

Production Refactor:

```bash
git commit -m "Refactor project structure for production"
```

Final Release:

```bash
git commit -m "feat: build LinkedIn ETL pipeline using Apify and NeonDB"
```

---

## Future Enhancements

* Experience Extraction
* Education Extraction
* Company Information
* Location Information
* Profile Images
* Followers Count
* Scheduled ETL Runs
* Airflow Integration
* Docker Deployment
* FastAPI Service Layer

---

## Author

Balaji

LinkedIn ETL Project using Python, Apify, SQLAlchemy, and Neon PostgreSQL.
