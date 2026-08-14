# Healthcare Information System

## Project overview

This repository contains the early backend foundation for a proposed multi-hospital healthcare information system. The requirements describe patient care, clinical workflows, hospital administration, and reporting for healthcare facilities, with South African privacy and operational needs in mind.

The files in `Documentation/` describe intended requirements and designs. They do not prove that a feature has been implemented; the source code is the implementation record.

## Current development status

The project is in the initial backend scaffolding and data-model stage. A minimal FastAPI process can now start and expose a health endpoint, but there is no complete domain workflow.

- **Implemented:** a minimal FastAPI application, CORS middleware, `GET /health`, a focused health smoke test, baseline settings, synchronous SQLAlchemy engine/session setup, password hashing and verification helpers, JWT access-token creation, a user-role enumeration, and partial SQLAlchemy models.
- **Partially implemented:** stabilized metadata mappings for users, patients, hospitals, and departments. Database migrations and persistence workflows do not yet exist.
- **Planned only:** the API, complete authentication and authorization, remaining domain models, migrations, frontend, reporting, notifications, deployment configuration, and the other workflows described in the design documents.

## Technology stack

Confirmed by the current backend code and dependency file:

- Python
- FastAPI application and Uvicorn server
- SQLAlchemy with PostgreSQL through psycopg 3
- Pydantic and pydantic-settings
- python-jose for JWT creation
- Passlib and bcrypt for password hashing
- Alembic dependency (not configured)
- pytest, pytest-asyncio, and HTTPX with focused health and ORM metadata tests
- Black, Flake8, and mypy development dependencies

Dependencies are currently unpinned, so the repository does not establish exact installed versions. React, TypeScript, Tailwind CSS, and related frontend tools are planned but not present.

## Project structure

```text
.
├── backend/
│   ├── .env.example        # Safe environment-variable template
│   ├── requirements.txt    # Python dependencies
│   └── app/
│       ├── core/           # Settings, database session, security helpers
│       ├── models/         # Four registered ORM models and placeholders
│       ├── schemas/        # Currently empty schema placeholders
│       ├── __init__.py     # Side-effect-free package boundary
│       └── main.py         # Minimal FastAPI app and health endpoint
│   └── tests/
│       ├── test_health.py  # Focused application smoke test
│       └── test_models.py  # ORM metadata and relationship tests
└── Documentation/
    ├── PROJECT_STATUS_REPORT.txt
    ├── phase1_proposal.txt
    ├── Technical docs.txt
    └── DEVELOPMENT_PROGRESS.md
```

There is currently no `frontend/`, API route package, CRUD layer, Alembic setup, broad domain test suite, Docker configuration, or seed data.

## Prerequisites

The intended backend baseline requires:

- Python 3.9 or newer, as specified by the design documents
- PostgreSQL (the design proposes PostgreSQL 14 or newer)
- Python virtual-environment support
- `pip`

Exact runtime versions have not yet been locked or verified by automated tests.

## Backend setup

From the repository root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

Then edit `backend/.env` for the local PostgreSQL instance and replace every placeholder value.

After configuring `backend/.env`, start the development server from the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The startup command and `GET http://127.0.0.1:8000/health` have been validated locally. The health endpoint confirms only that the FastAPI process is running; it does not check PostgreSQL or any other external service.

Run the focused smoke test from `backend` with:

```bash
python -m pytest
```

## Environment configuration

Copy `backend/.env.example` to `backend/.env`. The settings module loads that file relative to the backend directory, independent of the shell's current directory.

Required security configuration:

- `SECRET_KEY`: a unique, high-entropy value of at least 32 characters; the application configuration has no secret default.

Database configuration:

- `POSTGRES_SERVER`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `POSTGRES_PORT`

Other available settings cover the API prefix, project/version labels, token lifetimes, CORS origins, optional future superuser bootstrap values, and optional future SMTP integration. Initial-superuser and email workflows are not implemented.

Never commit `backend/.env`. The example file contains placeholders only and remains tracked.

## Currently implemented components

- `backend/app/core/config.py`: environment-backed settings and PostgreSQL URL construction.
- `backend/app/core/database.py`: synchronous engine, session factory, declarative base, and `get_db()` generator.
- `backend/app/core/security.py`: access-token creation and password hash/check helpers.
- `backend/app/main.py`: FastAPI application, configured CORS middleware, versioned documentation URLs, and process-only health endpoint.
- `backend/tests/test_health.py`: focused health endpoint smoke test.
- `backend/app/models/user.py`: user model and role enumeration.
- `backend/app/models/patient.py`: patient model with a one-to-one user relationship.
- `backend/app/models/hospital.py`: hospital model with departments.
- `backend/app/models/department.py`: department model associated with a hospital.
- `backend/app/models/__init__.py`: deliberate registration boundary for implemented models only.

These components are foundational and do not constitute a working application.

## Current limitations

- The only implemented HTTP endpoint is `GET /health`; no domain API exists.
- `backend/app/__init__.py` deliberately does not import domain models because that layer is incomplete.
- Relationships to planned models are deferred until those models are implemented.
- `Department.head_doctor_id` is intentionally not a foreign key until the planned `Doctor` model exists.
- Pydantic schema files are empty.
- There is no authentication/login workflow or authorization enforcement.
- There are no migrations, tests, frontend, containers, or deployment instructions.
- No database creation or seed process exists.
- Dependency versions are not pinned.

See `Documentation/PROJECT_STATUS_REPORT.txt` for the original detailed repository audit. That report remains a historical baseline and is not updated to imply later progress.

## Planned architecture and features

The design documents propose a React/TypeScript frontend communicating with a FastAPI REST API backed by PostgreSQL through SQLAlchemy. Proposed modules include:

- Authentication and role-based access
- Patient and doctor profiles
- Medical conditions and specializations
- Appointment scheduling
- Consultations and prescriptions
- Surgery scheduling, consent, teams, and reports
- Medical records
- Multi-hospital and department administration
- Reporting, notifications, billing, and later enterprise capabilities

All items above remain planned unless explicitly listed as implemented or partial in this README.

## Development workflow

1. Work on the `development` branch unless the team specifies otherwise.
2. Review `Documentation/PROJECT_STATUS_REPORT.txt`, the requirements, and the technical design before changing scope.
3. Create a focused change without treating planned documents as implementation evidence.
4. Run non-destructive validation appropriate to the changed code.
5. Append task results and remaining issues to `Documentation/DEVELOPMENT_PROGRESS.md`.
6. Review working-tree changes before committing; commits and pushes are performed only when explicitly requested.

The recommended next task is a separately scoped persistence step, such as adding the next explicitly approved model set or establishing migrations for the stabilized models. Authentication and domain APIs should follow in separately reviewed tasks.
