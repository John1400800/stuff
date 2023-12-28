-- DROP TABLE ...;

-- CREATE TABLE CITY (
--     ID INTEGER NOT NULL,
--     name VARCHAR(70) UNIQUE,
--     name_country VARCHAR(70) NOT NULL DEFAULT 'UK',
--     PRIMARY KEY(ID AUTOINCREMENT)
-- );

-- INSERT INTO CITY (name)
-- VALUES ('London'),
--     ('Liverpool'),
--     ('Birmingham'),
--     ('Oxford'),
--     ('Cambridge'),
--     ('Manchester'),
--     ('Nottingham');

-- SELECT * FROM CITY;

-- CREATE TABLE PEOPLE (
--     ID INTEGER NOT NULL,
--     name VARCHAR(100) NOT NULL DEFAULT 'unknoun',
--     id_city INTEGER NOT NULL DEFAULT 1
--     phonenumber VARCHAR(30),
--     PRIMARY KEY(ID AUTOINCREMENT)
-- )