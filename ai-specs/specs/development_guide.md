# Development Guide

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL (or Docker)

## Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"
```

### Environment Configuration

Create `backend/.env`:

```env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/app
FRONTEND_URL=http://localhost:3000
```

### Database Migrations

```bash
cd backend
alembic upgrade head
```

### Running the Backend

```bash
cd backend
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov

# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/
```

## Frontend Setup

```bash
cd frontend
npm install
```

### Running the Frontend

```bash
cd frontend
npm run dev
```

### Frontend Tests

```bash
cd frontend

# Run unit tests
npm test

# Run E2E tests (headless)
npm run cypress:run

# Open Cypress Test Runner
npm run cypress:open
```

## Project Structure

```
backend/
  src/
    domain/           # Entities, repository interfaces, exceptions
    application/      # Use cases (Clean Architecture)
    infrastructure/   # Database models, repository implementations, config
    presentation/     # FastAPI routers, Pydantic schemas, middleware
  tests/
    unit/             # Unit tests (entities, use cases)
    integration/      # Integration tests (API, repository)
  alembic/            # Database migrations

frontend/
  src/
    app/              # Redux store, hooks
    components/       # Shared components (Sidebar, AppLayout)
    features/         # Feature modules (companies/)
    pages/            # Route pages (CompaniesPage, DashboardPage)
    types/            # TypeScript type definitions
  cypress/
    e2e/              # End-to-end tests
```

## Tech Stack

### Backend
- **Framework:** FastAPI
- **ORM:** SQLAlchemy 2.0 (async)
- **Database:** PostgreSQL (asyncpg driver)
- **Migrations:** Alembic
- **Validation:** Pydantic v2
- **Testing:** pytest, pytest-asyncio, httpx
- **Linting:** ruff, mypy (strict)

### Frontend
- **Framework:** React 18 + TypeScript
- **Build Tool:** Vite
- **State Management:** Redux Toolkit (RTK Query)
- **UI Library:** React Bootstrap 2 + Bootstrap 5
- **Routing:** React Router v6
- **Testing:** Vitest + Testing Library
- **E2E Testing:** Cypress
