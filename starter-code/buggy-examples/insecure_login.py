"""DELIBERATELY INSECURE example for lesson 06.06 (Secure coding). Do NOT use this code.

Task: find and fix every security problem. There are at least 6. Hints are at the bottom.
"""
import sqlite3

ADMIN_PASSWORD = "Password123"          # problem?
DB = sqlite3.connect(":memory:")
DB.execute("CREATE TABLE users (username TEXT, password TEXT, role TEXT)")
DB.execute("INSERT INTO users VALUES ('aisha', 'letmein', 'member')")
DB.execute("INSERT INTO users VALUES ('admin', 'Password123', 'admin')")


def login(username, password):
    query = f"SELECT role FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Running:", query)            # problem?
    row = DB.execute(query).fetchone()
    if row:
        return row[0]
    return "Login failed: user " + username + " does not exist or password wrong"


def welcome_page(username):
    return "<h1>Welcome " + username + "</h1>"


def delete_user(current_role, username):
    # Any logged-in user can call this
    DB.execute(f"DELETE FROM users WHERE username = '{username}'")


if __name__ == "__main__":
    print(login("aisha", "letmein"))
    print(login("' OR '1'='1' --", "anything"))   # what happens here?
    print(welcome_page("<script>alert('hi')</script>"))

# Hints: SQL injection · plain-text passwords (use hashing, e.g. werkzeug.security or bcrypt) ·
# hard-coded secret · sensitive data written to logs · XSS (escape output) · missing authorisation check ·
# error message reveals which part was wrong · no limit on login attempts
