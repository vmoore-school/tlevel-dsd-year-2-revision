"""Riverside Community Sports Club: starter JSON API (Flask) that also serves the front end.

Run:  flask --app backend.app run --debug     (from the starter-code folder)
"""
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from backend.bookings import BookingError, create_booking, parse_id, spaces_left
from backend.db import close_db, database_path, get_db, init_db

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


def session_to_dict(row):
    return {
        "session_id": row["session_id"],
        "name": row["name"],
        "sport": row["sport"],
        "start": row["start_time"],
        "duration_minutes": row["duration_minutes"],
        "capacity": row["capacity"],
        "booked": row["booked"],
        "spaces_left": spaces_left(row["capacity"], row["booked"]),
        "price_gbp": row["price_pence"] / 100,
        "coach": row["coach_name"],
    }


SESSION_QUERY = """
    SELECT s.*, c.name AS coach_name,
           (SELECT COUNT(*) FROM booking b WHERE b.session_id = s.session_id) AS booked
    FROM session s JOIN coach c ON c.coach_id = s.coach_id
"""


def create_app(config=None):
    app = Flask(__name__, static_folder=None)
    app.config["DATABASE"] = database_path()
    if config:
        app.config.update(config)
    if not Path(app.config["DATABASE"]).exists():
        init_db(app.config["DATABASE"])
    app.teardown_appcontext(close_db)

    @app.errorhandler(BookingError)
    def handle_booking_error(error):
        return jsonify(error=error.message), error.status

    @app.get("/api/sessions")
    def list_sessions():
        rows = get_db().execute(SESSION_QUERY + " ORDER BY s.start_time").fetchall()
        return jsonify(sessions=[session_to_dict(r) for r in rows])

    @app.get("/api/sessions/<session_id>")
    def get_session(session_id):
        row = get_db().execute(
            SESSION_QUERY + " WHERE s.session_id = ?", (parse_id(session_id, "session_id"),)
        ).fetchone()
        if row is None:
            return jsonify(error="Session not found"), 404
        return jsonify(session_to_dict(row))

    @app.post("/api/bookings")
    def post_booking():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify(error="Request body must be JSON"), 400
        booking_id = create_booking(get_db(), data.get("member_id"), data.get("session_id"))
        return jsonify(booking_id=booking_id), 201

    @app.delete("/api/bookings/<booking_id>")
    def delete_booking(booking_id):
        db = get_db()
        cursor = db.execute("DELETE FROM booking WHERE booking_id = ?", (parse_id(booking_id, "booking_id"),))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify(error="Booking not found"), 404
        return "", 204

    @app.get("/api/stats")
    def stats():
        rows = get_db().execute(
            "SELECT s.sport, COUNT(b.booking_id) AS bookings "
            "FROM session s LEFT JOIN booking b ON b.session_id = s.session_id "
            "GROUP BY s.sport ORDER BY bookings DESC"
        ).fetchall()
        return jsonify(bookings_by_sport=[dict(r) for r in rows])

    @app.get("/")
    def index():
        return send_from_directory(FRONTEND_DIR, "index.html")

    @app.get("/<path:filename>")
    def frontend_files(filename):
        return send_from_directory(FRONTEND_DIR, filename)

    return app


app = create_app()
