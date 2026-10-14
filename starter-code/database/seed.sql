-- Fictional seed data for the starter project.
INSERT INTO coach (name, email) VALUES
    ('Jordan Ellis', 'jordan.ellis@example.com'),
    ('Sam Okafor',   'sam.okafor@example.com'),
    ('Priya Shah',   'priya.shah@example.com');

INSERT INTO member (first_name, last_name, email, date_joined) VALUES
    ('Aisha',  'Khan',     'aisha.khan@example.com',     '2024-09-01'),
    ('Tom',    'Price',    'tom.price@example.com',      '2025-01-15'),
    ('Mei',    'Chen',     'mei.chen@example.com',       '2025-03-02'),
    ('Oliver', 'Bennett',  'oliver.bennett@example.com', '2025-06-20'),
    ('Grace',  'Adeyemi',  'grace.adeyemi@example.com',  '2026-02-11'),
    ('Noah',   'Williams', 'noah.williams@example.com',  '2026-09-05');

INSERT INTO session (name, sport, start_time, duration_minutes, capacity, price_pence, coach_id) VALUES
    ('Junior Football',  'Football', '2027-04-15 17:30', 60, 20, 500, 2),
    ('Netball Training', 'Netball',  '2027-04-15 19:00', 90, 2,  500, 3),
    ('Walking Football', 'Football', '2027-04-16 10:00', 60, 16, 300, 2),
    ('Fitness Circuit',  'Fitness',  '2027-04-17 18:00', 45, 25, 400, 1);

INSERT INTO booking (member_id, session_id, attended) VALUES
    (1, 1, NULL), (2, 1, NULL), (3, 2, NULL), (4, 2, NULL), (5, 3, NULL);
