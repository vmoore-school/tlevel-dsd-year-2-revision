# Container image for the starter project (lesson 06.08).
# Build:  docker build -t rcsc-starter .      (or: podman build ...)
# Run:    docker run -p 8000:8000 rcsc-starter   then open http://localhost:8000
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn==23.0.0

COPY backend/ backend/
COPY frontend/ frontend/
COPY database/schema.sql database/seed.sql database/

ENV DATABASE_PATH=/app/database/club.db
EXPOSE 8000

# Port binding and stateless processes (12-factor). gunicorn is a production WSGI server.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.app:app"]
