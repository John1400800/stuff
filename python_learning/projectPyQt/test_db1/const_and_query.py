DB_PATH = r'projectPyQt\test_db1\hoteles1.db'

DATA_PATH = r'projectPyQt\test_db1\data.txt'

SQL_CREATE_DB = '''
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
'''

SQL_DELETE_DB = '''
DROP TABLE IF EXISTS CITIES;
DROP TABLE IF EXISTS HOTELS;
DROP TABLE IF EXISTS PEOPLE;
'''

SQL_HALF_INSERT_CITIES = '''
INSERT INTO CITIES(name, visa_code)
VALUES '''

SQL_HALF_INSERT_HOTELS = '''
INSERT INTO HOTELS(name, id_city, max_people, num_of_guests, price)
VALUES '''

SQL_HALF_INSERT_PEOPLE = '''
INSERT INTO PEOPLE(name, visa_code, id_hotel)
VALUES '''

SQL_GET_CITIES = '''
SELECT name, visa_code FROM CITIES'''

SQL_GET_VISA = '''
SELECT visa_code FROM CITIES
WHERE name = ?'''

SQL_GET_FREE_HOTELS = '''
SELECT name, price FROM HOTELS
WHERE
    num_of_guests < max_people
    AND id_city = (SELECT id FROM CITIES WHERE name = ?)'''

SQL_GET_BUSY_HOTELS = '''
SELECT name, price FROM HOTELS
WHERE
    num_of_guests = max_people
    AND id_city = (SELECT id FROM CITIES WHERE name = ?)'''

SQL_GET_HOTEL_ID = '''
SELECT id from HOTELS
WHERE name = ? AND id_city = (SELECT id FROM CITIES WHERE name = ?)
'''

SQL_UPDATE_ONE_GUEST = '''
UPDATE HOTELS
SET num_of_guests=num_of_guests+1
WHERE HOTELS.id = ?'''

SQL_INSERT_MAN = '''
INSERT INTO PEOPLE(name, visa_code, id_hotel)
VALUES (?, ?, ?)'''
