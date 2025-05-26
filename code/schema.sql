CREATE TABLE candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    skills TEXT,
    education TEXT,
    experience INTEGER,  -- in years
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE job_matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER,
    job_title TEXT,
    match_score REAL,
    FOREIGN KEY (candidate_id) REFERENCES candidates (id)
);