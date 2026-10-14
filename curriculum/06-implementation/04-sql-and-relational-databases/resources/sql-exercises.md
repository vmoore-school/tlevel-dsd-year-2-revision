# SQL Exercises (lesson 06.04)

Use the starter database: `starter-code/database/schema.sql` + `seed.sql`.

```bash
cd starter-code
sqlite3 practice.db < database/schema.sql
sqlite3 practice.db < database/seed.sql
sqlite3 practice.db
```
(Or open the files in DB Browser for SQLite.)

## DML: SELECT
1. List all sessions in start-time order.
2. List the names of football sessions that cost less than £5 (prices are stored in pence).
3. Show each session name with its coach's name. *(JOIN)*
4. Count the bookings for each session, **including sessions with zero bookings**. *(LEFT JOIN, GROUP BY)*
5. Show sessions that are full. *(HAVING)*
6. Find members who have never booked anything. *(LEFT JOIN ... WHERE ... IS NULL, or NOT IN)*
7. Total potential income per sport (bookings × price), highest first.

## DML: INSERT, UPDATE, DELETE
8. Add yourself as a member.
9. Book yourself onto "Walking Football".
10. Move "Fitness Circuit" to 18:30 on the same day.
11. Cancel your booking.
12. Try to book member 999 onto a session. What stops you, and why is that good?

## DDL
13. Create a `waiting_list` table (member, session, date added, position) with suitable keys and constraints.
14. Add a `phone` column to `member`.

## Security
15. Explain why `"SELECT * FROM member WHERE email = '" + email + "'"` is dangerous, and rewrite it
    as a parameterised query in Python (`?` placeholders).

---

<details><summary>Answers to 3, 4 and 6</summary>

```sql
-- 3
SELECT s.name, c.name AS coach FROM session s JOIN coach c ON c.coach_id = s.coach_id;

-- 4
SELECT s.name, COUNT(b.booking_id) AS bookings
FROM session s LEFT JOIN booking b ON b.session_id = s.session_id
GROUP BY s.session_id ORDER BY bookings DESC;

-- 6
SELECT m.first_name, m.last_name
FROM member m LEFT JOIN booking b ON b.member_id = m.member_id
WHERE b.booking_id IS NULL;
```
</details>
