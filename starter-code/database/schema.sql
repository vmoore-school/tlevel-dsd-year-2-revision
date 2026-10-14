-- Riverside Community Sports Club: starter schema (SQLite dialect)
-- Normalised to 3NF. See curriculum/04-design/12-database-design for the worked example.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS session;
DROP TABLE IF EXISTS coach;
DROP TABLE IF EXISTS member;

CREATE TABLE member (
    member_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name    VARCHAR(50)  NOT NULL,
    last_name     VARCHAR(50)  NOT NULL,
    email         VARCHAR(254) NOT NULL UNIQUE,
    date_joined   DATE         NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE coach (
    coach_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name          VARCHAR(100) NOT NULL,
    email         VARCHAR(254) NOT NULL UNIQUE
);

CREATE TABLE session (
    session_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name             VARCHAR(100) NOT NULL,
    sport            VARCHAR(50)  NOT NULL,
    start_time       DATETIME     NOT NULL,
    duration_minutes INTEGER      NOT NULL CHECK (duration_minutes BETWEEN 15 AND 240),
    capacity         INTEGER      NOT NULL CHECK (capacity BETWEEN 1 AND 50),
    price_pence      INTEGER      NOT NULL CHECK (price_pence >= 0),
    coach_id         INTEGER      NOT NULL REFERENCES coach(coach_id)
);

CREATE TABLE booking (
    booking_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id     INTEGER  NOT NULL REFERENCES member(member_id),
    session_id    INTEGER  NOT NULL REFERENCES session(session_id),
    booked_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    attended      BOOLEAN,
    UNIQUE (member_id, session_id)
);
