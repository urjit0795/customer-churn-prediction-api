# Customer Churn Prediction API

A lightweight REST API built using FastAPI and Pydantic to demonstrate backend engineering, input validation, and automated testing for ML inference services.

## Overview

This project demonstrates how a Python-based prediction service can be exposed through a REST API for integration with external applications.

The current implementation uses a simple rule-based predictor as a placeholder for a trained machine learning model.

## Tech Stack

- Python 3.13
- FastAPI
- Pydantic
- Pytest
- HTTPX

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks API availability |
| POST | `/predict` | Returns customer churn risk |

## Prediction Logic

- Customer tenure below 12 months → High risk
- Customer tenure of 12 months or more → Low risk

## Input Validation

Pydantic validates incoming requests and enforces the following constraints:

- Customer ID must be positive.
- Tenure cannot be negative.
- Monthly spending cannot be negative.
- All required fields must be present.

## Getting Started

Clone the repository and install dependencies:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

Access the interactive API documentation at:

`http://127.0.0.1:8000/docs`

## Example Request

```json
{
  "customer_id": 101,
  "tenure_months": 6,
  "monthly_spend": 80
}
```

## Example Response

```json
{
  "customer_id": 101,
  "risk_level": "high"
}
```

## Automated Testing

Run all tests:

```bash
python -m pytest -v
```

The test suite covers health checks, high- and low-risk predictions, negative tenure, and missing required fields.

## Future Improvements

- Integrate a trained ML model.
- Add structured logging and exception handling.
- Implement API authentication.
- Containerize the application using Docker.
- Deploy the service to AWS.
- Introduce monitoring and model performance evaluation.

## Purpose

This project is part of a hands-on Forward Deployed Engineering learning roadmap focused on building reliable, customer-facing AI applications.