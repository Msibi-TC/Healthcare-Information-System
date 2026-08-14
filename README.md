# Healthcare Information System

## Project overview

This repository contains the early backend foundation for a proposed multi-hospital healthcare information system. The requirements describe patient care, clinical workflows, hospital administration, and reporting for healthcare facilities, with South African privacy and operational needs in mind.

The files in `Documentation/` describe intended requirements and designs. They do not prove that a feature has been implemented; the source code is the implementation record.

## Current development status

The project is in the initial backend scaffolding and data-model stage. It is not yet a runnable application and has no complete end-to-end workflow.

- **Implemented:** baseline settings, synchronous SQLAlchemy engine/session setup, password hashing and verification helpers, JWT access-token creation, a user-role enumeration, and partial SQLAlchemy models.
- **Partially implemented:** user, patient, hospital, and department persistence definitions. These models still contain unresolved naming, relationship, and foreign-key problems.
- **Planned only:** the API, complete authentication and authorization, remaining domain models, migrations, frontend, reporting, notifications, deployment configuration, and the other workflows described in the design documents.

## Technology stack

Confirmed by the current backend code and dependency file:

- Python
- FastAPI and Uvicorn dependencies (no FastAPI application instance yet)
- SQLAlchemy with PostgreSQL through psycopg 3
- Pydantic and pydantic-settings
- python-jose for JWT creation
- Passlib and bcrypt for password hashing
- Alembic dependency (not configured)
- pytest, pytest-asyncio, and HTTPX dependencies (no tests yet)
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
│       ├── models/         # Partial SQLAlchemy models and placeholders
│       ├── schemas/        # Currently empty schema placeholders
│       ├── __init__.py     # Currently contains unresolved model imports
│       └── main.py         # Empty; no FastAPI application exists yet
└── Documentation/
    ├── PROJECT_STATUS_REPORT.txt
    ├── phase1_proposal.txt
    ├── Technical docs.txt
    └── DEVELOPMENT_PROGRESS.md
```

There is currently no `frontend/`, API route package, CRUD layer, Alembic setup, test suite, Docker configuration, or seed data.

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

The conventional future launch command is expected to be:

```bash
uvicorn app.main:app --reload
```

That command does **not** work yet because `backend/app/main.py` has no FastAPI `app` object and package/model imports remain incomplete. This baseline task intentionally does not implement the application.

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
- `backend/app/models/user.py`: partial user model and role enumeration.
- `backend/app/models/patient.py`: partial patient model.
- `backend/app/models/hospitals.py`: partial hospital model.
- `backend/app/models/departments.py`: partial department model.

These components are foundational and do not constitute a working application.

## Current limitations

- `backend/app/main.py` is empty; there is no FastAPI application or endpoint.
- `backend/app/__init__.py` imports missing or differently named modules/classes.
- Several model relationship targets do not exist.
- Existing models contain table-name, relationship-name, and foreign-key inconsistencies.
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

The recommended next implementation task is a minimal bootable FastAPI application and health endpoint while carefully isolating or correcting unresolved model imports. Authentication and domain APIs should follow in separately reviewed tasks.
