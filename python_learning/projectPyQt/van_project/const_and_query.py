DB_PATH = r'hotels.db'

DATA_PATH = r'data.txt'

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
SELECT name, max_people - num_of_guests, price FROM HOTELS
WHERE
    num_of_guests < max_people
    AND id_city = (SELECT id FROM CITIES WHERE name = ?)'''

SQL_GET_BUSY_HOTELS = '''
SELECT name, max_people - num_of_guests, price FROM HOTELS
WHERE
    num_of_guests = max_people
    AND id_city = (SELECT id FROM CITIES WHERE name = ?)'''

SQL_GET_HOTEL_ID = '''
SELECT id from HOTELS
WHERE name = ? AND price = ?
AND id_city = (SELECT id FROM CITIES WHERE name = ?)
'''

SQL_UPDATE_ONE_GUEST = '''
UPDATE HOTELS
SET num_of_guests=num_of_guests+1
WHERE HOTELS.id = ?'''

SQL_DELETE_ONE_GUEST = '''
UPDATE HOTELS
SET num_of_guests=num_of_guests-1
WHERE HOTELS.id = ?'''

SQL_CLEAR_HOTEL_ID = '''
UPDATE PEOPLE
SET id_hotel=0
WHERE id_hotel = ? AND name = ?;'''

SQL_INSERT_MAN = '''
INSERT INTO PEOPLE(name, visa_code, id_hotel)
VALUES (?, ?, ?)'''

GET_PEOPLE_FROM_HOTEL = """
SELECT PEOPLE.name, visa_code FROM HOTELS
INNER JOIN PEOPLE ON HOTELS.id = PEOPLE.id_hotel
WHERE HOTELS.id = ?"""
