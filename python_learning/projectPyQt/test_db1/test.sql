CREATE TABLE IF NOT EXISTS CITIES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    visa_code TEXT
);

CREATE TABLE IF NOT EXISTS HOTELS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    id_city INTEGER,
    max_people INTEGER,
    num_of_guests INTEGER DEFAULT 0,
    price INTEGER
);

CREATE TABLE IF NOT EXISTS PEOPLE (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    visa_code TEXT,
    id_hotel INTEGER DEFAULT 0
);


-- /Incert
-- cities
INSERT INTO CITIES(name, visa_code)
VALUES 
-- hotels
INSERT INTO HOTELS(name, id_city, max_people, num_of_guests, price)
VALUES 
-- people
INSERT INTO PEOPLE(name, visa_code, id_hotel)
VALUES 