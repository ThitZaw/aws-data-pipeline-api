# aws-data-pipeline-api
AWS Data Pipeline API

## Description

A serverless data ingestion and processing pipeline built with FastAPI, AWS S3, Lambda, and PostgreSQL.

This project demonstrates how to design and implement a scalable backend system using AWS cloud services and modern Python frameworks.

---

## Why This Project?

This project was built to demonstrate hands-on experience with AWS cloud services, backend API development, and data pipeline design in preparation for backend and data engineering roles.

---

## Architecture

FastAPI → API Gateway → Lambda → S3  
                         ↓  
                    PostgreSQL

---

## Tech Stack

- Backend: FastAPI (Python)
- Cloud: AWS (S3, Lambda, API Gateway, IAM)
- Database: PostgreSQL
- Version Control: Git
- (Optional) Docker

---

## Features

- Upload data via API
- Store raw files in AWS S3
- Process data using AWS Lambda
- Store structured data in PostgreSQL
- RESTful API built with FastAPI

---

### Step 1 — FastAPI Basic Setup ✅
**Adding Fast API:**
- Set up FastAPI project structure
- Created `/upload` and `/data` endpoints
- Implemented file upload handling
- Tested API using Swagger UI

**Tech Used:**
- FastAPI
- Uvicorn

### Step 2 — PostgreSQL with Docker ✅

**connecting fastapi with postgre:**
- Set up PostgreSQL using Docker
- Connected FastAPI (local) to PostgreSQL container
- Created database model for file records
- Stored uploaded file metadata in database

**Tech Used:**
- PostgreSQL
- Docker
- SQLAlchemy

**Notes:**
- Learned how to run databases in containers
- Connected local backend to containerized database