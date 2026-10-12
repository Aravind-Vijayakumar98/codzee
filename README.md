# TaskFlow API

A small Django REST Framework project for a coding-assessment workflow. It exposes CRUD endpoints for tasks, validates task data, and includes automated tests.

## Requirements
- Python 3.10+
- Git

## Run locally (Linux/macOS)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Windows activation: `.venv\Scripts\activate`

API root: `http://127.0.0.1:8000/api/tasks/`

## Endpoints
- `GET /api/tasks/` — list tasks
- `POST /api/tasks/` — create a task
- `GET /api/tasks/<id>/` — retrieve one task
- `PATCH /api/tasks/<id>/` — update a task
- `DELETE /api/tasks/<id>/` — delete a task
- `GET /api/health/` — health check
- `GET /api/docs/` — browsable API root (DRF)

Example POST:
```json
{
  "title": "Prepare Codzee assessment",
  "description": "Create three meaningful pull requests",
  "status": "todo",
  "priority": "medium"
}
```

Allowed status values: `todo`, `in_progress`, `done`.
Allowed priority values: `low`, `medium`, `high`.

## Run tests
```bash
python manage.py test
```

## Deploy
The repository includes a `render.yaml` Blueprint configuration. Push this project to a public GitHub repository, then in Render choose **New + > Blueprint** and select the repository. Review the database/service plan and current pricing/availability before creating resources. After deployment, test `/api/health/` and `/api/tasks/`.

## Suggested Codzee PRs
1. **PR 1 — Validation and regression tests:** improve validation for whitespace-only titles and add tests.
2. **PR 2 — API behavior:** add filtering by status and tests, or improve error responses.
3. **PR 3 — Performance/quality:** add pagination and tests, or add query-count/performance coverage.

Create a separate branch for each PR, push it, and open the PR against `main`. Review Codzee's actual comments and record accurate examples; do not fabricate findings.

## Before making the repository public
Do not commit `.env`, secrets, real personal data, or database files. This starter contains no production credentials.
