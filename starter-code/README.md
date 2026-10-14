# Starter Project: Riverside Community Sports Club booking system

A small, working **full-stack** example in three languages, based on
[mock brief 01](../mock-briefs/brief-01-community-sports-club.md):

| Layer | Language / tech | Folder |
|---|---|---|
| Front end | HTML, CSS, **JavaScript** (no framework) | `frontend/` |
| Back end | **Python** 3.10+ with Flask (JSON API) | `backend/` |
| Database | **SQL** (SQLite) | `database/` |
| Tests | pytest (unit and integration) | `tests/` |
| DevOps | Dockerfile, GitHub Actions CI, `.env.example` | root, `.github/` |

It's deliberately small, so it is a **teaching aid, not an OSP answer**. In the real OSP you design and
build your own solution from the Pearson brief.

## Run it

```bash
cd starter-code
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app backend.app run --debug
```

Open <http://127.0.0.1:5000>. The SQLite database is created from `database/schema.sql` and `seed.sql`
the first time you run it. Delete `database/club.db` to reset it.

## Test it

```bash
python -m pytest -v
```

## API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/sessions` | All sessions, with spaces left |
| GET | `/api/sessions/<id>` | One session |
| POST | `/api/bookings` | Body `{"member_id": 1, "session_id": 3}` → `201` with `booking_id`, or `400`/`404`/`409` with an error |
| DELETE | `/api/bookings/<id>` | Cancel a booking → `204` |
| GET | `/api/stats` | Bookings per sport (for a dashboard) |

## Extension tasks (map to lessons)

- [ ] 06.02 Add a "My bookings" page with a cancel button
- [ ] 06.03 Add login with hashed passwords and a session cookie; add coach and manager roles
- [ ] 06.04 Add a `waiting_list` table and promote people automatically when someone cancels
- [ ] 06.10 Build a dashboard page with Chart.js using `/api/stats` and `sample-data/sales-data.csv`
- [ ] 06.07 Audit against the 12 factors (see the lesson resource)
- [ ] 06.08 Build and run it in Docker; push to GitHub and get CI passing
- [ ] 07.02 Run Lighthouse and fix the accessibility and performance issues
- [ ] 07.03 Run `bandit` and `pip-audit` and triage the results
- [ ] 08.04 Write an OpenAPI (Swagger) contract for the API
