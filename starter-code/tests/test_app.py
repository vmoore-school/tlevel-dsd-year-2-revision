"""Automated tests for the starter API. Run with:  python -m pytest"""
import pytest

from backend.app import create_app
from backend.bookings import BookingError, parse_id, spaces_left
from backend.db import init_db


@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test.db"
    init_db(db_path)
    app = create_app({"DATABASE": str(db_path), "TESTING": True})
    return app.test_client()


# ---------- Unit tests: business rules ----------

@pytest.mark.parametrize("value, expected", [(1, 1), ("7", 7), (" 12 ", 12)])
def test_parse_id_valid(value, expected):
    assert parse_id(value, "id") == expected


@pytest.mark.parametrize("value", [0, -1, "abc", "", None, 2.5, "3.0", True])
def test_parse_id_invalid(value):
    with pytest.raises(BookingError):
        parse_id(value, "id")


@pytest.mark.parametrize("capacity, booked, expected", [(20, 0, 20), (20, 19, 1), (20, 20, 0), (20, 25, 0)])
def test_spaces_left(capacity, booked, expected):
    assert spaces_left(capacity, booked) == expected


# ---------- Integration tests: API + database ----------

def test_list_sessions(client):
    response = client.get("/api/sessions")
    assert response.status_code == 200
    sessions = response.get_json()["sessions"]
    assert len(sessions) == 4
    assert {"session_id", "name", "spaces_left", "price_gbp"} <= sessions[0].keys()


def test_get_unknown_session_returns_404(client):
    assert client.get("/api/sessions/999").status_code == 404


def test_create_booking_valid(client):
    response = client.post("/api/bookings", json={"member_id": 1, "session_id": 3})
    assert response.status_code == 201
    assert "booking_id" in response.get_json()


def test_create_booking_full_session(client):
    # Seed data: session 2 has capacity 2 and 2 bookings
    response = client.post("/api/bookings", json={"member_id": 1, "session_id": 2})
    assert response.status_code == 409
    assert response.get_json()["error"] == "Session full"


def test_create_booking_duplicate(client):
    response = client.post("/api/bookings", json={"member_id": 1, "session_id": 1})
    assert response.status_code == 409


def test_create_booking_unknown_member(client):
    response = client.post("/api/bookings", json={"member_id": 999, "session_id": 1})
    assert response.status_code == 404


def test_create_booking_erroneous_data(client):
    response = client.post("/api/bookings", json={"member_id": "four", "session_id": 1})
    assert response.status_code == 400


def test_create_booking_requires_json(client):
    response = client.post("/api/bookings", data="member_id=1")
    assert response.status_code == 400


def test_delete_booking(client):
    assert client.delete("/api/bookings/1").status_code == 204
    assert client.delete("/api/bookings/1").status_code == 404


def test_stats(client):
    data = client.get("/api/stats").get_json()
    assert data["bookings_by_sport"][0] == {"sport": "Football", "bookings": 3}


def test_front_end_served(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Riverside Community Sports Club" in response.data
