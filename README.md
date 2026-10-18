# DevOps Utilities API

A Python-based REST API built with FastAPI to expose system metrics and retrieve AWS S3 bucket information.

## Features

- **System Metrics:** Retrieves CPU, memory, and disk usage.
- **AWS S3 Integration:** Lists S3 buckets accessible to the configured AWS identity.
- **REST API:** Provides HTTP endpoints through FastAPI.
- **Interactive API Documentation:** FastAPI generates Swagger UI automatically.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Boto3
- psutil
- AWS S3

## Project Structure

```text
devops_util/
├── FastAPIproj.py
├── fourthsept.py
└── requirements.txt
```

## Prerequisites

- Python 3
- An AWS account and configured credentials for the S3 endpoint
- AWS permissions to list the buckets you want to access

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials using the AWS CLI or another supported Boto3 credential provider. Avoid hardcoding credentials in the source code.

## Run the API

Start the development server:

```bash
uvicorn FastAPIproj:app --reload
```

The API will usually be available at:

`http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/hello` | Returns a welcome message |
| GET | `/metrics` | Returns CPU, memory, and disk usage |
| GET | `/aws/s3` | Lists accessible S3 buckets |

## Interactive Documentation

With the server running, visit:

`http://127.0.0.1:8000/docs`

FastAPI provides an interactive Swagger UI for exploring and testing the endpoints.

## Notes

This project was built as a learning exercise to explore Python, REST APIs, Linux system metrics, and AWS integration.
