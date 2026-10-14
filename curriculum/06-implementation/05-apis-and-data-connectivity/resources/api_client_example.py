"""Calling an API, parsing JSON and connecting to a database (lesson 06.05). Standard library only.

Run from the repository root:
    python curriculum/06-implementation/05-apis-and-data-connectivity/resources/api_client_example.py
"""
import json
import os
import sqlite3
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

# --- 1. Parse a saved API response (works offline) ---
data = json.loads((ROOT / "sample-data" / "api-response-example.json").read_text())
print(f"Page {data['page']} of results, {data['total']} sessions in total")
for s in data["sessions"]:
    spaces = s["capacity"] - s["booked"]
    print(f" - {s['name']:<18} coach: {s['coach']['name']:<12} spaces: {spaces}")
print("Next page:", data["links"]["next"])

# --- 2. Call a live API (GET request to an endpoint) ---
# API keys belong in environment variables, NEVER in code:  export WEATHER_API_KEY=...
API_KEY = os.environ.get("WEATHER_API_KEY")   # not needed for the public API below; shown for practice
url = "https://api.postcodes.io/postcodes/SW1A1AA"   # free public API, no key required
try:
    with urllib.request.urlopen(url, timeout=5) as response:
        result = json.load(response)["result"]
        print(f"\nLive API: {result['postcode']} is in {result['admin_district']} ({result['region']})")
except (urllib.error.URLError, TimeoutError, KeyError) as error:
    print(f"\nLive API call failed (offline?): {error}")

# --- 3. Database connection: Python's DB-API (the same idea as JDBC/ODBC) ---
# connection -> cursor/statement -> parameterised query -> result set
conn = sqlite3.connect(":memory:")               # data source (a file name or server details)
conn.execute("CREATE TABLE session (id INTEGER PRIMARY KEY, name TEXT, booked INTEGER)")
conn.executemany("INSERT INTO session (id, name, booked) VALUES (?, ?, ?)",       # prepared statement
                 [(s["session_id"], s["name"], s["booked"]) for s in data["sessions"]])
conn.execute("UPDATE session SET booked = booked + 1 WHERE id = ?", (3,))           # update
conn.execute("DELETE FROM session WHERE id = ?", (2,))                              # delete
for row in conn.execute("SELECT id, name, booked FROM session ORDER BY id"):        # result set
    print("DB row:", row)
conn.close()

# JDBC equivalent (Java), for comparison:
#   Connection conn = DriverManager.getConnection("jdbc:mysql://host/club", user, password);
#   PreparedStatement ps = conn.prepareStatement("SELECT * FROM session WHERE id = ?");
#   ps.setInt(1, 3);  ResultSet rs = ps.executeQuery();
