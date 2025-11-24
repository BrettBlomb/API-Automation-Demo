# API Automation Demo

![Tests](https://github.com/BrettBlomb/API-Automation-Demo/actions/workflows/python-tests.yml/badge.svg)

API test automation framework using Python, Pytest, and GitHub Actions CI.

## 🚀 What This Project Demonstrates
- Automated API validation using Python & Requests
- Positive, negative, and data-driven testing
- JSON Schema validation (contract testing)
- CI/CD pipeline executing tests on every push
- Professional test structure with `tests/` and `utils/`

## 🧪 Test Coverage
- GET /users?page=2 — Verify status, schema & data structure
- GET /users/{id} — Param tests for multiple user IDs
- POST /users — Validate new user creation response
- Error handling for not found responses

## 🛠 Tools & Libraries
- Python
- Pytest
- Requests
- JSONSchema
- GitHub Actions

## ▶️ Running Tests
```bash
pip install -r requirements.txt
pytest -v
