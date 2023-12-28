-- SQLite
CREATE TABLE IF NOT EXISTS HOTELS (
    id_hotel INTEGER,
    id_city INTEGER,
    name_of_hotel TEXT,
    discription TEXT,
    PRIMARY KEY (id_hotel AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS ROOMS (
    id_room INTEGER,
    num_of_bed INTEGER,
    id_hotel INTEGER,
    id_people INTEGER,
    PRIMARY KEY (id_room AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS PEOPLES (
    id_people INTEGER,
    name TEXT,
    phone_num INTEGER,
    passport_cod INTEGER,
    id_city INTEGER,
    PRIMARY KEY (id_people AUTOINCREMENT)

);

CREATE TABLE IF NOT EXISTS CITIES (
    id_city INTEGER,
    name_city TEXT,
    id_country INTEGER,
    PRIMARY KEY (id_city AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS COUNTRIES (
    id_country INTEGER,
    name_of_country TEXT,
    phone_cod TEXT,
    passport_cod TEXT,
    PRIMARY KEY (id_country AUTOINCREMENT)
);