-- CREATE TABLE PEOPLE (
--     id INTEGER NOT NULL,
--     name TEXT NOT NULL DEFAULT 'unknown',
--     growth INTEGER NOT NULL DEFAULT 0,
--     age INTEGER NOT NULL DEFAULT 0,
--     city TEXT NOT NULL DEFAULT 'unknown',
--     street NOT NULL DEFAULT 'unknown',
--     PRIMARY KEY("id" AUTOINCREMENT)
-- );

-- INSERT INTO PEOPLE (name, growth, age, city, street)
-- VALUES ('gorge', 156, 16, 'Moscow', 'Alaben'),
--     ('artem', 178, 17, 'StPetersburg', 'Liniava'),
--     ('gorge', 167, 43, 'Harkev', 'Parinitchino'),
--     ('gorge', 144, 12, 'Rostov', 'Mercashichy'),
--     ('gorge', 186, 21, 'Moscow', 'Jolty')

-- SELECT city FROM PEOPLE
--     WHERE age >= 17 AND name LIKE 'a%m'

-- SELECT * FROM PEOPLE
-- WHERE id BETWEEN 6 and 12;

-- UPDATE PEOPLE SET name='pol'
-- WHERE name = 'gorge'

-- DELETE FROM PEOPLE
-- WHERE id in (3, 4, 5);

-- SELECT * FROM PEOPLE
