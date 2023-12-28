-- DROP TABLE IF EXISTS CITIES;
-- DROP TABLE IF EXISTS HOTELS;
-- DROP TABLE IF EXISTS PEOPLE;

-- SELECT * FROM HOTELS
-- WHERE HOTELS.name LIKE "%Brown's%"

-- SELECT name, price FROM HOTELS
-- WHERE num_of_guests < max_people

-- SELECT name, visa_code FROM CITIES

-- SELECT name, price FROM HOTELS
-- WHERE
--     num_of_guests = max_people
--     AND id_city = (SELECT id FROM CITIES WHERE name = ?)

-- SELECT visa_code FROM CITIES
-- WHERE name = ?



-- INSERT INTO PEOPLE(name, visa_code, id_hotel)
-- VALUES (?, ?, ?)

-- SELECT id from HOTELS
-- WHERE name = ? AND id_city = (SELECT id FROM CITIES WHERE name = ?)



-- UPDATE HOTELS
-- SET num_of_guests=num_of_guests+1
-- WHERE
--     HOTELS.id = ?

SELECT * FROM HOTELS INNER JOIN PEOPLE ON HOTELS.id = PEOPLE.id_hotel
WHERE HOTELS.name = 'Shangri-La Lancaster'