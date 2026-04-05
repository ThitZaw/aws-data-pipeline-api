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

FastAPI → API Gateway → Lambda → S3 → Athena → Dashboard 
                         ↓  
                    PostgreSQL

---

## Tech Stack

- Backend: FastAPI (Python)
- Cloud: AWS (S3, Lambda, API Gateway, IAM , ECR , Cloudwatch)
- Database: PostgreSQL
- Version Control: Git
- Containerization : Docker

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
- Connected local backend to containerized database

### Step 3 — AWS S3 Integration (Raw Data Storage) ✅

**upload raw file to S3**
- Created an S3 bucket for data storage
- Integrated FastAPI with AWS S3 using boto3
- Uploaded raw CSV files to S3 (`raw/` folder)
- Stored S3 file path (`s3_path`) in PostgreSQL
- Updated database schema to include S3 reference

**Tech Used:**
- AWS S3
- boto3 (AWS SDK for Python)
- FastAPI
- PostgreSQL

**Workflow:**
1. User uploads file via API  
2. File is saved locally (temporary)  
3. File is uploaded to S3 (`raw/` bucket path)  
4. S3 file path is stored in PostgreSQL  
FastAPI (/upload) → Save file (temporary) → Upload to S3 (raw/) → Store S3 path in PostgreSQL

## Step 4 — Data Transformation (CSV → Parquet) ✅

**Convert raw data into analytics-ready format**

- Implemented transformation logic using pandas
- Read CSV files directly from S3
- Cleaned and standardized column names
- Converted CSV → Parquet format
- Stored processed data in S3 (`processed/` folder)

**Tech Used:**
- pandas  
- pyarrow  
- boto3  

**Workflow:**
S3 (raw CSV) → Lambda → Transform → S3 (processed Parquet)

---

## Step 5 — Serverless Processing with AWS Lambda (Docker + ECR) ✅

**Automated and scalable data processing pipeline**

- Containerized transformation logic using Docker
- Built and pushed Docker image to Amazon ECR
- Deployed AWS Lambda using container image from ECR
- Configured Lambda handler to process S3 events
- Integrated Lambda with S3 trigger (PUT event)
- Automatically processes files uploaded to `raw/`

**Tech Used:**
- AWS Lambda  
- Docker  
- Amazon Elastic Container Registry (ECR)  

**Workflow:**
FastAPI → Upload CSV → S3 (raw/) → Lambda (Docker via ECR) → Process → S3 (processed/)