# FastAPI Expense Tracker

A backend API for tracking personal expenses and budgets, built with **FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication**.  
Includes Docker support for easy setup and deployment.

---

## Features
- User authentication (JWT)
- CRUD for expenses
- Monthly spending summaries
- PostgreSQL database with Alembic migrations
- Swagger API docs

---

## Tech Stack
- Backend: FastAPI, SQLAlchemy, Alembic
- Auth: JWT (`python-jose`, `passlib`)
- Database: PostgreSQL (production), SQLite (local)
- Deployment: Docker + Render/Railway

---

## Installation (Local Dev)

```bash
git clone https://github.com/typicaleoxx/fastapi-expense-tracker.git
cd fastapi-expense-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
