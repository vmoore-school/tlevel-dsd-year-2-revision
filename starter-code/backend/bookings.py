"""Booking business rules, kept separate from the web layer so they are easy to unit test."""

MIN_ID = 1


class BookingError(Exception):
    """Raised when a booking breaks a business rule. `status` is the HTTP status to return."""

    def __init__(self, message, status=400):
        super().__init__(message)
        self.message = message
        self.status = status


def parse_id(value, field):
    """Validate that `value` is a whole number >= 1. Accepts ints or numeric strings."""
    if isinstance(value, bool):
        raise BookingError(f"{field} must be a whole number")
    try:
        number = int(value)
    except (TypeError, ValueError):
        raise BookingError(f"{field} must be a whole number") from None
    if str(number) != str(value).strip():
        raise BookingError(f"{field} must be a whole number")
    if number < MIN_ID:
        raise BookingError(f"{field} must be {MIN_ID} or more")
    return number


def spaces_left(capacity, booked):
    return max(capacity - booked, 0)


def create_booking(db, member_id, session_id):
    """Create a booking if the member and session exist, there is space, and it is not a duplicate."""
    member_id = parse_id(member_id, "member_id")
    session_id = parse_id(session_id, "session_id")

    if db.execute("SELECT 1 FROM member WHERE member_id = ?", (member_id,)).fetchone() is None:
        raise BookingError("Member not found", 404)

    session = db.execute(
        "SELECT capacity, (SELECT COUNT(*) FROM booking b WHERE b.session_id = s.session_id) AS booked "
        "FROM session s WHERE session_id = ?",
        (session_id,),
    ).fetchone()
    if session is None:
        raise BookingError("Session not found", 404)
    if spaces_left(session["capacity"], session["booked"]) == 0:
        raise BookingError("Session full", 409)

    existing = db.execute(
        "SELECT 1 FROM booking WHERE member_id = ? AND session_id = ?", (member_id, session_id)
    ).fetchone()
    if existing:
        raise BookingError("Member already booked on this session", 409)

    cursor = db.execute(
        "INSERT INTO booking (member_id, session_id) VALUES (?, ?)", (member_id, session_id)
    )
    db.commit()
    return cursor.lastrowid
