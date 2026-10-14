"""Database helpers. Config comes from the environment (12-factor: store config in the environment)."""
import os
import sqlite3
from pathlib import Path

from flask import current_app, g

DATABASE_DIR = Path(__file__).resolve().parent.parent / "database"


def get_db():
    """Return one connection per request, with rows that behave like dicts."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(path, with_seed=True):
    """Create the tables (and optionally the sample data) in the database at `path`."""
    conn = sqlite3.connect(path)
    conn.executescript((DATABASE_DIR / "schema.sql").read_text())
    if with_seed:
        conn.executescript((DATABASE_DIR / "seed.sql").read_text())
    conn.commit()
    conn.close()


def database_path():
    return os.environ.get("DATABASE_PATH", str(DATABASE_DIR / "club.db"))
